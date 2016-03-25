echo "This shell command has not been updated yet, disable driver, ensure GoPro WiFi, run captureImage.py"
echo "disable driver"

echo "cd /etc/network/
echo "run switcher python script - connect to wifi network for ftp"
~ python WiFiSwitcher.py wifissid wifipsk


echo "run ftp script to retrieve target"

echo "run switcher python script - switch to gopro wifi"
echo "python WiFiSwitcher.py gopro"

echo "python captureimage.py"
