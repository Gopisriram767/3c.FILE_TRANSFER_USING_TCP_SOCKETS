import socket
import os
SERVER_IP="127.0.0.1" 
PORT=5001
BUFFER_SIZE=4096
filename=input("Enter file name to send: ")
if not os.path.exists(filename):
    print("File not found!")
    exit()
client=socket.socket()
client.connect((SERVER_IP, PORT))
client.send(filename.encode())
with open(filename, "rb") as file:
    while True:
        data=file.read(BUFFER_SIZE)
        if not data:
            break
        client.send(data)
print("File sent successfully.")
client.close()