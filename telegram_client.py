import requests
from config import TELEGRAM_BOT_TOKEN

TELEGRAM_API_URL = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"

def send_dm_to_user(player):
    chat_id = player.get("telegram_id")
    if not chat_id:
        print("No Telegram ID found for player.")
        return

    message = f"Hi {player.get('name')}, you've been selected for campaign #{player.get('campaign_id')}!"

    payload = {
        "chat_id": chat_id,
        "text": message
    }

    response = requests.post(TELEGRAM_API_URL, json=payload)

    if response.status_code != 200:
        print(f"Failed to send message: {response.text}")
