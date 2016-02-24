from urlCommands import UrlCommands as UC   # A collection of url commands to request go pro actions
import cv2
import numpy as np
import os


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
    imageID = "frame.jpeg"
    targetID = "target.png"
    gopro = UC()
    path = "/home/paul/workspace/BAD/captureImage"

    def __init__(self):
        # Make sure the GoPro is turned on, initialize settings and begin capture.
        print "Initializing GoPro.."
        #self.gopro.turn_on()
        #self.begin_capture()

    def start_photo_thread(self):
        # capture thread to capture photos during flight
        self.gopro.start_capture()
        self.gopro.stop_capture()

    def start_search_thread(self):
        # thread to handle the URL requests, we dont want them to cause the captures to fall behind
        self.get_photo()
        
    def capture_video(self):
        self.gopro.enable_camera_mode()  # enable camera video mode
        self.gopro.start_capture()

    def get_photo(self):
        self.gopro.get_photo()   # This will download the latest photo to the image directory
        self.imageID = self.gopro.get_image_id()

    def begin_capture(self):
        # Init all of the GoPro Settings to capture a photo
        self.gopro.enable_photo_mode()
        self.gopro.start_capture()
        self.gopro.stop_capture()
        self.start_search_thread()
        self.start_photo_thread()
        
    def shutdown(self):
        self.gopro.turn_off()

cap = CaptureImage()
# Read in the images
os.chdir(cap.path)
#image we are looking for 
img1 = cv2.imread(cap.targetID,0)
os.chdir(cap.path + "/img")
#current frame input, this will be camera frame input later.
img2 = cv2.imread(cap.imageID,0)
orb = cv2.ORB_create()
# find the keypoints and descriptors with SIFT
kp1, des1 = orb.detectAndCompute(img1,None)
kp2, des2 = orb.detectAndCompute(img2,None)

# FLANN parameters
FLANN_INDEX_KDTREE = 0
index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
search_params = dict(checks=50)   # lower the checks, faster the computation, but less accurate.
 
flann = cv2.FlannBasedMatcher(index_params,search_params)
  
matches = flann.knnMatch(des1,des2,k=2)
 
# Need to draw only good matches, so create a mask
mask = [[0,0] for i in xrange(len(matches))]
 
# lowe's ratio test to find elements within range
for i,(m,n) in enumerate(matches):
     if m.distance < 0.6*n.distance:
         mask[i]=[1,0]
 
draw_params = dict(matchColor = (0,255,0),
                    singlePointColor = (255,255,255),
                    mask = mask,
                    flags = 0)

hit = cv2.drawMatchesKnn(img1,kp1,img2,kp2,matches,None,**draw_params)
os.chdir(cap.path + "/hits")
cv2.imwrite("hit.jpeg", hit)
