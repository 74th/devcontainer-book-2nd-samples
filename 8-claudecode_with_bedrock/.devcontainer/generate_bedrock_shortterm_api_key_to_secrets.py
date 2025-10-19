# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "aws-bedrock-token-generator",
# ]
# ///
import pathlib
from aws_bedrock_token_generator import provide_token

output_path = pathlib.Path("~/.secrets/bedrock_api_key").expanduser()

def main() -> None:
    token = provide_token(region="ap-northeast-1")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(token)

    print("generated token")


if __name__ == "__main__":
    main()
