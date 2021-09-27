import os
from os import getenv
from dotenv import load_dotenv

load_dotenv()

admins = {}
AUDIO_CALL = {}
VIDEO_CALL = {}
API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH", "")
BOT_TOKEN = getenv("BOT_TOKEN", "1995793533:AAESBMKOqi9exREz_DeW3kw8ijsMWhUMmKM")
SESSION_STRING = getenv("SESSION_STRING", "")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "KayAspirerProject")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "KayAspirerProject")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "userrr0001")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
REPLY_MESSAGE = getenv("REPLY_MESSAGE", "")
if REPLY_MESSAGE:
    REPLY_MESSAGE = REPLY_MESSAGE
else:
    REPLY_MESSAGE = None
