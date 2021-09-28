import os
from bot.plugins.nopm import User
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

kay.start()
User.start()
print("\n[INFO] - STARTED VIDEO PLAYER BOT, JOIN @ASMSAFONE !")

idle()
kay.stop()
User.stop()
print("\n[INFO] - STOPPED VIDEO PLAYER BOT, by famouskaykay !")
