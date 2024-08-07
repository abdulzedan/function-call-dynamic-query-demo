from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from openai import AzureOpenAI
import os


token_provider = get_bearer_token_provider(
    DefaultAzureCredential(), "https://cognitiveservices.azure.com/.default"
)

api_version = os.getenv("AZURE_OPENAI_VERSION")
endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")

client = AzureOpenAI(
    api_version=api_version,
    azure_endpoint=endpoint,
    azure_ad_token_provider=token_provider,
)

response = client.chat.completions.create(
    model=os.getenv("AZURE_OPENAI_CHAT_DEPLOYMENT"),
    messages=[{"role": "user", "content": "Tell me a bedtime story"}],
    max_tokens=100,
)
print(response.choices[0].message.content)
