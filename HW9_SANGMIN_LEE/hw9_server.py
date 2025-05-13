import socket
import select

HOST = '0.0.0.0'
PORT = 1234

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

print(f"서버 시작됨: {HOST}:{PORT}")
socket_list = [server_socket]
clients = {}

def broadcast(msg, exclude_socket=None):
    for sock in clients:
        if sock != exclude_socket:
            try:
                sock.sendall(msg.encode())
            except:
                sock.close()
                socket_list.remove(sock)
                del clients[sock]

while True:
    read_sockets, _, exception_sockets = select.select(socket_list, [], socket_list)

    for sock in read_sockets:
        if sock == server_socket:
            client_socket, client_addr = server_socket.accept()
            socket_list.append(client_socket)
            print(f"새 클라이언트 접속: {client_addr}")
        else:
            try:
                data = sock.recv(1024).decode()
                if not data:
                    raise ConnectionResetError()

                if sock not in clients:
                    clients[sock] = data.strip()
                    broadcast(f"[알림] {clients[sock]} 님이 입장하였습니다.", sock)
                elif data.strip().lower() == 'quit':
                    broadcast(f"[알림] {clients[sock]} 님이 퇴장하였습니다.", sock)
                    print(f"{clients[sock]} 접속 종료")
                    socket_list.remove(sock)
                    del clients[sock]
                    sock.close()
                else:
                    msg = f"[{clients[sock]}] {data}"
                    print(msg.strip())
                    broadcast(msg, sock)
            except:
                if sock in clients:
                    print(f"{clients[sock]} 연결 끊김")
                    broadcast(f"[알림] {clients[sock]} 님 연결 끊김", sock)
                    del clients[sock]
                socket_list.remove(sock)
                sock.close()

    for sock in exception_sockets:
        socket_list.remove(sock)
        if sock in clients:
            del clients[sock]
        sock.close()
