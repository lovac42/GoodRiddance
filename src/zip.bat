@echo off
set ZIP=C:\PROGRA~1\7-Zip\7z.exe a -tzip -y -r
set REPO=good_riddance
set VERSION=0.1.0

fsum -r -jm -md5 -d%REPO% * > checksum.md5
move checksum.md5 %REPO%/checksum.md5

quick_manifest.exe "Good Riddance: Inline Media" "%REPO%" >%REPO%/manifest.json

echo %VERSION% >%REPO%/VERSION

cd %REPO%
%ZIP% ../%REPO%_v%VERSION%_Anki21.ankiaddon *
