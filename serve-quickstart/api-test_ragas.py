import argparse
import os

from openai import OpenAI

parser = argparse.ArgumentParser()
# parser.add_argument("--base-url", default="https://api.openai.com")
parser.add_argument("--base-url", default="https://model-service-gateway-a5vw2t543kme.oregon.google-cluster.vessl.ai")
parser.add_argument("--api-key", default="token-abc123")
parser.add_argument("--model-name", default="explodinggradients/Ragas-critic-llm-Qwen1.5-GPTQ")
parser.add_argument("--prompt", default="나는 한글을 사랑해요.")
args = parser.parse_args()

client = OpenAI(
    base_url=os.path.join(args.base_url, "v1"),
    # api_key=args.api_key,
)

completion = client.chat.completions.create(
    model=args.model_name,
    messages=[
        {"role": "system", "content": "Translate into English."},
        {"role": "user", "content": args.prompt},
    ],
)

print(completion.choices[0].message.content)