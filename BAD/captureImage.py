from urlCommands import UrlCommands as UC  # A collection of url commands to request go pro actions
import time
import cv2
import numpy as np
import os


# Home cherokee directory:
# http://10.5.5.9:8080/videos/DCIM/100GOPRO/


class CaptureImage:
    home_directory = "http://10.5.5.9:8080/videos/DCIM/100GOPRO/"
    imageID = ""
    gopro = UC()

    def __init__(self):
        print "hey"
        self.gopro.turn_on()             # turn on the gopro
        self.begin_capture()

    def capture_photo(self):
        self.gopro.enable_photo_mode()   # Enable still photos
        self.gopro.start_capture()       # capture a photo
        self.gopro.stop_capture()
        time.sleep(1)
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
target_img = cv2.imread('targetimage.jpeg',0)  #image we are looking for 
img = cv2.imread('currentframe.jpeg',0)        #current frame input, this will be camera frame input later.
# use the orb object to capture the images keypoints and descriptors.
orb = cv2.ORB_create()
kp1, des1 = orb.detectAndCompute(target_img, None)       
kp2, des2 = orb.detectAndCompute(img, None)

# Use the brute force algorithm (temporary) to match like keypoints
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
matches = bf.match(des1,des2)
hit = cv2.drawMatches(target_img,kp1,img,kp2,matches[:10],None, flags=2)
if matches.len > 10:
	os.chdir("/media/external/hits")
	cv2.imwrite("hit.jpeg", hit)
cv2.waitKey(0)
cv2.destroyAllWindows()
