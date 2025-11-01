#!/bin/bash
# マウント対象のディレクトリを予め作成しておく
# Dockerランタイムによっては存在しないディレクトリをマウントできなかったり、
# root権限で作成される場合があるため
mkdir -p ~/.cache/devcontainer/python/uv-cache
mkdir -p ~/.cache/devcontainer/node/npm-cache
mkdir -p ~/.cache/devcontainer/node/npm-config
mkdir -p ~/.cache/devcontainer/node/node-gyp
mkdir -p ~/.cache/devcontainer/node/node-pre-gyp
mkdir -p ~/.cache/devcontainer/node/pnpm-store
