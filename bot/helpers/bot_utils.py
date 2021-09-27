from pyrogram import Client
from bot.config import API_ID, API_HASH, BOT_TOKEN
from bot import vcusr


vcusr.start()
ok = vcusr.get_me()
USERNAME = ok.username
BOT_NAME = ok.first_name
