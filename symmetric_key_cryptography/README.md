## 共通鍵暗号方式

### チャット機能の最小構成

- TCP/IPで接続
- A,B側に受取用のスレッドを作りながら、送信用のループも回す。
- 共通鍵暗号を使って中間者に傍受されたとしても何を通信しているかわからないようにする。

## 手順
![instraction](https://pub-6da9e73f1c274a3ca06bd422be861599.r2.dev/symmetric_key_cryptography.gif)

## 事前準備
```
make host
make poison
```

