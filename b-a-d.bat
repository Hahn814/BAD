@echo off
 
echo oooooooooo.  oooooooooooo       .o.         .oooooo.     .oooooo.   ooooo      ooo 
echo `888'   `Y8b `888'     `8      .888.       d8P'  `Y8b   d8P'  `Y8b  `888b.     `8' 
echo  888     888  888             .8"888.     888          888      888  8 `88b.    8  
echo  888oooo888'  888oooo8       .8' `888.    888          888      888  8   `88b.  8  
echo  888    `88b  888    "      .88ooo8888.   888          888      888  8     `88b.8  
echo  888    .88P  888       o  .8'     `888.  `88b    ooo  `88b    d88'  8       `888  
echo o888bood8P'  o888ooooood8 o88o     o8888o  `Y8bood8P'   `Y8bood8P'  o8o        `8 

echo.
echo            Development Team:
echo            ..PAUL HAHN	
echo            ..JOHN DEROSA
echo            ..VINCENT VITOLO
echo.

echo Starting Mission Planner Software
start /MIN /D"C:\Program Files (x86)\Mission Planner" MissionPlanner.exe

echo Starting Target Collection Application 
start /MIN /D"C:\Users\Paul\Documents\Visual Studio 2015\Projects\CollectTarget\CollectTarget\bin\Debug" CollectTarget.exe

echo Starting Communication With Intel Edison
start /MIN /D"C:\Users\Paul\BeaconDrone" notify.py

pause
exit

