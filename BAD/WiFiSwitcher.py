from urlCommands import UrlCommands as UC
import fileinput
import os

fileLocation = "/etc/network/"      # Directory of the wifi configuration file
fileToSearch = "interfaces"         # Wifi file name
searchText1 = "wpa-ssid"            # tags to find correct line within file
searchText2 = "wpa-psk"             # .
goProWiFi = "wpa-ssid " + UC.ip     # replacement lines
goProPsk = "wpa-psk " + UC.pw       # .

temp = os.getcwd()                  # capture original directory to return to afterward
os.chdir(fileLocation)

f = open(fileToSearch , mode='wb')
fileContents = f.readlines()

for line in fileContents:
    if searchText1 in line:
        line = goProWiFi

    else:
        if searchText2 in line:
            line = goProPsk

os.chdir(temp)
