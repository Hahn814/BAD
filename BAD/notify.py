import socket
import time
import subprocess

# These should be an adjustable variable in the future
SERVER_IP = '192.168.2.25'
PORT_NUMBER = 2016

# create the INET socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print "Attempting to notify Edison.."

try:
    # connect and push a message to start
    s.connect((SERVER_IP, 2016))
    print "<< Notification successful >>"
    s.send('START')

except Exception as e:
    print "<< Notification failed >>"
    print e


print("Program dialog will close..")
time.sleep(5.5)
