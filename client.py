import socket

def receive_file(output_filename, host='127.0.0.1', port=65432):
    # Create TCP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    # Receive file data and write to output file
    with open(output_filename, 'wb') as f:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            f.write(data)

    print("File received successfully.")
    client_socket.close()

if __name__ == "__main__":
    receive_file("received_sample.txt")   # File will be saved here