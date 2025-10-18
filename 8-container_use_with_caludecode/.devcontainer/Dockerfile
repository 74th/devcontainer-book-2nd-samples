FROM mcr.microsoft.com/devcontainers/javascript-node

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
ENV UV_PYTHON_INSTALL_DIR=/var/uv/python
ENV UV_CACHE_DIR=/var/uv/cache
