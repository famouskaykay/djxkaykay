from pyrogram import Client
from bot.config import API_ID, API_HASH, BOT_TOKEN

kay = Client(
    "VideoPlayer",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN
)
kay.start()
ok = kay.get_me()
USERNAME = ok.username
BOT_NAME = ok.first_name
