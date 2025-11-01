FROM python:3.13.7-trixie

# https://code.visualstudio.com/remote/advancedcontainers/add-nonroot-user

# 非rootユーザの引数
ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID

# 非rootユーザの追加
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME
# sudo の追加
RUN apt-get update \
    && apt-get install -y sudo \
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME

# uv のインストール
COPY --from=ghcr.io/astral-sh/uv:0.8.22 /uv /uvx /bin/
RUN mkdir -p /var/uv/cache; \
    chmod 777 /var/uv/cache
ENV UV_COMPILE_BYTECODE=1 \
    UV_SYSTEM_PYTHON=true \
    UV_CACHE_DIR=/var/uv/cache \
    UV_LINK_MODE=copy

# ユーザでコマンドの実行
USER $USERNAME
RUN uv tool install ruff@0.13.2
