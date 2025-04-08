import socket
import random

HOST = 'localhost'
PORT = 9002

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)
    print(f"[Device2] Listening on {HOST}:{PORT}")

    conn, addr = server_socket.accept()
    with conn:
        print(f"[Device2] Connected by {addr}")
        while True:
            data = conn.recv(1024).decode()
            if data == 'Request':
                heartbeat = random.randint(40, 140)
                steps = random.randint(2000, 6000)
                cal = random.randint(1000, 4000)
                response = f"Heartbeat={heartbeat}, Steps={steps}, Cal={cal}"
                conn.sendall(response.encode())
            elif data == 'quit':
                print("[Device2] Quit signal received. Shutting down.")
                break
