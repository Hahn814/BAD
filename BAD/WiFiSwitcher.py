from urlCommands import UrlCommands as UC
import os
import sys


if len(sys.argv) > 1:
    #fileLocation = "/etc/network/"                     # Directory of the wifi configuration file
    fileLocation = "/home/paul/workspace/BAD/BAD"      # Directory of the wifi configuration file

    fileToSearch = "interfaces"         # Wifi file name
    searchText1 = "wpa-ssid"            # tags to find correct line within file
    searchText2 = "wpa-psk"             # .
    valid = False

    
    if sys.argv[1] == "network":
        print sys.argv[1]
        WiFi = "wpa-ssid " + sys.argv[2]     # replacement lines
        Psk = "wpa-psk " + sys.argv[3]       # .
        valid = True
    else:
        if sys.argv[1] == "gopro":
            print sys.argv[1]
            WiFi = "wpa-ssid " + UC.ssid     # replacement lines
            Psk = "wpa-psk " + UC.pw       # .
            valid = True

    if valid:
        temp = os.getcwd()                  # capture original directory to return to afterward
        os.chdir(fileLocation)
            
        f = open(fileToSearch , mode='rb')
        fileContents = f.readlines()
        
        count = 0
        for line in fileContents:
            
            if searchText1 in line:
                line = WiFi + "\n"

            else:
                if searchText2 in line:
                    line = Psk + "\n"
                    
            fileContents[count] = line
            count = count + 1
        f.close()
        
        f = open(fileToSearch , mode='w+')
        print fileContents
        f.writelines(fileContents)
        
        
        os.chdir(temp)
    else:
        print "WiFiSwitcher.py :: Argument used is not valid, valid syntax: \n" \
            "\python WiFiSwitcher.py gopro \npython WiFiSwitcher.py wifiSSID wifiPSK "
else:
    print "WiFiSwitcher.py :: Incorrect number of command line arguments used."
    
