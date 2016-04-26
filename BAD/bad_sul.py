import socket
import subprocess

PORT_NUMBER = 2016

# Command Line: python WiFiSwitcher.py network ssid psk
subprocess.call(['python','WiFiSwitcher.py','network', 'ssid', 'psk'])
# Create an INET servee socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
HOST_NAME =  socket.gethostbyname('0.0.0.0')
# Bind socket to port and host
# bind (address, port)
serversocket.bind((HOST_NAME, PORT_NUMBER))

print "Listening on port " +  str(PORT_NUMBER) + " for startup message.. " + str(HOST_NAME)

# accept incoming client message
(data, addr) = serversocket.recvfrom(1024)

print "Start up message recieved: " + data
print "Starting main execution loop.."

# run the shell command script to begin program execution. 
process = subprocess.Popen('./bad-init.sh', shell=True, stdout=subprocess.PIPE)
process.wait()
print process.returncode
