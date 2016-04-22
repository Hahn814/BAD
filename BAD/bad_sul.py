import socket
import subprocess

# Create an INET servee socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind socket to port and host
# bind (address, port)
serversocket.bind((socket.gethostname(), 80))

# Listen for a single connection from the GCU
serversocket.listen(1)

# accept incoming client connections
(clientsocket, addr) = serversocket.accept()

print "Start up message recieved: " + str(clientsocket.getsockname)
print "Starting main execution loop.."

subprocess.call("/home/BAD/BAD/./bad-init.sh")
