#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >.
#

from motor.motor_asyncio import AsyncIOMotorClient as _mongo_client_
from pymongo import MongoClient

import config

from ..logging import LOGGER


if not config.MONGO_DB_URI:
    raise RuntimeError(
        "MONGO_DB_URI is required. Refusing to use an embedded/default MongoDB credential."
    )

_mongo_async_ = _mongo_client_(config.MONGO_DB_URI)
_mongo_sync_ = MongoClient(config.MONGO_DB_URI)

_db_name = getattr(config, "MONGO_DB_NAME", "Yukki").strip() or "Yukki"
mongodb = _mongo_async_[_db_name]
pymongodb = _mongo_sync_[_db_name]
