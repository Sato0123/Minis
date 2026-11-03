# Minis

コンピュータサイエンスやWeb技術の仕組みを、小さく動くコードで手を動かしながら学ぶための学習用リポジトリです。
各ディレクトリが1つの単元になっていて、それぞれの `README.md` に手順や解説があります。

## 質問・要望について

わからないこと、うまく動かないこと、「こういう単元がほしい」といった要望があれば、気軽に [Issue](https://github.com/Sato0123/Minis/issues) に書いてください。

- どの単元の話か（ディレクトリ名）
- やったこと・期待した結果・実際の結果（エラーメッセージがあれば貼ってください）
- 実行環境（OS、Python や Docker のバージョンなど）

を書いてもらえると答えやすいです。

## 単元一覧

| 単元 | 内容 |
| --- | --- |
| [http_servers](./http_servers) | netcat・CGI・SSI・テンプレートエンジンで簡易HTTPサーバを動かし、Webサーバがリクエストにどう応答してきたかの変遷を学ぶ。 |
| [Rendering_Patterns](./Rendering_Patterns) | MPA / SPA × CSR / SSR / SSG の組み合わせごとに、HTMLがどこで・いつ作られるかの違いを比較する。 |
| [chat](./chat) | TCP/IPソケットとスレッドを使った最小構成のチャット。送信ループと受信スレッドを同時に動かす。 |
| [man_in_the_middle](./man_in_the_middle) | DNSポイズニング（`/etc/hosts` で代用）で通信を横取りし、平文チャットが中間者に盗み見られる様子を体験する。 |
| [symmetric_key_cryptography](./symmetric_key_cryptography) | 共通鍵暗号でチャットを暗号化し、中間者に傍受されても内容がわからないことを確かめる。 |
| [mutex_demo](./mutex_demo) | C と pthread で複数スレッドから同じ変数を更新し、競合状態（race condition）と mutex による排他制御を確認する。 |
| [yaml](./yaml) | Python で YAML ファイルを読み込み、中身をパースして表示する。 |
| [algo](./algo) | データ構造・ソート・リスト探索・グラフ探索（ベルマン–フォード法など）のアルゴリズム。※作成中 |

おすすめの順番: `chat` → `man_in_the_middle` → `symmetric_key_cryptography` は、同じチャットを題材に「通信 → 盗聴 → 暗号化」と続く流れになっています。
