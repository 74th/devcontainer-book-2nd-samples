#!/bin/bash
# sudo権限の剥奪
sudo rm -rf /etc/sudoers.d/*

# 依存パッケージのインストール
uv sync --all-groups
cd todo_frontend; npm install

# pnpmのストアディレクトリを変更
mkdir -p /home/vscode/.pnpm-store
pnpm config set store-dir /home/vscode/.pnpm-store
