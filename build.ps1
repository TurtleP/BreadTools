Write-Host "Building Bread Tools.."

$watch = [System.Diagnostics.Stopwatch]::StartNew()

Remove-Item -ErrorAction Ignore .\BreadTools.zip

pyinstaller.exe --clean --log-level="ERROR" .\main.spec

Remove-Item -Recurse .\build
Compress-Archive -Path .\dist\main\* -DestinationPath .\BreadTools.zip
Remove-Item -Recurse .\dist

$watch.Stop()

Write-Host "Done in" $watch.Elapsed.TotalSeconds "seconds."
