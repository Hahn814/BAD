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
#-----------------------------------------------------------------------

class CaptureImage:
    home_directory = "http://10.5.5.9:8080/videos/DCIM/100GOPRO/"
    imageID = "frame.jpeg"
    targetID = "target.png"
    gopro = UC()
    path = "/home/paul/workspace/BAD/captureImage"

    def __init__(self):
        print "Initializing GoPro.."
        #self.gopro.turn_on()             # turn on the gopro
        #self.begin_capture()

    def capture_photo(self):
        self.gopro.enable_photo_mode()   # Enable still photos
        self.gopro.start_capture()       # capture a photo
        self.gopro.stop_capture()
        self.get_photo()

    def capture_video(self):
        self.gopro.enable_camera_mode()  # enable camera video mode
        self.gopro.start_capture()

    def get_photo(self):
        self.gopro.get_photo()   # This will download the latest photo to the image directory
        self.imageID = self.gopro.get_image_id()

    def begin_capture(self):
        self.capture_photo()

    def shutdown(self):
        self.gopro.turn_off()

cap = CaptureImage()
# Read in the images
os.chdir(cap.path)
img1 = cv2.imread(cap.targetID,0)  #image we are looking for 
os.chdir(cap.path + "/img")
img2 = cv2.imread(cap.imageID,0)        #current frame input, this will be camera frame input later.
surf = cv2.xfeatures2d.SURF_create(400)
# find the keypoints and descriptors with SIFT
kp1, des1 = surf.detectAndCompute(img1,None)
kp2, des2 = surf.detectAndCompute(img2,None)

# FLANN parameters
FLANN_INDEX_KDTREE = 0
index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
search_params = dict(checks=50)   # or pass empty dictionary
 
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
