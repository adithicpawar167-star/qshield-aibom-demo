from openai import AzureOpenAI
client = AzureOpenAI(
    azure_endpoint="https://test-resource.openai.azure.com",
    api_version="2024-02-01"
)
