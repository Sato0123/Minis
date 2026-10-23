import socket

from chat import chat_encrypt

HOST, PORT = "127.0.0.2", 50007


def server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        print("接続:", addr)
        with conn:
            chat_encrypt.chat(conn)


if __name__ == "__main__":
    print("b.py (server)")
    server()
