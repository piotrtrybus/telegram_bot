from fastapi import FastAPI, Request
from optimove_client import fetch_player_data
from telegram_client import send_dm_to_user

app = FastAPI()

@app.post("/optimove-webhook")
async def optimove_webhook(request: Request):
    payload = await request.json()
    campaign_id = payload.get("campaign_id")

    if not campaign_id:
        return {"error": "No campaign_id in payload"}

    # Fetch player data from Optimove
    players = fetch_player_data(campaign_id)

    # Send Telegram DMs
    for player in players:
        send_dm_to_user(player)

    return {"status": "success"}
