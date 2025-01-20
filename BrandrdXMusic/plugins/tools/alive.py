import asyncio

from BrandrdXMusic import app
from pyrogram import filters
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from config import MUSIC_BOT_NAME

@app.on_message(filters.command(["alive"]))
async def start(client: Client, message: Message):
    await message.reply_video(
        video=f"https://files.catbox.moe/1gw87u.mp4",
        caption=f"Hey {message.from_user.mention}\n\nI'm {MUSIC_BOT_NAME}\n\nHey There, I'm Alive.\n\n",
        reply_markup=InlineKeyboardMarkup(
            [
               [
            InlineKeyboardButton(
                text="Owner", url=f"https://t.me/TheErenYeager"
            ),
            InlineKeyboardButton(
                text="Support", url=f"https://t.me/Ahjin_Sprt"
            ),
        ],
                [
            InlineKeyboardButton(
                text="Updates", url=f"https://t.me/SungUpdates"
            ),
                ],
                [
                    InlineKeyboardButton(
                        "🗑️ Close", callback_data="close"
                    )
                ],
            ]
        )
    )
