from kay import kaykay
from kay import TOKEN, API_ID, API_HASH
from pyrogram import Client
import logging, os

logging.basicConfig(level=logging.WARNING,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

Client(
    "djkaykay",
    API_ID,
    API_HASH,
    bot_token=TOKEN,
    plugins={'root': 'kay.plugins'}
).start()
os.system("echo 'Bot Started'")
kaykay.run()
