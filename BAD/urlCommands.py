import urllib2
import urllib
import re
import os

# structure : http://<ip>/<device>/<app>?t=<password>&p=<command>


class UrlCommands:
    pw = "SeniorProject"
    ip = "10.5.5.9"
    ssid = "vinniesgopro"
    device = ""
    app = ""
    command = ""
    url = ""
    current = ""
    imageid = ""

    def __init__(self):
        self.command = ""

    # http://<ip>/camera/VR?t=<password>&p=%00
    def build_url(self, dev, a, com):
        self.url = "http://" + self.ip + "/" + dev + "/" + a + "?t=" + self.pw + "&p=" + "%" + com
        try:
            urllib2.urlopen(self.url)
            print self.url + " Command Sent.."
            current = ""
        except urllib2.URLError:
            print "An error occurred while attempting to retrieve url: " + self.url

# BACPAC device commands: off, on, change_mode, start/stop capture
# http://<ip>/bacpac/PW?t=<password>&p=%01
    def turn_off(self):
        device = "bacpac"
        app = "PW"
        command = "00"
        current = "\tBACPAC:PW:00: Power down.."
        self.build_url(device, app, command)
        return device + app + command

    def turn_on(self):
        device = "bacpac"
        app = "PW"
        command = "01"
        current = "\tBACPAC:PW:01: Power On.."
        self.build_url(device, app, command)
        return device + app + command

    def change_mode(self):
        device = "bacpac"
        app = "PW"
        command = "02"
        current = "\tBACPAC:PW:02: Change Mode."
        self.build_url(device, app, command)
        return device + app + command

# http://<ip>/bacpac/SH?t=<password>&p=%01
    def start_capture(self):
        device = "bacpac"
        app = "SH"
        command = "01"
        current = "\tBACPAC:SH:01: * Start Capture"
        self.build_url(device, app, command)
        return device + app + command

    def stop_capture(self):
        device = "bacpac"
        app = "SH"
        command = "00"
        current = "\tBACPAC:SH:00: * Stop Capture"
        self.build_url(device, app, command)
        return device + app + command
# Camera preview methods on/off
# http://<ip>/camera/PV?t=<password>&p=%02
    def preview_on(self):
        device = "camera"
        app = "PV"
        command = "02"
        current = "\tCAMERA:PV:02: Preview On"
        self.build_url(device, app, command)

    def preview_off(self):
        device = "camera"
        app = "PV"
        command = "00"
        current = "\tCAMERA:PV:00: Preview Off"
        self.build_url(device, app, command)
        return device + app + command

# Camera mode methods
# http://<ip>/camera/CM?t=<password>&p=%00
    def enable_camera_mode(self):
        device = "camera"
        app = "CM"
        command = "00"
        self.build_url(device, app, command)
        return device + app + command

    def enable_photo_mode(self):
        device = "camera"
        app = "CM"
        command = "01"
        current = "\tCAMERA:CM:01: Photo Mode Enabled"
        self.build_url(device, app, command)
        return device + app + command

    def enable_burst_mode(self):
        device = "camera"
        app = "CM"
        command = "02"
        self.build_url(device, app, command)
        return device + app + command

    def enable_tl_mode(self):
        device = "camera"
        app = "CM"
        command = "03"
        self.build_url(device, app, command)
        return device + app + command

    def enable_tl2_mode(self):
        device = "camera"
        app = "CM"
        command = "04"
        self.build_url(device, app, command)
        return device + app + command

# Camera orientation methods
# http://<ip>/camera/UP?t=<password>&p=%00
    def set_head_up(self):
            device = "camera"
            app = "UP"
            command = "00"
            self.build_url(device, app, command)
            return device + app + command

    def set_head_down(self):
            device = "camera"
            app = "UP"
            command = "01"
            self.build_url(device, app, command)
            return device + app + command

# Video resolution methods
# http://<ip>/camera/VR?t=<password>&p=%00
    def set_video_resolution(self, r):

        if r == 'WVGA-60':
            command = "00"
        elif r == 'WVGA-120':
            command = "01"
        elif r == '720-30':
            command = "02"
        elif r == '720-60':
            command = "03"
        elif r == '960-30':
            command = "04"
        elif r == '960-60':
            command = "05"
        elif r == '1080-30':
            command = "06"
        else:
            print "Error occurred while setting camera's video resolution: " + r + " is not a valid parameter"
            command = "00"

        device = "camera"
        app = "VR"
        self.build_url(device, app, command)
        return device + app + command

    # methods to set photo resolutions
    # http://<ip>/camera/PR?t=<password>&p=%00
    def set_photo_resolution(self, r):
        if r == '11MP_WIDE':
            command = "00"
        elif r == '8MP_MEDIUM':
            command = "01"
        elif r == '5MP_WIDE':
            command = "02"
        elif r == '5MP_MEDIUM':
            command = "03"
        else:
            print "Error occurred while setting camera's photo resolution: " + r + " is not a valid parameter"
            command = "00"

        device = "camera"
        app = "PR"
        self.build_url(device, app, command)
        return device + app + command

    # Camera timer settings
    # http://<ip>/camera/TI?t=<password>&p=%00
    def set_timer(self, tm):
        if tm == 0.5:
            command = "00"
        elif tm == 1:
            command = "01"
        elif tm == 2:
            command = "02"
        elif tm == 5:
            command = "03"
        elif tm == 10:
            command = "04"
        elif tm == 30:
            command = "05"
        elif tm == 60:
            command = "06"
        else:
            print "Error occurred::<set_timer>::timer interval: " + tm + " is not a valid parameter"
            command = "00"

        device = "camera"
        app = "TI"
        self.build_url(device, app, command)
        return device + app + command

    # home_directory = "http://10.5.5.9:8080/videos/DCIM/100GOPRO/"
    def get_photo(self):
        home_dir = "http://" + self.ip + ":8080/videos/DCIM/101GOPRO/"  # Cherokee Web Server
        repeat = True
        
        # Waiting for the server to update
        while repeat == True:
            path = urllib2.urlopen(home_dir)                                # Get the Cherokee URL
            string = path.read()                                            # Get the HTML info from web server
            pattern = re.compile('\w\w\w\w\w\w\w\w.JPG"')                   # regular expression to find all JPG names
            files = pattern.findall(string)                                 # get the filenames into a list
            temp = files[-1].replace('\"', "")
            
            if temp != self.imageid:
                self.imageid = temp
                repeat = False
                

        urllib.urlretrieve(home_dir+self.imageid, self.imageid)         # get the last element from the list
        print("Cherokee_Downloaded " + self.imageid)
        return self.imageid
                
# This will staydisabled during the testing phase, in order to follow frames captured
#        for i in os.listdir("media/external/img"):  # remove all previous images
#            os.remove(i)


    def get_image_id(self):
        return self.imageid


