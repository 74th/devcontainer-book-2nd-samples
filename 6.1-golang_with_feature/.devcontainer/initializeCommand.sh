#!/bin/bash
# マウント対象のディレクトリを予め作成しておく
# Dockerランタイムによっては存在しないディレクトリをマウントできなかったり、
# root権限で作成される場合があるため
mkdir -p ~/.cache/devcontainer/go/cache-go-build
mkdir -p ~/.cache/devcontainer/go/pkg-mod
mkdir -p ~/.cache/devcontainer/go/pkg-submdb
