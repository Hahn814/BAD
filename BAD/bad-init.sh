echo "Initializing Beacon Autonomous Drone Software Dependencies."
echo "disable library libdc1394 :: ln /dev/null /dev/raw1394"
ln /dev/null /dev/raw1394

cd /home/BAD/BAD
ifdown wlan0
python WiFiSwitcher.py NetworkSSID NetworkPSK
ifup wlan0

echo "Searching network drive for user's target image.. CL param = target.png"
python acquireImageTarget.py target.png

echo "Connecting to GoPro Independent WiFi Network.."
echo "python WiFiSwitcher.py gopro"

ifdown wlan0
python WiFiSwitcher.py gopro
ifup wlan0

echo "python captureimage.py"
python captureimage.py
