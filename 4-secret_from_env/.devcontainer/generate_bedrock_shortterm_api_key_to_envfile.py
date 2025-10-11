# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "aws-bedrock-token-generator",
# ]
# ///
from aws_bedrock_token_generator import provide_token
import pathlib

env_file = pathlib.Path(".devcontainer/devcontainer.env")

def main() -> None:
    # https://github.com/aws/aws-bedrock-token-generator-python/blob/main/README.md
    token = provide_token(region="ap-northeast-1")
    env_file.write_text(
        "AWS_BEARER_TOKEN_BEDROCK=" + token + "\n",
    )


if __name__ == "__main__":
    main()
