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
# path must be changed to /media/external... for the Edison sd card directory
# home_directory = "http://10.5.5.9:8080/videos/DCIM/100GOPRO/"
#-----------------------------------------------------------------------

class CaptureImage:

    def __init__(self):
        # Make sure the GoPro is turned on, initialize settings and begin capture.
        self.imageID = "frame.jpeg"
        self.targetID = "target.png"
        self.goproURL = UC()
        self.path = os.getcwd()
        print self.path
        print "Initializing GoPro.."
        #self.gopro.turn_on()
        
    def start_photo_thread(self):
        # capture thread to capture photos during flight
        print "Started " + threading.currentThread().getName() + " " + str(time.time())
        print "Closed " + threading.currentThread().getName() + " " + str(time.time())
        
    def start_search_thread(self):
        # thread to handle the URL requests, we dont want them to cause the captures to fall behind
        print "Started " + threading.currentThread().getName() + " " + str(time.time())
        print "Closed " + threading.currentThread().getName() + " " + str(time.time())
        
    def capture_video(self):
        self.gopro.enable_camera_mode()  # enable camera video mode
        self.gopro.start_capture()

    def get_photo(self):
        self.gopro.get_photo()   # This will download the latest photo to the image directory
        self.imageID = self.gopro.get_image_id()

    def begin_capture(self):
        print "Init Threading.."
        # Init all of the GoPro Settings to capture a photo
        # self.gopro.enable_photo_mode()
        # self.gopro.start_capture()
        # self.gopro.stop_capture()
        self.start_search_thread()
        self.start_photo_thread()
        
    def shutdown(self):
        self.gopro.turn_off()

cap = CaptureImage()
t1 = threading.Thread(name="capture_thread", target=cap.start_photo_thread)
t2 = threading.Thread(name="cherokee_thread", target=cap.start_search_thread)
t1.start()
t2.start()
# Collect the images captured
os.chdir(cap.path)
img1 = cv2.imread(cap.targetID,0)   # Target image from user.
os.chdir(cap.path + "/img")
img2 = cv2.imread(cap.imageID,0)    # Current frame from GoPro

t1 = time.time()

# Create the ORB object
orb = cv2.ORB_create()
kp1 = orb.detect(img1,None)
kp2 = orb.detect(img2,None)

# Get the descriptors of each image
kp1, des1 = orb.compute(img1, kp1)
kp2, des2 = orb.compute(img2, kp1)

# FLANN parameters needed for flann matcher
FLANN_INDEX_KDTREE = 0
index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
search_params = dict(checks=50)   # higher the # = more accurate/slower
 
# Create and match descriptors
flann = cv2.FlannBasedMatcher(index_params,search_params)
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
print (str(time.time()-t1) + " s " + 
                "\nTotal Matches: "+ 
                str(len(matches)))
os.chdir(cap.path + "/hits")
cv2.imwrite("hit.jpeg", hit)
