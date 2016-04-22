import socket

#create an INET socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print "Attempting to notify Edison.."

try:
    s.connect(("192.168.2.27", 80))
    print "Notification successful"
except RuntimeError:
    print "Notification failed.."
