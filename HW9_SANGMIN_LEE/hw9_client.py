import socket
import threading

HOST = '127.0.0.1'
PORT = 1234

def receive(sock):
    while True:
        try:
            msg = sock.recv(1024).decode()
            if msg:
                print(msg)
        except:
            print("서버와 연결이 끊겼습니다.")
            break

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

user_id = input("ID를 입력하세요: ")
client_socket.sendall(user_id.encode())

recv_thread = threading.Thread(target=receive, args=(client_socket,))
recv_thread.daemon = True
recv_thread.start()

while True:
    try:
        msg = input()
        if msg.lower() == 'quit':
            client_socket.sendall('quit'.encode())
            break
        client_socket.sendall(msg.encode())
    except:
        break

client_socket.close()
