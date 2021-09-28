from bot import vcusr
import logging
import os 
from pyrogram import Client, idle
from bot.config import API_ID, API_HASH, BOT_TOKEN

kay = Client(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="plugins"),
)
if not os.path.isdir("./downloads"):
    os.makedirs("./downloads")

logging.basicConfig(level=logging.WARNING,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

if __name__ == "__main__" :
    vcusr.run()

kay.start()
idle()
Bot.stop()
