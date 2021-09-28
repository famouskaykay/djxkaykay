from bot import kay
from bot.config import API_ID, API_HASH, BOT_TOKEN

kay.start()
ok = kay.get_me()
USERNAME = ok.username
BOT_NAME = ok.first_name
