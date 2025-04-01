import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

addr = ('localhost', 9000)
sock.connect(addr)
msg = sock.recv(1024)
print(msg.decode())

#이름전송
name = "LEE SANGMIN"
sock.send(name.encode())

#학번수신
data = sock.recv(4) 

student_id = int.from_bytes(data, 'big')  

converted_id = int.from_bytes(student_id.to_bytes(4, 'little'), 'little')#리틀엔디안으로해석

print("수신한 학번 (리틀 엔디언):", converted_id)


sock.close()