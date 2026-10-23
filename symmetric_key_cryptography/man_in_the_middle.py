import socket
import threading

# a.py -> b.py のつもりが
# a.py -> man_in_the_middle.py -> b.py になる
LISTEN_HOST, LISTEN_PORT = "127.0.0.1", 50007  # a.py (client side)
TARGET_HOST, TARGET_PORT = "127.0.0.2", 50007  # b.py (server side)


def forward(src, dst, label):
    while True:
        data = src.recv(4096)
        if not data:
            break
        try:
            string: str = bytes.decode(data, "utf-8")
        except UnicodeDecodeError:
            print("data isn't UTF-8!?? I can't read this!!")
            string = data
        print(f"get secret message![{label}] {string!r}")
        dst.sendall(data)
    src.close()
    dst.close()


def man_in_the_middle():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as listener:
        listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        listener.bind((LISTEN_HOST, LISTEN_PORT))
        listener.listen()
        print("中間者 待ち受け中...")
        while True:
            client, addr = listener.accept()
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.connect((TARGET_HOST, TARGET_PORT))
            print("接続を中継:", addr)
            # 両方向を別スレッドで中継
            threading.Thread(
                target=forward, args=(client, server, "C→S"), daemon=True
            ).start()
            threading.Thread(
                target=forward, args=(server, client, "S→C"), daemon=True
            ).start()


if __name__ == "__main__":
    man_in_the_middle()
