import socket

from chat import chat

HOST, PORT = "victim.local", 50007


def client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print("接続:", f"('{HOST}', {PORT})")
        chat.chat(s)


if __name__ == "__main__":
    print("a.py (client)")
    client()
