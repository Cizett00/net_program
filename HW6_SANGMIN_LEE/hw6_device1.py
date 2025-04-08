import socket
import random

HOST = 'localhost'
PORT = 9001

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)
    print(f"[Device1] Listening on {HOST}:{PORT}")

    conn, addr = server_socket.accept()
    with conn:
        print(f"[Device1] Connected by {addr}")
        while True:
            data = conn.recv(1024).decode()
            if data == 'Request':
                temp = random.randint(0, 40)
                humid = random.randint(0, 100)
                illum = random.randint(70, 150)
                response = f"Temp={temp}, Humid={humid}, Illum={illum}"
                conn.sendall(response.encode())
            elif data == 'quit':
                print("[Device1] Quit signal received. Shutting down.")
                break
