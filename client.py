import socket

HOST = "localhost"
PORT = 80
ADDR = (HOST, PORT)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(ADDR)

while True:
    text = input("Enter lowercase: ")
    if text == "exit":
        s.close()
        break
    s.send(text.encode())
    data = s.recv(1024)
    print(data.decode())