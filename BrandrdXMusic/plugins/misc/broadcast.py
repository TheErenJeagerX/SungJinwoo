import asyncio
from pyrogram import filters
from pyrogram.errors import FloodWait

from BrandrdXMusic import app
from config import OWNER_ID  # Add OWNER_ID to your config

# Flag to prevent multiple broadcasts
IS_BROADCASTING = False


@app.on_message(filters.command("broadcast") & filters.user(OWNER_ID))
async def broadcast_message(client, message):
    """
    Broadcast a message to served chats, users, and assistants.
    Only available for the bot owner.
    """
    global IS_BROADCASTING

    # Check if already broadcasting
    if IS_BROADCASTING:
        return await message.reply_text("🚫 A broadcast is already in progress.")

    # Get message details
    if message.reply_to_message:
        msg_id = message.reply_to_message.id
        chat_id = message.chat.id
    else:
        if len(message.command) < 2:
            return await message.reply_text("❌ Please provide a message to broadcast.")
        query = message.text.split(None, 1)[1]
        query = query.replace("-pin", "").replace("-nobot", "").replace("-pinloud", "").replace("-assistant", "").replace("-user", "")
        if query == "":
            return await message.reply_text("❌ The broadcast message cannot be empty.")

    # Set broadcasting flag
    IS_BROADCASTING = True
    await message.reply_text("✅ Starting broadcast...")

    # Broadcast to chats
    if "-nobot" not in message.text:
        sent, pinned = 0, 0
        chats = [int(chat["chat_id"]) for chat in await get_served_chats()]
        for chat in chats:
            try:
                if message.reply_to_message:
                    msg = await app.forward_messages(chat, chat_id, msg_id)
                else:
                    msg = await app.send_message(chat, text=query)

                # Handle pinning
                if "-pin" in message.text:
                    try:
                        await msg.pin(disable_notification=True)
                        pinned += 1
                    except:
                        continue
                elif "-pinloud" in message.text:
                    try:
                        await msg.pin(disable_notification=False)
                        pinned += 1
                    except:
                        continue

                sent += 1
                await asyncio.sleep(0.2)
            except FloodWait as fw:
                await asyncio.sleep(fw.value)
            except:
                continue

        await message.reply_text(f"✅ Broadcast completed: {sent} chats, {pinned} messages pinned.")

    # Reset broadcasting flag
    IS_BROADCASTING = False