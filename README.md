START UP PROCEDURE:

    1. ADJUST ALL PARAMETER TO REFLECT CURRENT SITUATION:
            + Switch from testing directory, to intel edison interfaces directory within WiFiSwitcher.py (/etc/network/)
            + Enter Correct CL parameters for bad-init.sh
                - WiFiSwitcher (x2)
                - acquireTargetImage

    2. PIXHAWK AND MISSION PLANNER SETUP
            + ESC calibration
            + Transmitter calibration
            + Ensure GPS lock
            + Write mission waypoint to PixHawk
            + Flight Modes
            
    3. Intel Edison
            + Power on Edison
            + When image is selected and continure button is selected in target UI on GCU the Edison will begin automation of capture process.
            + On landing Edison can be powered off with UAV
            
    4. Retreive Images
            + Unprocessed Images: via GoPro SD card or Cherokee Server
            + Processed Images: via Intel Edison /home/BAD/BAD/img and ../hits directories. 
            

