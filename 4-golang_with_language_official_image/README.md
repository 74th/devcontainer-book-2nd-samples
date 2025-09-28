Go言語で、DockerHubの言語公式イメージをベースにした環境構築例

- Dockerfileにて、DockerHub上のGo言語公式イメージを指定
- Dockerfileにて、各種ツールのインストール
- DevContainer Featuresで、core-utilsを使って非rootユーザの作成
- docker-compose.yamlに、キャッシュをコンテナ外に置く設定を追加
- postCreateCommandにて、go getでプロジェクト依存ファイルをインストール
