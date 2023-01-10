import os
from dotenv import load_dotenv
from bot import client
import openai

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
openai.api_key = os.getenv("OPENAI_API_KEY")

client.run(DISCORD_TOKEN)
