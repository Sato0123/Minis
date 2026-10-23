import threading

from cipher import decrypt, encrypt


def receive_loop(sock):
    while True:
        data = sock.recv(1024)
        if not data:
            print("相手が切断しました")
            break
        print(decrypt(data))


def chat(sock):
    threading.Thread(target=receive_loop, args=(sock,), daemon=True).start()
    while True:
        msg = input()
        if msg == "exit":
            break
        encrypted = encrypt(msg)
        sock.sendall(encrypted)
