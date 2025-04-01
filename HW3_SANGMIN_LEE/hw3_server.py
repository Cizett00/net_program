import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('',9000))
s.listen(2)

while True:
    client, addr = s.accept()
    print('Connection from ', addr)
    client.send(b'Hello ' + addr[0].encode())

    #이름수신
    name = client.recv(1024).decode()
    print("Received name:", name)

    #학번전송
    student_id = 20201528
    student_id_big = student_id.to_bytes(4, 'big')#빅엔디안변경경
    client.send(student_id_big)

    client.close()