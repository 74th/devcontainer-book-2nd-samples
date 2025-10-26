Go言語で、DevContainer公式のFeatureを利用した開発環境構築

- Dockerfileにて、DevContainer公式のベースイメージを指定
- devcontainer.jsonにて、Go言語Featureを追加
- compose.ymlに、キャッシュをコンテナ外に置く設定を追加
- initializeCommandにて、コンテナ外キャッシュのディレクトリ作成
- postCreateCommandにて、go installで必要なツールをインストール
- postCreateCommandにて、go getでプロジェクト依存ファイルをインストール
