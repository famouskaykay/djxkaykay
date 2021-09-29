import os

from os import getenv
from dotenv import load_dotenv

load_dotenv()
admins = {}
ADMIN = int(os.getenv('ADMIN',1917528355))
CHANNEL = int(os.getenv('CHANNEL',12345))
APP_ID = int(os.getenv("API_ID", "6"))
API_HASH = os.getenv("API_HASH", "eb06d4abeb98ae0f581e")
BOT_USERNAME = os.getenv("BOT_USERNAME", "djxkaykay")
ASSISTANT_NAME = os.getenv("ASSISTANT_NAME", "famouskaykay2")
SUPPORT_GROUP = os.getenv("SUPPORT_GROUP", "KayAspirerProject")
UPDATES_CHANNEL = os.getenv("UPDATES_CHANNEL", "xprograming")
SOURCE_CODE = os.getenv("SOURCE_CODE", "github.com/famouskayky/djxkaykay")
BOT_TOKEN = os.getenv("BOT_TOKEN")
SESSION_NAME = os.getenv("SESSION_NAME")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
