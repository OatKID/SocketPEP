import socket

HOST = "localhost"
PORT = 1200
ADDR = (HOST, PORT)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(ADDR)

while True:
    ask = input("Do you want to predict about exam performance of student ? (Yes/No): ")
    if ask == "No":
        print("[ClOSE CLIENT]")
        s.close()
        break
    s.send(ask.encode())
    
    hours = input("Enter to study hours (0.00 - 12.00): ")
    s.send(hours.encode())
    
    data = s.recv(1024).decode()
    print(data)