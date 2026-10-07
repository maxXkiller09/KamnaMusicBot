#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

from typing import Union

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from YukkiMusic import app


def help_pannel(_, START: Union[bool, int] = None):
    labels = [
        "ADMIN", "AUTH", "G-CAST",
        "BL-CHAT", "BL-USER", "C-PLAY",
        "G-BAN", "LOOP", "LOG",
        "PING", "PLAY", "SHUFFLE",
        "SEEK", "SONG", "SPEED",
    ]

    rows = []
    for start in range(0, len(labels), 3):
        rows.append([
            InlineKeyboardButton(
                text=labels[start + offset],
                callback_data=f"help_callback hb{start + offset + 1}",
            )
            for offset in range(3)
        ])

    if START:
        rows.append([
            InlineKeyboardButton(
                text=_["BACK_BUTTON"],
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text=_["CLOSEMENU_BUTTON"],
                callback_data="close",
            ),
        ])
    else:
        rows.append([
            InlineKeyboardButton(
                text=_["CLOSEMENU_BUTTON"],
                callback_data="close",
            )
        ])

    return InlineKeyboardMarkup(rows)


def help_back_markup(_):
    return InlineKeyboardMarkup(
        [[
            InlineKeyboardButton(
                text=_["BACK_BUTTON"],
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data="close",
            ),
        ]]
    )


def private_help_panel(_):
    buttons = [[
        InlineKeyboardButton(
            text=_["S_B_1"],
            url=f"https://t.me/{app.username}?start=help",
        ),
    ]]
    return buttons
