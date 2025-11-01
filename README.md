# 同人誌『DevContainer実践ガイド』サンプルコード

<img src="./material/ebook.png" alt="DevContainer実践ガイド表紙" width="600"/>

このリポジトリは技術書典19にては [@74th](https://github.com/74th) が頒布した同人誌『DevContainer実践ガイド』のサンプルコードを収録しています。

販売先: Booth https://74th.booth.pm/items/7605652

## 本リポジトリの内容

### 本紙掲載

- 4. DevContainerの細かい使い方
  - [4.2-C2-add_non_root_user](4.2-C2-add_non_root_user): 非rootユーザを利用する。Dockerfileでの設定例。
  - [4.2-C3-add_non_root_user](4.2-C3-add_non_root_user): 非rootユーザを利用する。DevContainer Features common-utilsを利用した設定例。
  - [4.5-secret_from_env](4.5-secret_from_env): シークレットの持ち込み方。envfileから、コンテナの環境変数に渡す。
  - [4.5-secret_from_mount](4.5-secret_from_mount): シークレットの持ち込み方。ディレクトリマウントで渡す。
  - [4.5-secret_from_compose_secrets](4.5-secret_from_compose_secrets): シークレットの持ち込み方。Docker ComposeのSecretマウントを利用する。
  - [4.7-git_config_from_dotfiles](4.7-git_config_from_dotfiles): dotfilesの利用
  - [4.8-override_settings](4.8-override_settings): 個人の設定を使う
- 5. DevContainer Features
  - [5.3-docker_in_docker](5.3-docker_in_docker): Docker in Dockerの設定例
- 6. DevContainer構築例
  - [6.1-golang_with_language_official_image](6.1-golang_with_language_official_image): Go。DockerHubのGo言語公式イメージを利用。
  - [6.2-python_with_devcontainer_official_image](6.2-python_with_devcontainer_official_image): Python。DevContainer公式イメージを利用。
  - [6.3-append_nodejs](6.3-append_nodejs): Node.js。DevContainer Featuresを利用
  - [6.4-with_redis](6.4-with_redis): Redis
  - [6.4-with_mysql](6.4-with_mysql): MySQL
  - [6.4-with_postgresql](6.4-with_postgresql): PostgreSQL
- 7. ネットワーク隔離環境
  - [7.3-normal](7.3-normal): ネットワーク共有したDocker Compose構成（比較用）
  - [7.3-network_dedicated_container](7.3-network_dedicated_container): Docker Composeでネットワークを作り、ホストと分離する
  - [7.4-firewall_by_iptables](7.4-firewall_by_iptables): composeでネットワークを作り、ホストと分離する。方法1、iptablesでFirewallを構築しIPで制限する
  - [7.4-http_proxy](7.4-http_proxy): composeでネットワークを作り、ホストと分離する。方法2、HTTPプロキシでドメインで制限する
- 8. ローカルでのLLMコーディングエージェントでのDevContainerの利用
  - [8.2-claudecode](8.2-claudecode): Claude Code
  - [8.2-claudecode_with_bedrock](8.2-claudecode_with_bedrock): Calude Code。AWS Bedrock認証情報の渡し方。
  - [8.2-claudecode_with_vertexai](8.2-claudecode_with_vertexai): Claude Code。Google Vertex AI認証情報の渡し方。
  - [8.3-codex_cli](8.3-codex_cli): Codex CLI
  - [8.4-gemini_cli](8.4-gemini_cli): Gemini CLI
  - [8.5-copilot_cli](8.5-copilot_cli): Copilot CLI

### 本紙未掲載

- [6.1-golang_with_devcontainer_official_image](6.1-golang_with_devcontainer_official_image): DevContainer公式イメージを利用したGo言語DevContainer構築例
- [6.1-golang_with_feature](6.1-golang_with_feature): DevContainer Featuresを利用したGo言語DevContainer構築例
- [6.2-python_with_language_official_image](6.2-python_with_language_official_image): DockerHubのPython公式イメージを利用したDevContainer構築例

## LICENSE

CC-0

再掲する際は本書を一緒に紹介していただけると嬉しいです！
