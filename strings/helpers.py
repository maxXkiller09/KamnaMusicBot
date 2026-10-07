#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

HELP_1 = """🛡️ **ADMIN COMMANDS**

/pause — Pause the playing music.
/resume — Resume paused music.
/mute — Mute the playing music.
/unmute — Unmute the playing music.
/skip — Skip the current track.
/stop — Stop the current playback.

**Channel aliases:** /cpause /cresume /cmute /cunmute /cskip /cstop"""

HELP_2 = """🔐 **AUTH COMMANDS**

/auth [user] — Add a user to the group AUTH list.
/unauth [user] — Remove a user from the AUTH list.
/authusers — Check the AUTH users of the group.

AUTH users can use permitted admin playback commands without group-admin rights."""

HELP_3 = """📡 **G-CAST COMMANDS**

/channelplay [chat] — Connect a channel to a group for voice-chat streaming.
/channelplay disable — Disable channel-play mode.
/cplay — Play in channel mode.
/cplayforce — Force play in channel mode."""

HELP_4 = """🚫 **BL-CHAT COMMANDS**

/blacklistchat [CHAT_ID] — Blacklist a chat.
/whitelistchat [CHAT_ID] — Remove a chat from blacklist.
/blacklistedchat — View blacklisted chats.

These are management commands and follow the bot's permission system."""

HELP_5 = """🚫 **BL-USER COMMANDS**

/block [user] — Block a user from using the bot.
/unblock [user] — Remove a user from the blocked list.
/blockedusers — Check the blocked-user list."""

HELP_6 = """🎙️ **C-PLAY COMMANDS**

/cplay [query] — Play a query in channel-play mode.
/cplayforce [query] — Force play without clearing the queue.
/channelplay [chat] — Link channel playback to a group.

**c** means channel play."""

HELP_7 = """⛔ **G-BAN COMMANDS**

/gban [user] — Globally ban a user from served chats.
/ungban [user] — Remove a global ban.
/gbannedusers — View globally banned users.

These commands require the appropriate management permission."""

HELP_8 = """🔁 **LOOP COMMANDS**

/loop [enable/disable] — Toggle loop playback.
/loop [1-10] — Repeat the current track the selected number of times.
/cloop [enable/disable] — Channel-play loop mode.
/cloop [1-10] — Repeat in channel-play mode."""

HELP_9 = """📝 **LOG COMMANDS**

/logger [enable/disable] — Control query logging.
/get_log [lines] — View recent bot log lines.

Log-management commands require authorized management access."""

HELP_10 = """📶 **PING COMMANDS**

/ping — Check bot response, RAM/CPU and basic runtime status.

Use this for a quick health check without exposing private configuration."""

HELP_11 = """▶️ **PLAY COMMANDS**

/play [query] — Play music.
/vplay [query] — Play video.
/playforce [query] — Force play.
/vplayforce [query] — Force video play.
/playlist — View saved server playlists.
/deleteplaylist — Delete a saved playlist.

**v** means video play; **force** starts the requested track immediately."""

HELP_12 = """🔀 **SHUFFLE COMMANDS**

/shuffle — Randomly shuffle the current queue.
/cshuffle — Shuffle the channel-play queue."""

HELP_13 = """⏩ **SEEK COMMANDS**

/seek [time] — Forward seek to a duration.
/seekback [time] — Seek backward.
/cseek [time] — Forward seek in channel-play mode.
/cseekback [time] — Backward seek in channel-play mode."""

HELP_14 = """🎵 **SONG COMMANDS**

/song [track] — Download a YouTube track as supported by the bot.
/lyrics [music name] — Search lyrics for a track.
/queue — View the current music queue.
/cqueue — View the channel-play queue."""

HELP_15 = """⚡ **SPEED COMMANDS**

/speed [value] — Change playback speed when supported by the active player.

Use the value accepted by your current player configuration."""
