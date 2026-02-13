import socket

def send_file(filename, host='127.0.0.1', port=65432):
    # Create TCP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Server listening on {host}:{port}")

    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")

    # Open file and send in chunks
    with open(filename, 'rb') as f:
        data = f.read(1024)
        while data:
            conn.send(data)
            data = f.read(1024)

    print("File transfer complete.")
    conn.close()
    server_socket.close()

if __name__ == "__main__":
    send_file("sample.txt")   # Replace with the file you want to send