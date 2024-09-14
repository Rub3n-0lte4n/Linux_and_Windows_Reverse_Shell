# Reverse Shell Setup Script with Auto Installation

This Python script automates the setup for a reverse shell connection between a **Windows** machine and a **Linux** server. It checks for necessary tools (such as `ncat` for Netcat with SSL support), installs them if missing, configures firewall rules, and then either starts a Netcat listener (on Linux) or establishes a reverse shell connection (on Windows).

## Features

- **Automatic Installation**: The script checks if `ncat` is installed and attempts to install it if it's missing.
  - On **Linux**, it uses the appropriate package manager (`apt` for Ubuntu/Debian or `yum` for CentOS/RHEL).
  - On **Windows**, it downloads and installs Nmap (which includes `ncat`) using PowerShell.
  
- **Firewall Configuration**: It automatically opens the specified port on both Linux and Windows firewalls.
  - On **Linux**, it uses `iptables`.
  - On **Windows**, it uses a PowerShell command to configure the firewall.

- **Platform-Agnostic**: The script works on both **Windows** and **Linux**, and adjusts its behavior based on the platform it’s running on.

- **Reverse Shell Setup**:
  - **Linux**: Starts a Netcat listener that awaits a connection from a Windows machine.
  - **Windows**: Establishes a reverse shell to the Linux listener using `ncat`.

## Prerequisites

### Windows
- **Python**: Install Python from [python.org](https://www.python.org/downloads/). Make sure to check the box "Add Python to PATH" during installation.
- **Administrator Privileges**: You need admin rights to install software and configure the firewall.

### Linux
- **Python**: Most Linux distributions come with Python pre-installed. If not, install it using your package manager (`apt` for Debian-based or `yum` for Red Hat-based).
- **Root Privileges**: You need root access to install software and configure the firewall.

## Installation & Setup

1. **Clone the Repository or Download the Script**:
   - Clone this repository or download the Python script `netcat_script.py`.

2. **Run the Script**:
   - **On Windows**: Open Command Prompt as Administrator and navigate to the script location. Run the following command:
     ```bash
     python netcat_script.py
     ```
   - **On Linux**: Open the terminal and navigate to the script location. Run:
     ```bash
     sudo python3 netcat_script.py
     ```

3. **Enter Connection Details**:
   - You will be prompted to provide the **port number** to use for the connection and the **IP address of the Linux machine**.
   - On Windows, the script will automatically detect your local IP address and configure the firewall for the specified port.

4. **Firewall Configuration**:
   - The script will automatically configure the firewall to allow traffic on the specified port. Ensure that you run the script with appropriate privileges (Administrator on Windows, root on Linux).

5. **Connection**:
   - If running on **Linux**, the script starts a Netcat listener, waiting for a reverse shell connection from the Windows machine.
   - If running on **Windows**, the script connects to the specified Linux IP address and starts a reverse shell using `cmd.exe`.

## Example Workflow

### Step 1: Run the Script on Linux
```bash
sudo python3 netcat_script.py
    
- Enter the port number (e.g., 4444).
- Enter the IP address of the Linux machine (e.g., 192.168.1.10).
- The script will configure the firewall and start a Netcat listener.
