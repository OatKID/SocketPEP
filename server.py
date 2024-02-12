import socket
from Ai import StudentExamPerformance

classification = StudentExamPerformance()

HOST = "localhost"
PORT = 1200
ADDR = (HOST, PORT)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(ADDR)
s.listen()

print("waiting for connection...")
connection, client_address = s.accept()
print("Connect already.")
while True:
    data = connection.recv(1024).decode()
    if not data:
        print("[CLOSE SERVER]")
        connection.close()
        break
    print("[GET] -> %s"%(data))
    data = data.upper()
    print(f"[RESPONE] -> {data}")
    connection.send(data.encode())