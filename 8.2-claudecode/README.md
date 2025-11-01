claudecodeを使い、claudecodeのアカウントでログインして利用する

認証情報等を永続化する場合以下を、コンテナ外にマウントする

- ~/.claude.json
- ~/.claude/

起動前に先にディレクトリを作っておく

```
mkdir -p ~/.llm/claude/.claude
touch ~/.llm/claude/.claude.json
```

最初だけ、`.claude.json` が意図しないファイルである旨のエラーが出ますが、fixをさせることができる
