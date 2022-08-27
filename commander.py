import socket


HOST = "127.0.0.1" # Remote host
PORT = 8081 # Remote port


server = socket.socket()
server.bind((HOST , PORT))
print ("[+] Server Starting")
print("[+] Listening on %s:%d" % (HOST, PORT))
server.listen(1)
client , addr = server.accept()
print(f"[+] Connected to {addr}")

while True:
    command = input("Shell> ")
    command = command.encode
    client.send(command)
    print("[+] Command Sent")
    output = client.recv(1024)
    print(output.decode())
    if "exit" in command:
        break
    client.close()
    print(f"Output: {output}")
    if command == "quit":
        client.close()
        server.close()
        exit()
    
        