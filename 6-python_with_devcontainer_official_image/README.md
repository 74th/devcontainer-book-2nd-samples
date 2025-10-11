Pythonで、DockerHubの言語公式イメージをベースにした環境構築例

- Dockerfileにて、DockerHub上のPython言語公式イメージを指定
- DevContainer Featuresで、core-utilsを使って非rootユーザの作成
- docker-compose.yamlに、キャッシュをコンテナ外に置く設定を追加
- postCreateCommandにて、uv syncでプロジェクト依存ファイルをインストール
