# DockerHubの公式イメージを利用
# https://hub.docker.com/_/python
FROM python:3.13.7

# uv のインストール
COPY --from=ghcr.io/astral-sh/uv:0.8.22 /uv /uvx /bin/
RUN mkdir -p /var/uv/cache; \
    chmod 777 /var/uv/cache
ENV UV_COMPILE_BYTECODE=1 \
    UV_SYSTEM_PYTHON=true \
    UV_CACHE_DIR=/var/uv/cache \
    UV_LINK_MODE=copy
