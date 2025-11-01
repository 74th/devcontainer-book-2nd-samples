#!/bin/bash

# Goの各ツールのインストール
# ユーザ権限でインストールするので、ユーザが更新できる
go install golang.org/x/tools/gopls@latest
go install github.com/cweill/gotests@latest
go install github.com/josharian/impl@latest
go install github.com/go-delve/delve/cmd/dlv@latest

# golangci-lintのバージョン固定
GOLANGCI_LINT_VERSION=v1.64.8
curl -sSfL https://raw.githubusercontent.com/golangci/golangci-lint/HEAD/install.sh | sh -s -- -b $(go env GOPATH)/bin $GOLANGCI_LINT_VERSION

# 依存パッケージのインストール
go get ./...
