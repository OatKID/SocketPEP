import socket

HOST = "localhost"
PORT = 80
ADDR = (HOST, PORT)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(ADDR)
s.listen()

print("waiting for connection...")
connection, client_address = s.accept()
print("Connect already.")
while True:
    data = connection.recv(1024).decode()
    print("[RESPONE] -> %s"%(data))
    if not data:
        connection.close()
        break
    data = data.upper()
    connection.send(data.encode())