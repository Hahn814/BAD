@echo off

echo.
echo BEACON AUTONOMOUS DRONE
echo CALIFORNIA UNIVERISTY OF PA
echo PAUL HAHN	
echo JOHN DEROSA
echo VINCENT VITOLO
echo.

echo Starting Mission Planner Software
start /MIN /D"C:\Program Files (x86)\Mission Planner" MissionPlanner.exe

echo Starting Target Collection Application 
start /MIN /D"C:\Users\Paul\Documents\Visual Studio 2015\Projects\CollectTarget\CollectTarget\bin\Debug" CollectTarget.exe

pause
exit

