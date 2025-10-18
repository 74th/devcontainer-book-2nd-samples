geminiを使い、Googleのアカウントでログインして利用する

認証情報等を永続化する場合以下を、コンテナ外にマウントする

- ~/.gemini
- ~/.config/configstore

起動前に先にディレクトリを作っておく

```
mkdir -p ~/.llm/gemini/.gemini
mkdir -p ~/.llm/gemini/.config/configstore
```
