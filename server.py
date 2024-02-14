import socket
from Ai import StudentExamPerformance

def get_data_float(connection, from_number, to_number, text):
    while True:
        data = connection.recv(1024).decode()
        
        try:
            data = float(data)
            if data < from_number or data > to_number:
                print(f"[RESPONE {text}] -> Data is not range that is set. [status 112 range out]")
                connection.send(b"Data is not range that is set. [status 112 range out]")
                continue
        except:
            print(f"[RESPONE {text}] -> Data must be float.!! [status 111 type error]")
            connection.send(b"Data must be float.!! [status 111 type error]")
            continue
        print(f"[GET {text}] -> {data}")
        connection.send(b"OK [status 200 OK]")
        return data

classification = StudentExamPerformance()

HOST = "localhost"
PORT = 1200
ADDR = (HOST, PORT)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(ADDR)
s.listen()

print("waiting for connection from client...")
connection, client_address = s.accept()
print(f"Connect already at {client_address}")
while True:
    ask = connection.recv(1024).decode()
    if not ask:
        print("[CLOSE SERVER]")
        connection.close()
        break
    
    # Recives data from client such as hours and scores
    hours = get_data_float(connection, 0.00, 12.00, "hours")
    scores = get_data_float(connection, 0.00, 100.00, "scores")
    
    result = classification.predict(hours, scores)
    
    result = f"Predict of student exam: {result}"
    print(f"[RESPONE] -> Predict Complete -> \"{result}\" [status 210 OK Predict]")
    connection.send(f"Predict Complete -> \"{result}\" [status 210 OK Predict]".encode())