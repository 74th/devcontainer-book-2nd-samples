FROM mcr.microsoft.com/devcontainers/base

# node.jsをnodesource.comからインストール
RUN apt-get update && \
    apt-get install -y curl && \
    curl -fsSL https://deb.nodesource.com/setup_22.x | bash - && \
    apt-get install -y nodejs && \
    rm -rf /var/lib/apt/lists/*

ENV PATH="/home/vscode/npm/bin:${PATH}"
