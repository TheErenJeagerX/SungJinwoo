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
        caption=f"Hey {message.from_user.mention}\n\nI'm {MUSIC_BOT_NAME}\n\n•  sᴜɴɢ ᴊɪɴ ᴡᴏᴏ ɪs ᴀʟɪᴠᴇ •
┏────✦────────┓
  ★ ʙᴏᴛ ᴠᴇʀsɪᴏɴ : 2.0
  ★ ᴩʏʀᴏɢʀᴀᴍ : 2.0.106
  ★ ᴅᴇᴠᴇʟᴏᴘᴇʀ : @TheErenYeager & @EminenceCurse
  ★ sᴜᴘᴘᴏʀᴛ : @Ahjin_Sprt
┗────✦────────┛\n\n",
        reply_markup=InlineKeyboardMarkup(
            [
               [
            InlineKeyboardButton(
                text="• ᴏᴡɴᴇʀ •", url=f"https://t.me/TheErenYeager"
            ),
            InlineKeyboardButton(
                text="• sᴜᴘᴘᴏʀᴛ •", url=f"https://t.me/Ahjin_Sprt"
            ),
        ],
                [
            InlineKeyboardButton(
                text="• ᴜᴘᴅᴀᴛᴇs •", url=f"https://t.me/SungUpdates"
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
