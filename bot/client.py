import os
from binance.client import Client
from dotenv import load_dotenv

load_dotenv()

def get_client():
    api_key = os.getenv("BINANCE_API_KEY")
    api_secret = os.getenv("BINANCE_API_SECRET")

    # ✅ Create client WITHOUT pinging spot API
    client = Client(
        api_key,
        api_secret,
        testnet=True   # 🔥 THIS IS THE KEY FIX
    )

    return client