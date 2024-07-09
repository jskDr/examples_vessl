import argparse
import os

from openai import OpenAI

parser = argparse.ArgumentParser()
# parser.add_argument("--base-url", default="https://api.openai.com")
parser.add_argument("--base-url", default="https://model-service-gateway-ah60lx61f7b6.oregon.google-cluster.vessl.ai")
parser.add_argument("--api-key", default="token-abc123")
parser.add_argument("--model-name", default="JamesKim/mistral-7b-qlora-alpaca-1k-0509_ARC-Train")
parser.add_argument("--prompt", default="당신은 누구입니까?")
args = parser.parse_args()

client = OpenAI(
    base_url=os.path.join(args.base_url, "v1"),
    # api_key=args.api_key,
)

completion = client.chat.completions.create(
    model=args.model_name,
    messages=[
        # {"role": "system", "content": "Translate into English."},
        {"role": "user", "content": args.prompt},
    ],
)

print(completion.choices[0].message.content)