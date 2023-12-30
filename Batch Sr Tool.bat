@echo off
SETLOCAL ENABLEDELAYEDEXPANSION
SET "sourceDir=E:\Motorcycle tools\Sigrok\Wheel speed"
SET "outputFile=%sourceDir%\Sorted.txt"

REM del "%outputFile%"

for /L %%i in (1,1,100) do (
    SET "filename=%%i.sr"
    SET "inputFile=!sourceDir!\!filename!"
    IF EXIST "!inputFile!" (
        echo Processing file: !filename!
        echo. >> "%outputFile%"
        echo. >> "%outputFile%"
        echo !filename! >> "%outputFile%"
        echo. >> "%outputFile%"
        "C:\Program Files\sigrok\sigrok-cli\sigrok-cli.exe" -i "!inputFile!" -P uart:rx=D0:baudrate=16040 >> "%outputFile%"
        echo. >> "%outputFile%"
        echo. >> "%outputFile%"
    )
)

echo Done.
ENDLOCAL