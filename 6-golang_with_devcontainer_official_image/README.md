Go言語で、DevContainer公式イメージをベースにした環境構築例

- Dockerfileにて、DevContainer公式イメージを指定
- compose.ymlに、キャッシュをコンテナ外に置く設定を追加
- initializeCommandにて、コンテナ外キャッシュのディレクトリ作成
- postCreateCommandにて、go installで必要なツールをインストール
- postCreateCommandにて、go getでプロジェクト依存ファイルをインストール
