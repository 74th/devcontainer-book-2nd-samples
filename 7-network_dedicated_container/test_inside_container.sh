#!/bin/bash
uv sync
uv run -m pytest --timeout=10 --timeout-method=thread