#!/bin/bash
# .secrets/bedrock_api_key に一時的な Bedrock API Key を生成して保存
uv run .devcontainer/generate_bedrock_shortterm_api_key_to_secrets.py
