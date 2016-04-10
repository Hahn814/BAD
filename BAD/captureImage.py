from urlCommands import UrlCommands as UC   # A collection of url commands to request go pro actions
import cv2
import numpy as np
import os
import time
import threading


# Home cherokee directory:
# http://10.5.5.9:8080/videos/DCIM/100GOPRO/
#-----------------------------------------------------------------------\
# Adjustments when testing within edison:
# remove comments in init constructor
# imshow method must be removed
# search thread : replace append frame with commented append command
# path must be changed to /media/external... for the Edison sd card directory
# home_directory = "http://10.5.5.9:8080/videos/DCIM/100GOPRO/"
#-----------------------------------------------------------------------

class CaptureImage:

    def __init__(self):
        # Make sure the GoPro is turned on, initialize settings and begin capture.
        self.imageID = ["frame.jpeg"]
        self.current = "frame.jpeg"
        self.targetID = "target.png"
        self.gopro = UC()
        self.path = os.getcwd()
        print self.path
        print "Initializing GoPro.."
        res = self.gopro.turn_on()
        time.sleep(5)
        
    def start_photo_thread(self):
        # capture thread to capture photos during flight
        t1 = time.time()
        print "Started " + threading.currentThread().getName()
        im_count = 2
        
        while 1:
            res = self.gopro.start_capture()
            res = self.gopro.stop_capture()  
            time.sleep(10)
            im_count += 1  
            print threading.currentThread().getName() + "image count: " + str(im_count)
            
        t2 = time.time() - t1
        print "Closed " + threading.currentThread().getName() + " :: " + str(t2) + "s"
        
    def start_search_thread(self):
        # thread to handle the URL requests, we dont want them to cause the captures to fall behind
        print "Started " + threading.currentThread().getName()
        img_count = 1
        t1 = time.time()
        
        while 1:
            try:
                img_count += 1
                #self.imageID.append("frame.jpeg")
                self.imageID.append(self.get_photo())     # Add newest photo to list
                print "\n" + "Photo List:" + str(self.imageID)
                print threading.currentThread().getName() + "image count: " + str(img_count)
            except:
                print "Exception Search Thread"
                
        t2 = time.time() - t1
        print "Closed " + threading.currentThread().getName() + " :: " + str(t2) + "s"
        print "Frames Captured: " + str(img_count)
        
    def start_process_thread(self):
        # Thread to process images left in stack
        print "Started " + threading.currentThread().getName()
        proc_count = 0
        t1 = time.time()
        hits = 0
        
        os.chdir(cap.path)
        # Collect the images captured
        img1 = cv2.imread(cap.targetID,0)   # Target image from user.
        # Create the SURF object
        surf = cv2.xfeatures2d.SURF_create(500)
        kp1, des1 = surf.detectAndCompute(img1, None) # Detect target keypoints
        
        # FLANN parameters needed for flann matcher
        FLANN_INDEX_KDTREE = 0
        index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
        search_params = dict(checks=50)   # higher the # = more accurate/slower
        flann = cv2.FlannBasedMatcher(index_params,search_params)
        
        # While thread is executing capture images
        # If index is going to be exceeded, wait until it is updated
        while 1:
            try:
                
                if (len(self.imageID) > proc_count):
                    os.chdir(cap.path + "/img")
                    img2 = cv2.imread(cap.imageID[proc_count],0)    # Current frame from GoPro
                    print "\nPROCESS IMAGE:" + cap.imageID[proc_count]
                    # calculate current frames keypoints
                    if(os.path.isfile(cap.imageID[proc_count])):
                        kp2, des2 = surf.detectAndCompute(img2, None)
                        
                        # Create and match descriptors
                        matches = flann.knnMatch(des1,des2,k=2)
                        
                        # Need to draw only good matches, so create a mask
                        matchesMask = [[0,0] for i in xrange(len(matches))]
                        
                        # Lowe's ratio test to get the closest matching vectors
                        good = []
                        for i,(m,n) in enumerate(matches):
                             if m.distance < 0.6*n.distance:
                                 matchesMask[i]=[1,0]
                                 good.append(m) # Append the good match for count/comparison
                                 
                        # Adjust the drawing parameters
                        draw_params = dict(matchColor = (0,255,0),
                                            singlePointColor = (255,255,255),
                                            matchesMask = matchesMask,
                                            flags = 0)
                                            
                        # Draw the image found and save to hits directory
                        hit = cv2.drawMatchesKnn(img1,kp1,img2,kp2,matches,None,**draw_params)
                        
                        # Write the hit to file
                        os.chdir(cap.path + "/hits")
                        cv2.imwrite("hit.jpeg", hit)
                        
                        if(len(good)>10):
                            hits += 1
                            print "Hit: " + str(hits) + ", Img KP Count: " + str(len(good))
                            
                    proc_count += 1
                    print threading.currentThread().getName() + "Process count: " + str(proc_count)
            except:
                print "Failed - sleep 3"
                time.sleep(3)
                
        t2 = time.time() - t1
        print "Closed " + threading.currentThread().getName() + " :: " + str(t2) + "s"
        print "Hits: " + str(hits)
        
    def capture_video(self):
        res = self.gopro.enable_camera_mode()  # enable camera video mode
        res = self.gopro.start_capture()

    def get_photo(self):
        res = self.gopro.get_photo()   # This will download the latest photo to the image directory
        print "Image Recieved: " + self.gopro.get_image_id()
        return self.gopro.get_image_id()

    def begin_capture(self):
        print "Init Threading.."
        # Init all of the GoPro Settings to capture a photo
        res = self.gopro.enable_photo_mode()
        res = self.gopro.start_capture()
        res = self.gopro.stop_capture()
        # Create the capture and upload threads
        t1 = threading.Thread(name="capture_thread", target=cap.start_photo_thread)
        t1.setDaemon(True)
        t2 = threading.Thread(name="cherokee_thread", target=cap.start_search_thread)
        t1.setDaemon(True)
        t3 = threading.Thread(name="process_thread", target=cap.start_process_thread)
        t1.setDaemon(True)
        # Start the threads for processing to begin
        t1.start()
        t2.start()
        t3.start()
        t1.join()
        t2.join()
        t3.join()
        
    def shutdown(self):
        res = self.gopro.turn_off()

cap = CaptureImage()
cap.begin_capture()


