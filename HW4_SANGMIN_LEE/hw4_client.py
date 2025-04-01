from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 3333))

while True:
    msg = input('input calculation formula: ').strip()
    if msg == 'q' or msg == 'quit':
        break

    s.send(msg.encode())

    print('Received message:', s.recv(1024).decode())

s.close()