# example_http_servers

## アーキテクチャ一覧

- **NetCat Server**
    - netcatコマンドを使った簡易サーバ。
    - listenなどの基本を確認できる。

- **CGI (Common Gateway Interface)**

    - httpリクエストに対してスクリプトを実行し、標準出力としてそのまま返す。
    - クエリパラメータは環境変数から読み込む。

- **SSI** (Server Side Includes)
    - インクルードディレクティブと呼ばれる命令をHTMLに埋め込む。
    - テンプレートエンジンの祖先。

- **Template Engine**
    - テンプレートを用意しスクリプトで動的にコンテンツを生成する。

## 動作確認

### 起動

対象アーキテクチャのディレクトリに移動してcompose up
```
cd cgi
docker compose up -d
```

### 出力確認

```
curl -i localhost:80
```

### 停止

```
docker compose down
```
