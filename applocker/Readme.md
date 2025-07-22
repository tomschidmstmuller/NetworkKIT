## AppLocker - Notes

#### Detect bypasses

- A more effective executable, such as a simple infinite loop binary, should be used instead of something like calc.exe, which may only remain active in the background for a short time. This will provide your script with sufficient time to detect the process in the task list and log it accordingly.

```
@echo off
 
C:
cd C:\TEMP\
 

echo Creating a cursive list of all directories and sub-directories of the selected folder e.g. c:\
dir C:\ /s /b /o:n /a:d > C:\TEMP\dirs.txt
 

echo Attempting to copy calc.exe to all folders (write permission check)
for /F "tokens=*" %%A in (dirs.txt) do copy "C:\Windows\System32\calc.exe" "%%A" /Y
 
echo Attempting to execute calc.exe (execution permission check)
for /F "tokens=*" %%A in (dirs.txt) do if exist "%%A\calc.exe" icacls "%%A\calc.exe" /grant %USERNAME%:f & start "" "%%A\calc.exe" && tasklist /v | findstr "calc.exe" > executed.txt && for %%B in (executed.txt) do if not %%~zB==0 echo %%A >> bypasses.txt && taskkill /IM calc.exe /F && del /F executed.txt
 
echo Deleting calc.exe from all locations
for /F "tokens=*" %%A in (dirs.txt) do del /F "%%A\calc.exe"
 
echo Done
```

---
