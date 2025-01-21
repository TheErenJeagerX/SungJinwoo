import requests
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from BrandrdXMusic import app
from config import BANNED_USERS


@app.on_message(filters.command("lyrics") & ~BANNED_USERS)
async def lyrics_search(client, message: Message):
    if len(message.command) < 2:
        return await message.reply_text("❌ Please provide the song title!")

    title = message.text.split(None, 1)[1]
    m = await message.reply_text("🔍 Searching for lyrics...")

    # API request to ovh.lyrics
    try:
        response = requests.get(f"https://api.lyrics.ovh/v1/{title}")
        if response.status_code == 200:
            data = response.json()
            lyrics = data.get("lyrics", None)

            if not lyrics:
                return await m.edit(f"❌ No lyrics found for `{title}`.")
            
            # Displaying lyrics
            if len(lyrics) > 4000:  # If lyrics exceed Telegram message limit
                return await m.edit(
                    "⚠️ Lyrics are too long to display here. Please check an external source."
                )

            await m.edit(f"🎵 **Lyrics for** `{title}`:\n\n{lyrics}")
        else:
            await m.edit(f"❌ Lyrics not found for `{title}`.")
    except Exception as e:
        await m.edit(f"❌ Error occurred: {e}")