import socket

# 서버 주소 및 포트 설정
SERVER_IP = 'localhost'
SERVER_PORT = 9999

# UDP 소켓 생성
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    msg = input('Enter the message("send mboxId message" or "receive mboxId"): ').strip()
    client_socket.sendto(msg.encode(), (SERVER_IP, SERVER_PORT))
    
    if msg.lower() == "quit" or msg.lower() == "q":
        print("클라이언트 종료")
        break

    # 응답 수신
    data, _ = client_socket.recvfrom(1024)
    print("서버 응답:", data.decode())

client_socket.close()
