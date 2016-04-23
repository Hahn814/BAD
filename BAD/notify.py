import socket
import time
import subprocess

subprocess.call("/home/BAD/BAD/python WiFiSwitcher.py network ssid psk")

# create an INET socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print "Attempting to notify Edison.."

try:
    s.connect((socket.gethostname(), 2016))
    print "<< Notification successful >>"

except Exception as e:
    print "<< Notification failed >>"
    print e


print("Program dialog will close..")
time.sleep(5.5)
