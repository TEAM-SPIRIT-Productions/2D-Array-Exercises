:: This script allows the user to launch the tests without needing use command line
@ECHO off
echo "This script will start check if the function you coded in exercise.py is correct."
echo "Starting up virtual environment..."
call ..\venv\scripts\activate.bat
echo "Start unit tests..."
py.test exercise_test.py
echo "Test concluded."
pause