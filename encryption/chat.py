import socket
import threading


def receive_loop(sock):
    while True:
        data = sock.recv(1024)
        if not data:
            print("相手が切断しました")
            break
        print(data.decode())


def chat(sock):
    threading.Thread(target=receive_loop, args=(sock,), daemon=True).start()
    while True:
        msg = input()
        if msg == "exit":
            break
        sock.sendall(msg.encode())


HOST, PORT = "127.0.0.1", 50007


def server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        print("接続:", addr)
        with conn:
            chat(conn)


def client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print("接続:", f"('{HOST}', {PORT})")
        chat(s)
