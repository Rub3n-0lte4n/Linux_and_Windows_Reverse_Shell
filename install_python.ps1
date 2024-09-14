# Define the URL for the latest Python 3 installer
$pythonUrl = "https://www.python.org/ftp/python/3.12.1/python-3.12.1-amd64.exe"

# Define the path to download the installer
$installerPath = "$env:TEMP\python-installer.exe"

# Download the Python installer
Invoke-WebRequest -Uri $pythonUrl -OutFile $installerPath

# Run the installer silently with default options
Start-Process -FilePath $installerPath -ArgumentList "/quiet InstallAllUsers=1 PrependPath=1" -Wait

# Remove the installer after installation
Remove-Item -Path $installerPath

# Verify the installation
python --version