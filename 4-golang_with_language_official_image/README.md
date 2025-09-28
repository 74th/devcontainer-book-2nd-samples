Go言語で、DockerHubの言語公式イメージをベースにした環境構築例

- Dockerfileにて、DockerHub上のGo言語公式イメージを指定
- Dockerfileにて、非rootユーザの作成
- Dockerfileにて、各種ツールのインストール
- docker-compose.yamlに、キャッシュをコンテナ外に置く設定を追加
- postCreateCommandにて、go getでプロジェクト依存ファイルをインストール
