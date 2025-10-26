# 言語公式イメージの利用
# https://hub.docker.com/_/golang
FROM golang:1.25.1-trixie

ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID

# マウント時、親ディレクトリが作られていないと、root権限で作成されてしまうため、事前に作成しておく
RUN mkdir -p /home/vscode/.cache/go-build /go/pkg && \
    chown -R $USER_UID:$USER_GID /home/vscode && \
    chmod 777 -R /home/vscode/.cache /go/pkg

# 各ツールのインストール
RUN go install golang.org/x/tools/gopls@latest; \
    go install github.com/cweill/gotests@latest; \
    go install github.com/josharian/impl@latest; \
    go install github.com/go-delve/delve/cmd/dlv@latest

# golangci-lintのバージョン固定
ENV GOLANGCI_LINT_VERSION=v1.64.8
RUN curl -sSfL https://raw.githubusercontent.com/golangci/golangci-lint/HEAD/install.sh | sh -s -- -b $(go env GOPATH)/bin $GOLANGCI_LINT_VERSION
