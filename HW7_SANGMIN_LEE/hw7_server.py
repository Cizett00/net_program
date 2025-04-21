import socket

# 메시지를 저장할 딕셔너리
mailboxes = {}

# 서버 주소 및 포트 설정
SERVER_IP = 'localhost'
SERVER_PORT = 9999

# UDP 소켓 생성 및 바인딩
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((SERVER_IP, SERVER_PORT))

print(f"UDP 서버가 {SERVER_IP}:{SERVER_PORT}에서 실행 중...")

while True:
    try:
        data, addr = server_socket.recvfrom(1024)
        message = data.decode().strip()
        print(f"수신: {message} (from {addr})")

        # 종료 명령 처리
        if message.lower() == "quit" or message.lower() == "q":
            print("서버 종료 명령 수신. 종료합니다.")
            break

        # send mboxId message 처리
        elif message.startswith("send "):
            parts = message.split(" ", 2)
            if len(parts) < 3:
                server_socket.sendto("Invalid send command".encode(), addr)
                continue
            mbox_id = parts[1]
            msg_content = parts[2]

            if mbox_id not in mailboxes:
                mailboxes[mbox_id] = []
            mailboxes[mbox_id].append(msg_content)
            server_socket.sendto("OK".encode(), addr)

        # receive mboxId 처리
        elif message.startswith("receive ")
            parts = message.split(" ", 1)
            if len(parts) < 2:
                server_socket.sendto("Invalid receive command".encode(), addr)
                continue
            mbox_id = parts[1]

            if mbox_id in mailboxes and mailboxes[mbox_id]:
                msg_to_send = mailboxes[mbox_id].pop(0)
                server_socket.sendto(msg_to_send.encode(), addr)
            else:
                server_socket.sendto("No messages".encode(), addr)

        else:
            server_socket.sendto("Unknown command".encode(), addr)

    except Exception as e:
        print(f"[오류] {e}")
        break

server_socket.close()
print("서버 소켓 종료")
