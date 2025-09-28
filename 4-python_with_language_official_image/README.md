Pythonで、DevContainer公式イメージをベースにした環境構築例

- Dockerfileにて、DevContainer公式イメージを指定
- docker-compose.yamlに、キャッシュをコンテナ外に置く設定を追加
- postCreateCommandにて、uv syncでプロジェクト依存ファイルをインストール
