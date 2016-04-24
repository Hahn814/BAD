import socket
import subprocess

PORT_NUMBER = 2016

subprocess.call(['python','WiFiSwitcher.py','network', 'ssid', 'psk'])
# Create an INET servee socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
HOST_NAME =  socket.gethostbyname('0.0.0.0')
# Bind socket to port and host
# bind (address, port)
serversocket.bind((HOST_NAME, PORT_NUMBER))

print "Listening on port " +  str(PORT_NUMBER) + " for startup message.. " + str(HOST_NAME)
# Listen for a single connection from the GCU

# accept incoming client connections

(data, addr) = serversocket.recvfrom(1024)

print "Start up message recieved: " + data
print "Starting main execution loop.."

print "Un comment the below section you ninny"
#process = subprocess.Popen('./bad-init.sh', shell=True, stdout=subprocess.PIPE)
#process.wait()
#print process.returncode
