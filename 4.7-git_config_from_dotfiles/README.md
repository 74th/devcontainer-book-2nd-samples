dotfilesを使って、git configを行う。


### VS Code, Cursor

```json
// settings.json
{
  "dotfiles.repository": "https://github.com/74th/devcontainer-book-2nd-samples.git",
  "dotfiles.installCommand": "4-git_config_from_dotfiles/dotfiles/install.sh",
}
```

### DevContainer CLI

```bash
devcontainer up \
  --workspace-folder=. \
  --dotfiles-repository=https://github.com/74th/devcontainer-book-2nd-samples.git \
  --dotfiles-install-command=4-git_config_from_dotfiles/dotfiles/install.sh \
```

### JetBrains IDE

現状、そのような機能はなさそう。