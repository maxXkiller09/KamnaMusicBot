import asyncio
import json
import os
import re
import sys

import config
from pyrogram import filters
from pyrogram.types import Message

from YukkiMusic import app

SETTINGS_FILE = "data/owner_settings.json"
MEDIA_DIR = "assets"


def _load():
    try:
        with open(SETTINGS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}


def _save(data):
    os.makedirs(os.path.dirname(SETTINGS_FILE), exist_ok=True)
    tmp = SETTINGS_FILE + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    os.replace(tmp, SETTINGS_FILE)


def _is_owner(message: Message):
    return bool(message.from_user and message.from_user.id in config.OWNER_ID)


def _url(value):
    return bool(re.match(r"^https?://", value))


def _set(key, value):
    data = _load()
    data[key] = value
    _save(data)


async def _set_media(message: Message, target):
    reply = message.reply_to_message
    if not reply:
        return "❌ Reply to a photo or video with the command."

    os.makedirs(MEDIA_DIR, exist_ok=True)

    if reply.photo:
        path = f"{MEDIA_DIR}/{target}.jpg"
        await reply.download(file_name=path)
        return path

    if reply.video:
        path = f"{MEDIA_DIR}/{target}.mp4"
        await reply.download(file_name=path)
        return path

    if reply.document and (reply.document.mime_type or "").startswith("image/"):
        path = f"{MEDIA_DIR}/{target}.jpg"
        await reply.download(file_name=path)
        return path

    if reply.document and (reply.document.mime_type or "").startswith("video/"):
        path = f"{MEDIA_DIR}/{target}.mp4"
        await reply.download(file_name=path)
        return path

    return "❌ Please reply to a photo or video."


OWNER_COMMANDS = [
    "setwelcome", "setimage", "setsupport", "setupdates",
    "setowner", "addowner", "delowner", "setbotname",
    "setbotlink", "setgithub", "setloggroup", "botsettings",
    "setplaylistimage", "setglobalimage", "setstatsimage",
    "setaudioimage", "setvideoimage", "setstreamimage",
    "setyoutubeimage", "setspotifyartistimage", "setspotifyalbumimage",
    "setspotifyplaylistimage", "setcloneqr",
    "restart", "reloadall", "refresh",
]


