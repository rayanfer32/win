@if (@CodeSection == @Batch) @then

@echo off

rem Use %SendKeys% to send keys to the keyboard buffer
set SendKeys=CScript //nologo //E:JScript "%~F0"

rem Start the other program in the same Window
rem start "" /B cmd

%windir%\system32\rundll32.exe shell32.dll,Control_RunDLL bthprops.cpl
timeout 1
%windir%\system32\rundll32.exe shell32.dll,Control_RunDLL bthprops.cpl
timeout 1
%SendKeys% " "
timeout 1
%SendKeys% "%%{F4}"

rem taskkill /f /IM SystemSettings.exe
goto :EOF


@end


// JScript section

var WshShell = WScript.CreateObject("WScript.Shell");
WshShell.SendKeys(WScript.Arguments(0));
