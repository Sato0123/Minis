from Crypto.Cipher import AES

key = b"0123456789012346"
iv = b" " * 16
assert len(key) == 16
assert len(iv) == 16


def encrypt(text: str):
    cipher = AES.new(key, AES.MODE_CBC, IV=iv)
    data = text.encode("utf-8")
    pad_len = 16 - (len(data) % 16)
    data += bytes([pad_len]) * pad_len

    return cipher.encrypt(data)


def decrypt(encrypted: bytes):
    cipher = AES.new(key, AES.MODE_CBC, IV=iv)
    data = cipher.decrypt(encrypted)
    pad_len = data[-1]
    data = data[:-pad_len]
    return data.decode("utf-8")
