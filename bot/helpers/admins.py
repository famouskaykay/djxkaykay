import time
from bot.assets import admins
from typing import List
from bot.assets.admins import set
from pyrogram.types import Chat
from bot.assets.admins import get as gett


async def get_administrators(chat: Chat) -> List[int]:
    get = gett(chat.id)

    if get:
        return get
    else:
        time.sleep(1)
        administrators = await chat.get_members(filter="administrators")
        to_set = []

        for administrator in administrators:
            if administrator.can_manage_voice_chats:
                to_set.append(administrator.user.id)

        set(chat.id, to_set)
        return await get_administrators(chat)
