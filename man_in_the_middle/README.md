## man_in_the_middle

- chat
  - TCP/IPで接続
  - A,B側に受取用のスレッドを作りながら、送信用のループも回す。
- DNSポイズニング(今回は/etc/hostsで代用)

![instraction](https://pub-6da9e73f1c274a3ca06bd422be861599.r2.dev/man_in_the_middle.gif)

## 手順

1. 初期化
```
make host
```

## Not Poisning

1. ターミナルを開いて
```
make run-b
```
2. 別ターミナルを開いて
```
make run-a
```

## Poisning
---

1. ポイズニング
```
make poison
```
2. サーバ起動
```
make run-b
```
3. 中間者起動
```
make run-m
```
4. クライアントを繋ぐ
```
make run-a
```
