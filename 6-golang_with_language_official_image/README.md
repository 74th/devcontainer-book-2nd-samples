Go言語で、DockerHubの言語公式イメージをベースにした環境構築例

- Dockerfileにて、DockerHub上のGo言語公式イメージを指定
- DevContainer Featuresで、core-utilsを使って非rootユーザの作成
- docker-compose.yamlに、キャッシュをコンテナ外に置く設定を追加
- initializeCommandにて、コンテナ外キャッシュのディレクトリ作成
- postCreateCommandにて、go installで必要なツールをインストール
- postCreateCommandにて、go getでプロジェクト依存ファイルをインストール
