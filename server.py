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
    ask = connection.recv(1024).decode()
    if not ask:
        print("[CLOSE SERVER]")
        connection.close()
        break
    
    hours = connection.recv(1024).decode()
    print(hours)
    if not hours:
        connection.send(b"Fail")
    else:
        connection.send(b"Pass")