#!/bin/bash
devcontainer up \
  --workspace-folder=. \
  --dotfiles-repository=github.com/74th/devcontainer-book-2nd-samples \
  --dotfiles-install-command=4-git_config_from_dotfiles/dotfiles/install.sh \