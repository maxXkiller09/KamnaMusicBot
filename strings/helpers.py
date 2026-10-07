#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

HELP_1 = """✦ **ADMIN COMMANDS ✦**

◯ /pause : Pauses the currently playing music.
◯ /resume : Resumes paused music.
◯ /mute : Mutes the assistant in the voice chat.
◯ /unmute : Unmutes the assistant.
◯ /skip : Skips the current track.
◯ /stop : Stops music and clears the current playback.
◯ /shuffle : Randomly shuffles the current queue.
◯ /seek [time] : Moves playback forward to the given time.
◯ /seekback [time] : Moves playback backward.
◯ /restart : Owner-only complete bot restart.
◯ /refresh : Owner-only complete bot refresh.

**Channel aliases:** /cpause /cresume /cmute /cunmute /cskip /cstop /cshuffle /cseek /cseekback"""

HELP_2 = """✦ **AUTH COMMANDS ✦**

◯ /auth [user] : Adds a user to this group's AUTH list.
◯ /unauth [user] : Removes a user from the AUTH list.
◯ /authusers : Shows the authorized users of the group.

AUTH users can use the permitted admin playback commands without needing group-admin rights."""

HELP_3 = """✦ **G-CAST COMMANDS ✦**

◯ /channelplay [chat] : Connects a channel with the group for channel voice-chat playback.
◯ /channelplay disable : Disables channel-play mode.
◯ /cplay [query] : Plays a query in channel-play mode.
◯ /cplayforce [query] : Force-plays a query in channel-play mode.

**c = Channel Play**"""

HELP_4 = """✦ **BL-CHAT COMMANDS ✦**

◯ /blacklistchat [CHAT_ID] : Blocks a chat from using the music bot.
◯ /whitelistchat [CHAT_ID] : Removes a chat from the blacklist.
◯ /blacklistedchat : Shows all blacklisted chats."""

HELP_5 = """✦ **BL-USER COMMANDS ✦**

◯ /block [user] : Blocks a user from using bot commands.
◯ /unblock [user] : Removes a user from the blocked list.
◯ /blockedusers : Shows the blocked-user list."""

HELP_6 = """✦ **C-PLAY COMMANDS ✦**

◯ /cplay [query] : Plays music through channel-play mode.
◯ /cplayforce [query] : Force-plays the requested track immediately.
◯ /channelplay [chat] : Links channel playback to a group.

**c = Channel Play**"""

HELP_7 = """✦ **G-BAN COMMANDS ✦**

◯ /gban [user] : Globally bans a user from the bot's served chats.
◯ /ungban [user] : Removes a global ban.
◯ /gbannedusers : Shows the globally banned-user list."""

HELP_8 = """✦ **LOOP COMMANDS ✦**

◯ /loop enable : Enables loop playback.
◯ /loop disable : Disables loop playback.
◯ /loop [1-10] : Repeats the current track the selected number of times.
◯ /cloop enable/disable : Controls loop mode for channel playback.
◯ /cloop [1-10] : Repeats channel-play music the selected number of times."""

HELP_9 = """✦ **LOG COMMANDS ✦**

◯ /logger enable/disable : Enables or disables query logging.
◯ /get_log [lines] : Gets recent bot log lines.

⚠️ Log commands are intended for authorized management use."""

HELP_10 = """✦ **PING & STATS ✦**

◯ /ping : Shows bot response time and basic system/runtime stats.
◯ /stats : Shows overall bot statistics.
◯ /activevoice : Shows currently active voice chats.
◯ /activevideo : Shows currently active video calls."""

HELP_11 = """✦ **PLAY COMMANDS ✦**

◯ /play [query] : Searches and starts playing music.
◯ /vplay [query] : Plays a video in voice chat.
◯ /playforce [query] : Force-plays the requested track immediately.
◯ /vplayforce [query] : Force-plays a video immediately.
◯ /playlist : Shows saved server playlists.
◯ /deleteplaylist : Deletes a saved playlist.
◯ /channelplay [chat] : Enables channel-play setup.

**v = Video Play • force = Immediate Play**"""

HELP_12 = """✦ **SHUFFLE COMMANDS ✦**

◯ /shuffle : Randomly changes the order of the current queue.
◯ /cshuffle : Shuffles the channel-play queue."""

HELP_13 = """✦ **SEEK COMMANDS ✦**

◯ /seek [time] : Forward-seeks the current track.
◯ /seekback [time] : Moves the current track backward.
◯ /cseek [time] : Forward-seeks channel-play music.
◯ /cseekback [time] : Moves channel-play music backward."""

HELP_14 = """✦ **SONG COMMANDS ✦**

◯ /song [track/link] : Downloads a supported track as audio/video.
◯ /lyrics [music name] : Searches lyrics for the requested track.
◯ /queue : Shows the current music queue.
◯ /cqueue : Shows the channel-play queue."""

HELP_15 = """✦ **SPEED COMMANDS ✦**

◯ /speed [value] : Changes playback speed when supported by the active player.

Use the value accepted by the current player configuration."""

HELP_16 = """✦ **CLONE COMMANDS ✦**

◯ /clone : Shows the ₹399 clone payment QR and instructions.
◯ /clonepay [TRANSACTION_ID] : Submit payment proof by replying to the screenshot.
◯ /myclones : Shows your approved clone registrations.
◯ /cloneinfo : Owner-only clone request status.

💳 Payment is manually verified. The owner approves or rejects each request.

🎨 Approved clone registrations use the same music assignment/codebase; runtime activation and separate bot-process setup are handled separately.

🔐 Never send a BotFather token in chat. Clone credentials stay out of normal-user messages."""
