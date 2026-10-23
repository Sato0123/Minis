## チャット機能の最小構成

- TCP/IPで接続
- A,B側に受取用のスレッドを作りながら、送信用のループも回す。

## 手順
![instraction](https://pub-6da9e73f1c274a3ca06bd422be861599.r2.dev/chat.gif)

1. ターミナルを開いて
```
make run-b
```
2. 別ターミナルを開いて
```
make run-a
```
