import requests
from pyrogram import filters
from BrandrdXMusic import app

# Replace this with a working Instagram video download API
API_URL = "https://api.example.com/instagram?url="

@app.on_message(filters.command(["ig", "instagram", "reel"]))
async def download_instagram_video(client, message):
    if len(message.command) < 2:
        await message.reply_text("Please provide the Instagram Reel URL after the command.")
        return

    a = await message.reply_text("Processing...")
    url = message.text.split()[1]
    full_api_url = f"{API_URL}{url}"

    try:
        # Make a request to the API
        response = requests.get(full_api_url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()

        if data.get("status"):
            video_url = data["data"][0].get("url")
            await a.delete()
            await client.send_video(message.chat.id, video_url)
        else:
            await a.edit("Failed to download the reel. The URL might be invalid.")
    except requests.exceptions.RequestException as e:
        await a.edit(f"An error occurred while processing your request: {e}")
    except Exception as e:
        await a.edit(f"An unexpected error occurred: {e}")

__MODULE__ = "Instagram"
__HELP__ = """/reel [Instagram Reel URL] - To download the reel.
/ig [Instagram Reel URL] - To download the reel.
/instagram [Instagram Reel URL] - To download the reel."""