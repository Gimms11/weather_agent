import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv()

api_key = os.getenv("API_KEY")
base_url = os.getenv("BASE_URL", "https://api.llmgateway.io/v1")
model_name = os.getenv("MODEL_NAME", "gemini-3.5-flash-lite")

model = init_chat_model(
    model=model_name,
    model_provider="openai",
    api_key=api_key,
    base_url=base_url,
)
