import socket
HOST="0.0.0.0"   
PORT=5001
BUFFER_SIZE=4096
server=socket.socket()
server.bind((HOST, PORT))
server.listen(1)
print("Server listening on port", PORT)
conn, addr=server.accept()
print("Connected from", addr)
filename=conn.recv(BUFFER_SIZE).decode()
print("Receiving file:", filename)
with open("received_" + filename, "wb") as file:
    while True:
        data=conn.recv(BUFFER_SIZE)
        if not data:
            break
        file.write(data)
print("File received successfully.")
conn.close()
server.close()