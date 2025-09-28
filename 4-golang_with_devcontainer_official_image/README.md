Go言語で、DevContainer公式イメージをベースにした環境構築例

- Dockerfileにて、DevContainer公式イメージを指定
- Dockerfileにて、バージョンを固定したいツールのインストール
- docker-compose.yamlに、キャッシュをコンテナ外に置く設定を追加
- postCreateCommandにて、go getでプロジェクト依存ファイルをインストール
