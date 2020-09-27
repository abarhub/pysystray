@echo off & setlocal
set batchPath=%~dp0
powershell.exe -file "%batchPath%build_zip.ps1"
