iptablesを使ったfirewall構築によるネットワーク隔離のサンプル

claude codeのサンプルを元にしたものです
https://github.com/anthropics/claude-code/blob/main/.devcontainer/init-firewall.sh

フィルタされたIPアドレスを知るためにxt_recentモジュールを使用しています。

.devcontainer/check_dropped_ip.sh を実行することで、ドロップされたIPアドレスを確認できます。
