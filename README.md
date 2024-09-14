<h1>Reverse Shell Setup Script with Auto Installation</h1>
<p>This Python script automates the setup for a reverse shell connection between a <strong>Windows</strong> machine and a <strong>Linux</strong> server. It checks for necessary tools (such as ncat for Netcat with SSL support), installs them if missing, configures firewall rules, and then either starts a Netcat listener (on Linux) or establishes a reverse shell connection (on Windows).</p>
<h2><strong>Features</strong></h2>
<pre class='codeblock'•	**Automatic Installation**: The script checks if ncat is installed and attempts to install it if it’s missing.
•	On **Linux**, it uses the appropriate package manager (apt for Ubuntu/Debian or yum for CentOS/RHEL).
•	On **Windows**, it downloads and installs Nmap (which includes ncat) using PowerShell.
•	**Firewall Configuration**: It automatically opens the specified port on both Linux and Windows firewalls.
•	On **Linux**, it uses iptables.
•	On **Windows**, it uses a PowerShell command to configure the firewall.
•	**Platform-Agnostic**: The script works on both **Windows** and **Linux**, and adjusts its behavior based on the platform it’s running on.
•	**Reverse Shell Setup**:
•	**Linux**: Starts a Netcat listener that awaits a connection from a Windows machine.
•	**Windows**: Establishes a reverse shell to the Linux listener using ncat.
</pre>
<p><strong>Prerequisites</strong></p>
<h2><strong>Windows</strong></h2>
<pre class='codeblock'•	**Python**: Install Python from [python.org](https://www.python.org/downloads/). Make sure to check the box “Add Python to PATH” during installation.
•	**Administrator Privileges**: You need admin rights to install software and configure the firewall.
</pre>
<h2>Linux</h2>
<pre class='codeblock'•	**Python**: Most Linux distributions come with Python pre-installed. If not, install it using your package manager (apt for Debian-based or yum for Red Hat-based).
•	**Root Privileges**: You need root access to install software and configure the firewall.
</pre>
<p><strong>Installation &amp; Setup</strong></p>
<pre class='codeblock'1.	**Clone the Repository or Download the Script**:
•	Clone this repository or download the Python script netcat_script.py.
2.	**Run the Script**:
•	**On Windows**: Open Command Prompt as Administrator and navigate to the script location. Run the following command:
</pre>
<blockquote>
<pre class='codeblock'        python netcat_script.py
</pre>
</blockquote>
<ul>
<li><pre class='codeblock'**On Linux**: Open the terminal and navigate to the script location. Run:
</pre>
</li>
</ul>
<blockquote>
<p>sudo python3 netcat_script.py
<strong>Enter Connection Details</strong>:
    •	You will be prompted to provide the <strong>port number</strong> to use for the connection and the <strong>IP address of the Linux machine</strong>.
    •	On Windows, the script will automatically detect your local IP address and configure the firewall for the specified port.
    4.	<strong>Firewall Configuration</strong>:
    •	The script will automatically configure the firewall to allow traffic on the specified port. Ensure that you run the script with appropriate privileges (Administrator on Windows, root on Linux).
    5.	<strong>Connection</strong>:
    •	If running on <strong>Linux</strong>, the script starts a Netcat listener, waiting for a reverse shell connection from the Windows machine.
    •	If running on <strong>Windows</strong>, the script connects to the specified Linux IP address and starts a reverse shell using cmd.exe.</p>
</blockquote>
<h2></h2>
<h2>Example Workflow</h2>
<p>Step 1**: Run the Script on Linux**</p>
<blockquote>
<p>sudo python3 netcat_script.py</p>
</blockquote>
<ul>
<li><p>Enter the port number (e.g., 4444).</p>
<p>•	Enter the IP address of the Linux machine (e.g., 192.168.1.10).
•	The script will configure the firewall and start a Netcat listener.</p>
</li>
</ul>
<p><strong>Step 2: Run the Script on Windows</strong></p>
<blockquote>
<p>python netcat_script.py</p>
</blockquote>
<ul>
<li><p>The script will automatically detect your Windows IP address.</p>
<p>•	It will configure the firewall for the specified port and connect to the Linux listener using a reverse shell.</p>
</li>
</ul>
<h2>Dependencies</h2>
<p>The script will automatically install the following dependencies if they are not already present:</p>
<pre class='codeblock'•	**Linux:**
•	ncat (Netcat with SSL support) via the system’s package manager.
•	iptables (for configuring firewall rules).
•	**Windows:**
•	**Ncat** (included in Nmap).
•	**PowerShell** (for downloading and configuring the firewall).
</pre>
<h2><strong>Script Breakdown</strong></h2>
<pre class='codeblock'•	**check_nc_installed()**: Verifies whether ncat is installed on the system.
•	**install_ncat()**: Installs ncat (using apt/yum on Linux, or downloading Nmap on Windows).
•	**check_firewall()**: Configures the firewall to allow traffic on the specified port (using iptables on Linux or PowerShell on Windows).
•	**get_windows_ip()**: Automatically detects the Windows machine’s IP address.
•	**start_netcat_listener()**: Starts a Netcat listener on Linux.
•	**connect_netcat_reverse_shell()**: Establishes a reverse shell from Windows to the Linux listener.
</pre>
<h2><strong>Security Warning</strong></h2>
<p>This script sets up a reverse shell, which can be used for both legitimate and malicious purposes. Be cautious about where and how you use this script. Only use it in a controlled environment for educational purposes, penetration testing, or system administration where you have permission.</p>
<h1><strong>Troubleshooting</strong></h1>
<pre class='codeblock'•	**Permission Denied**: Ensure you’re running the script with **admin/root privileges**.
•	**Firewall Issues**: Make sure the firewall allows the specified port. If the script fails to configure the firewall, manually open the port using firewall management tools.
•	**Missing Dependencies**: If the script fails to install ncat, try manually installing it:
•	On **Linux**: Install via package manager (apt or yum).
•	On **Windows**: Download Nmap from [Nmap’s official site](https://nmap.org/download.html).
</pre>
<h1><strong>License</strong></h1>
<p>This project is licensed under the MIT License. You are free to use, modify, and distribute this script as you see fit.</p>
<p>Let me know if you’d like any changes!</p>
