import socket
import time

def log_data(device_name, data):
    timestamp = time.ctime()
    line = f"{timestamp}: {device_name}: {data}\n"
    with open("data.txt", "a") as f:
        f.write(line)
    print("[Saved]", line.strip())

def main():
    dev1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    dev2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    dev1.connect(('localhost', 9001))
    dev2.connect(('localhost', 9002))

    print("=== IoT Client Started ===")
    print("Enter '1' (Device1), '2' (Device2), or 'quit' to exit.")

    while True:
        cmd = input(">> ").strip()
        if cmd == '1':
            dev1.sendall(b"Request")
            data = dev1.recv(1024).decode()
            log_data("Device1", data)
        elif cmd == '2':
            dev2.sendall(b"Request")
            data = dev2.recv(1024).decode()
            log_data("Device2", data)
        elif cmd == 'quit':
            dev1.sendall(b"quit")
            dev2.sendall(b"quit")
            print("[User] Shutting down.")
            break
        else:
            print("Invalid input. Use '1', '2', or 'quit'.")

    dev1.close()
    dev2.close()

if __name__ == "__main__":
    main()
