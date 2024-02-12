import socket

HOST = "localhost"
PORT = 1200
ADDR = (HOST, PORT)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(ADDR)

while True:
    text = input("Enter lowercase: ")
    if text == "exit":
        print("[ClOSE CLIENT]")
        s.close()
        break
    s.send(text.encode())
    data = s.recv(1024)
    print(data.decode())