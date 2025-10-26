#!/bin/bash
# sudo権限の剥奪
sudo rm -rf /etc/sudoers.d/*

# 依存パッケージのインストール
go get ./...
