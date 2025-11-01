#!/bin/bash
# sudo権限の剥奪
sudo rm -rf /etc/sudoers.d/*

# golangci-lintのバージョン固定
GOLANGCI_LINT_VERSION=v1.64.8
curl -sSfL https://raw.githubusercontent.com/golangci/golangci-lint/HEAD/install.sh | sh -s -- -b $(go env GOPATH)/bin $GOLANGCI_LINT_VERSION

# 依存パッケージのインストール
go get ./...
