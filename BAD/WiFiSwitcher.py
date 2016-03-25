from urlCommands import UrlCommands as UC
import fileinput
import os
import sys

if len(sys.argv) > 1:
    fileLocation = "/etc/network/"      # Directory of the wifi configuration file
    fileToSearch = "interfaces"         # Wifi file name
    searchText1 = "wpa-ssid"            # tags to find correct line within file
    searchText2 = "wpa-psk"             # .
    valid = False

    if sys.argv[1] == "network":
        WiFi = "wpa-ssid " + sys.argv[2]     # replacement lines
        Psk = "wpa-psk " + sys.argv[3]       # .
        valid = True
    else:
        if sys.argv[1] == "gopro":
            WiFi = "wpa-ssid " + UC.ip     # replacement lines
            Psk = "wpa-psk " + UC.pw       # .
            valid = True

    if valid:
        temp = os.getcwd()                  # capture original directory to return to afterward
        os.chdir(fileLocation)

        f = open(fileToSearch , mode='wb')
        fileContents = f.readlines()

        for line in fileContents:
            if searchText1 in line:
                line = WiFi

            else:
                if searchText2 in line:
                    line = Psk

        os.chdir(temp)
    else:
        "WiFiSwitcher.py :: Argument used is not valid, valid syntax: \n" \
            "\python WiFiSwitcher.py gopro \npython WiFiSwitcher.py wifiSSID wifiPSK "
else:
    print "WiFiSwitcher.py :: Incorrect number of command line arguments used."
    
