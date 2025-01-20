import os
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from BrandrdXMusic import app
import requests


def upload_file(file_path):
    url = "https://catbox.moe/user/api.php"
    data = {"reqtype": "fileupload", "json": "true"}
    files = {"fileToUpload": open(file_path, "rb")}
    response = requests.post(url, data=data, files=files)

    if response.status_code == 200:
        return True, response.text.strip()
    else:
        return False, f"Error: {response.status_code} - {response.text}"


@app.on_message(filters.command(["tgm", "tgt", "telegraph", "tl"]))
async def get_link_group(client, message):
    if not message.reply_to_message:
        return await message.reply_text(
            "Please Reply To A Media To Upload On Telegraph"
        )

    media = message.reply_to_message
    file_size = 0
    if media.photo:
        file_size = media.photo.file_size
    elif media.video:
        file_size = media.video.file_size
    elif media.document:
        file_size = media.document.file_size

    if file_size > 200 * 1024 * 1024:
        return await message.reply_text("Please Provide A Media File Under 200MB.")

    try:
        text = await message.reply("Processing...")

        async def progress(current, total):
            try:
                await text.edit_text(f"📥 Downloading... {current * 100 / total:.1f}%")
            except Exception:
                pass

        try:
            local_path = await media.download(progress=progress)
            await text.edit_text("🖨️Uploading To Telegraph...")

            success, upload_path = upload_file(local_path)

            if success:
                await text.edit_text(
                    f"💾 | [Uploaded Link]({upload_path})",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    "ᴜᴘʟᴏᴀᴅᴇᴅ ғɪʟᴇ",
                                    url=upload_path,
                                )
                            ]
                        ]
                    ),
                )
            else:
                await text.edit_text(
                    f"An Error Occurred While Uploading Your File\n{upload_path}"
                )

            try:
                os.remove(local_path)
            except Exception:
                pass

        except Exception as e:
            await text.edit_text(f"🗃️ File Upload Failed\n\n<i>Rᴇᴀsᴏɴ: {e}</i>")
            try:
                os.remove(local_path)
            except Exception:
                pass
            return
    except Exception:
        pass


__HELP__ = """
**Telegraph Upload Bot Commands**

Use These Commands To Upload Media To Telegraph:

- `/tgm`: Upload Replied Media To Telegraph.
- `/tgt`: Same As `/tgm`.
- `/telegraph`: Same As `/tgm`.
- `/tl`: Same As `/tgm`.

**ᴇxᴀᴍᴘʟᴇ:**
- Reply To A Photo Or Video With `/tgm` To Upload It.

**Note:**
You Must Reply To A Media File For The Upload To Work.
"""

__MODULE__ = "Telegraph"
