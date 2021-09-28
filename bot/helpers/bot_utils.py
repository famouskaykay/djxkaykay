from bot import vcusr
from bot.config import API_ID, API_HASH, BOT_TOKEN

vcusr.start()
ok = vcusr.get_me()
USERNAME = ok.username
BOT_NAME = ok.first_name
