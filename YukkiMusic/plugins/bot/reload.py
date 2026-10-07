from pyrogram import filters
from pyrogram.types import Message

from config import BANNED_USERS
from YukkiMusic import app
from YukkiMusic.core.call import Yukki

@app.on_message(
    filters.command("reload")
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
async def group_reload(client, message: Message):
    chat_id = message.chat.id
    try:
        await message.reply_text("🔄 Reloading this group's music/VC session only...")
        await Yukki.stop_stream(chat_id)
        await message.reply_text("✅ This group's music session has been reset. Other groups were not affected.")
    except Exception as e:
        await message.reply_text(f"❌ Group reload failed: {type(e).__name__}")
