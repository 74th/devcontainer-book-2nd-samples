# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "aws-bedrock-token-generator",
# ]
# ///
from aws_bedrock_token_generator import provide_token
import pathlib

# bedrockの一時トークンをClaudeCode用に発効し、.envrcに保存するスクリプト

env_file = pathlib.Path(".envrc")

def main() -> None:
    # https://github.com/aws/aws-bedrock-token-generator-python/blob/main/README.md
    token = provide_token(region="ap-northeast-1")
    env_file.write_text(f"""
export AWS_BEARER_TOKEN_BEDROCK={token}
export CLAUDE_CODE_USE_BEDROCK=1
export AWS_REGION=ap-northeast-1
"""
    )


if __name__ == "__main__":
    main()
