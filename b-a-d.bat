@echo off
 
echo  ______     ______     ______     ______     ______     __   __    
echo /\  == \   /\  ___\   /\  __ \   /\  ___\   /\  __ \   /\ "-.\ \   
echo \ \  __^<   \ \  __\   \ \  __ \  \ \ \____  \ \ \/\ \  \ \ \-.  \  
echo  \ \_____\  \ \_____\  \ \_\ \_\  \ \_____\  \ \_____\  \ \_\\"\_\ 
echo   \/_____/   \/_____/   \/_/\/_/   \/_____/   \/_____/   \/_/ \/_/ 
echo.  
echo  ______     __  __     ______   ______    
echo /\  __ \   /\ \/\ \   /\__  _\ /\  __ \   
echo \ \  __ \  \ \ \_\ \  \/_/\ \/ \ \ \/\ \  
echo  \ \_\ \_\  \ \_____\    \ \_\  \ \_____\ 
echo   \/_/\/_/   \/_____/     \/_/   \/_____/ 
echo.  
echo  _____     ______     ______     __   __     ______    
echo /\  __-.  /\  == \   /\  __ \   /\ "-.\ \   /\  ___\   
echo \ \ \/\ \ \ \  __^<   \ \ \/\ \  \ \ \-.  \  \ \  __\   
echo  \ \____-  \ \_\ \_\  \ \_____\  \ \_\\"\_\  \ \_____\ 
echo   \/____/   \/_/ /_/   \/_____/   \/_/ \/_/   \/_____/ 

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

pause
exit

