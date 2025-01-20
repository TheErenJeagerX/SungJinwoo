import logging

from googlesearch import search
from pyrogram import filters

from BrandrdXMusic import app
from SafoneAPI import SafoneAPI


@app.on_message(filters.command(["google", "gle"]))
async def google(bot, message):
    if len(message.command) < 2 and not message.reply_to_message:
        await message.reply_text("Example:\n\n`/google lord ram`")
        return

    if message.reply_to_message and message.reply_to_message.text:
        user_input = message.reply_to_message.text
    else:
        user_input = " ".join(message.command[1:])
    b = await message.reply_text("**Searching On Google....**")
    try:
        a = search(user_input, advanced=True)
        txt = f"Search Query: {user_input}\n\nresults"
        for result in a:
            txt += f"\n\n[❍ {result.title}]({result.url})\n<b>{result.description}</b>"
        await b.edit(
            txt,
            disable_web_page_preview=True,
        )
    except Exception as e:
        await b.edit(e)
        logging.exception(e)


@app.on_message(filters.command(["app", "apps"]))
async def app(bot, message):
    if len(message.command) < 2 and not message.reply_to_message:
        await message.reply_text("Example:\n\n`/app Free Fire`")
        return

    if message.reply_to_message and message.reply_to_message.text:
        user_input = message.reply_to_message.text
    else:
        user_input = " ".join(message.command[1:])
    cbb = await message.reply_text("**Searching On Play Store....**")
    a = await SafoneAPI().apps(user_input, 1)
    b = a["results"][0]
    icon = b["icon"]
    id = b["id"]
    link = b["link"]
    ca = b["description"]
    title = b["title"]
    dev = b["developer"]
    info = f"<b>[Title : {title}]({link})</b>\n<b>ɪᴅ</b>: <code>{id}</code>\n<b>Developer</b> : {dev}\n<b>Description </b>: {ca}"
    try:
        await message.reply_photo(icon, caption=info)
        await cbb.delete()
    except Exception as e:
        await message.reply_text(e)
