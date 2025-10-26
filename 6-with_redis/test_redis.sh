#!/bin/bash
set -xe

export REDISCLI_AUTH="redis-password"
redis-cli -h redis -p 6379 --user app SET test_key "Hello, Redis!"
redis-cli -h redis -p 6379 --user app GET test_key
