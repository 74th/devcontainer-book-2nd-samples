Copilot CLIを使う

認証情報等を永続化する場合以下を、コンテナ外にマウントする

- ~/.copilot

起動前に先にディレクトリを作っておく

```
mkdir -p ~/.llm/copilot/.copilot
mkdir -p ~/.llm/copilot/.config/configstore
```

認証キーも ~/.copilot/ に保存される
