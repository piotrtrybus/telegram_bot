import requests
from config import OPTIMOVE_API_KEY, OPTIMOVE_BASE_URL

def fetch_player_data(campaign_id: str):
    headers = {
        "Authorization": f"Bearer {OPTIMOVE_API_KEY}",
        "Content-Type": "application/json"
    }

    response = requests.get(
        f"{OPTIMOVE_BASE_URL}/campaigns/{campaign_id}/players",
        headers=headers
    )

    if response.status_code != 200:
        print(f"Error fetching players: {response.status_code}")
        return []

    data = response.json()
    return data.get("players", [])
