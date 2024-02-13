import socket

def respone_OK(socket):
    data = socket.recv(1024).decode()
    print(f"[RESPONE] -> {data}")
    if data == "OK [status 200 OK]":
        return True
    return False

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
    
    # Send hours of study
    hours = input("Enter hours of study (0.00 - 12.00): ")
    s.send(hours.encode())
    while not respone_OK(s):
        hours = input("Enter to study hours (0.00 - 12.00) again: ")
        s.send(hours.encode())
    
    # Send score of exam previous
    score = input("Enter score of exam previous (0.00-100.00): ")
    s.send(score.encode())
    while not respone_OK(s):
        hours = input("Enter score of exam previous (0.00-100.00) again: ")
        s.send(hours.encode())
    