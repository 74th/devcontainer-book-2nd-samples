# 公式イメージの利用
# https://github.com/devcontainers/images/tree/main/src/go
FROM mcr.microsoft.com/devcontainers/go:1.25

# golangci-lintのバージョン固定
ENV GOLANGCI_LINT_VERSION=v1.64.8
RUN curl -sSfL https://raw.githubusercontent.com/golangci/golangci-lint/HEAD/install.sh | sh -s -- -b $(go env GOPATH)/bin $GOLANGCI_LINT_VERSION

# マウント時、親ディレクトリが作られていないと、root権限で作成されてしまうため、事前に作成しておく
RUN mkdir -p /home/vscode/.cache/go-build && \
    chown -R vscode:vscode /home/vscode/.cache