@app.on_message(filters.command(OWNER_COMMANDS))
async def owner_settings(client, message: Message):
    if not _is_owner(message):
        return

    command = message.command[0].lower()
    args = message.command[1:]

    if command in ("setwelcome", "setimage"):
        path = await _set_media(message, "Welcome")
        if path.startswith("❌"):
            return await message.reply_text(path)

        config.START_IMG_URL = path
        _set("START_IMG_URL", path)

        if path.lower().endswith((".jpg", ".jpeg", ".png")):
            config.PING_IMG_URL = path
            _set("PING_IMG_URL", path)

        return await message.reply_text(
            "✅ Welcome media updated.\n\n"
            "• /start updated\n"
            "• Photo also updates /ping\n"
            "• Owner only"
        )

    image_commands = {
        "setplaylistimage": ("PLAYLIST_IMG_URL", "Playlist"),
        "setglobalimage": ("GLOBAL_IMG_URL", "Global"),
        "setstatsimage": ("STATS_IMG_URL", "Stats"),
        "setaudioimage": ("TELEGRAM_AUDIO_URL", "Audio"),
        "setvideoimage": ("TELEGRAM_VIDEO_URL", "Video"),
        "setstreamimage": ("STREAM_IMG_URL", "Stream"),
        "setyoutubeimage": ("YOUTUBE_IMG_URL", "Youtube"),
        "setspotifyartistimage": ("SPOTIFY_ARTIST_IMG_URL", "SpotifyArtist"),
        "setspotifyalbumimage": ("SPOTIFY_ALBUM_IMG_URL", "SpotifyAlbum"),
        "setspotifyplaylistimage": ("SPOTIFY_PLAYLIST_IMG_URL", "SpotifyPlaylist"),
    }

    if command in image_commands:
        key, target = image_commands[command]
        path = await _set_media(message, target)
        if path.startswith("❌"):
            return await message.reply_text(path)
        setattr(config, key, path)
        _set(key, path)
        return await message.reply_text(
            f"✅ {target} image updated.\n• Owner only"
        )

    if command == "setcloneqr":
        path = await _set_media(message, "CloneQR")
        if path.startswith("❌"):
            return await message.reply_text(path)
        config.CLONE_QR_IMAGE = path
        _set("CLONE_QR_IMAGE", path)
        return await message.reply_text(
            "✅ Clone payment QR updated.\n\n"
            "• This QR will be shown in the ₹399 clone payment flow\n"
            "• Owner only"
        )

    if command in ("restart", "reloadall", "refresh"):
        label = "RELOAD ALL" if command == "reloadall" else command.upper()
        await message.reply_text(
            f"🔄 {label} requested. Full bot reload starting...\n\n"
            "• Music/VC process will restart\n"
            "• Group handlers will reload\n"
            "• Voice-chat glitches should clear\n"
            "• Bot will reconnect automatically\n\n"
            "Please wait a few seconds."
        )
        await asyncio.sleep(1)
        os.execv(sys.executable, [sys.executable] + sys.argv)
        return

    if command == "setsupport":
        if len(args) != 1 or not _url(args[0]):
            return await message.reply_text("Usage: /setsupport https://t.me/...")
        config.SUPPORT_GROUP = args[0]
        _set("SUPPORT_GROUP", args[0])
        return await message.reply_text("✅ Support group updated.")

    if command == "setupdates":
        if len(args) != 1 or not _url(args[0]):
            return await message.reply_text("Usage: /setupdates https://t.me/...")
        config.SUPPORT_CHANNEL = args[0]
        _set("SUPPORT_CHANNEL", args[0])
        return await message.reply_text("✅ Updates channel updated.")

    if command in ("setowner", "addowner", "delowner"):
        if len(args) != 1 or not args[0].lstrip("-").isdigit():
            return await message.reply_text(
                f"Usage: /{command} USER_ID"
            )

        uid = int(args[0])
        owners = list(config.OWNER_ID)

        if command == "setowner":
            owners = [uid]
        elif command == "addowner":
            if uid not in owners:
                owners.append(uid)
        else:
            if uid in owners:
                owners.remove(uid)
            if not owners:
                return await message.reply_text("❌ At least one owner is required.")

        config.OWNER_ID = owners
        _set("OWNER_ID", owners)
        return await message.reply_text(
            "✅ Owner list updated.\n\n"
            + "Owners: " + ", ".join(map(str, owners))
        )

    if command == "setbotname":
        if not args:
            return await message.reply_text("Usage: /setbotname Kamna Music")
        name = " ".join(args).strip()
        if not name.isascii():
            return await message.reply_text("❌ Use normal ASCII text for bot name.")
        config.MUSIC_BOT_NAME = name
        _set("MUSIC_BOT_NAME", name)
        return await message.reply_text(f"✅ Bot name set to: {name}")

    if command == "setbotlink":
        if len(args) != 1 or not _url(args[0]):
            return await message.reply_text("Usage: /setbotlink https://t.me/YourBot")
        _set("BOT_LINK", args[0])
        return await message.reply_text("✅ Bot link saved.")

    if command == "setgithub":
        if len(args) != 1 or not _url(args[0]):
            return await message.reply_text("Usage: /setgithub https://github.com/...")
        config.GITHUB_REPO = args[0]
        _set("GITHUB_REPO", args[0])
        return await message.reply_text("✅ GitHub repository updated.")

    if command == "setloggroup":
        if len(args) != 1 or not args[0].lstrip("-").isdigit():
            return await message.reply_text("Usage: /setloggroup -1001234567890")
        config.LOG_GROUP_ID = int(args[0])
        _set("LOG_GROUP_ID", config.LOG_GROUP_ID)
        return await message.reply_text("✅ Log group updated.")

    if command == "botsettings":
        data = _load()
        return await message.reply_text(
            "⚙️ OWNER SETTINGS\n\n"
            f"👑 Owners: {', '.join(map(str, config.OWNER_ID))}\n"
            f"🎵 Bot name: {config.MUSIC_BOT_NAME}\n"
            f"🖼️ Welcome: {config.START_IMG_URL}\n"
            f"🔔 Support: {config.SUPPORT_GROUP or 'Not set'}\n"
            f"📢 Updates: {config.SUPPORT_CHANNEL or 'Not set'}\n"
            f"📦 GitHub: {config.GITHUB_REPO or 'Not set'}\n"
            f"📝 Log group: {config.LOG_GROUP_ID}\n"
            f"💾 Saved keys: {len(data)}"
        )
