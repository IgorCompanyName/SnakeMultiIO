import socket

HOST = "127.0.0.1"
PORT = 8080

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as stream:
    stream.connect((HOST, PORT))
    stream.sendall(b"Hello, world!")
    data = stream.recv(2048)

print(f"Received {data!r}")