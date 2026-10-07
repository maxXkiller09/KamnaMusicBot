from pyrogram import filters
from pyrogram.types import Message

import config
from config.config import OWNER_ID
from YukkiMusic import app

IMAGE_PATH = "assets/Ping.jpeg"


@app.on_message(filters.command("setimage") & filters.user(OWNER_ID))
async def set_image(client, message: Message):
    reply = message.reply_to_message

    if not reply:
        return await message.reply_text(
            "🖼️ Reply to an image with /setimage."
        )

    if reply.photo:
        file = reply.photo
    elif reply.document and (reply.document.mime_type or "").startswith("image/"):
        file = reply.document
    else:
        return await message.reply_text(
            "❌ Please reply to a photo/image."
        )

    try:
        await reply.download(file_name=IMAGE_PATH)
        config.START_IMG_URL = IMAGE_PATH
        config.PING_IMG_URL = IMAGE_PATH

        await message.reply_text(
            "✅ Image set successfully!\n\n"
            "• /start image updated\n"
            "• /ping image updated\n"
            "• Owner only"
        )
    except Exception as e:
        await message.reply_text(f"❌ Failed to save image: {e}")
