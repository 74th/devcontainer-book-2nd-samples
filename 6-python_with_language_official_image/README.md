Pythonで、DevContainer公式イメージをベースにした環境構築例

- Dockerfileにて、DevContainer公式イメージを指定
- compose.ymlに、キャッシュをコンテナ外に置く設定を追加
- postCreateCommandにて、uv syncでプロジェクト依存ファイルをインストール
