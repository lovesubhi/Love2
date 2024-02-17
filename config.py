import os
from os import getenv

API_ID = int(getenv("API_ID", None))

API_HASH = getenv("API_HASH", None)

BOT_USERNAME = getenv("BOT_USERNAME", None)

BOT_TOKEN = getenv("BOT_TOKEN", None)

OWNER_ID = int(getenv("OWNER_ID", None))

SUDO_USERS = list(map(int, getenv("SUDO_USERS", None).split())) if getenv("SUDO_USERS", None) else []

MONGO_URL = getenv("MONGO_URL", None)

SESSION_STRING = getenv("SESSION_STRING", None)

CHANNEL = getenv("CHANNEL", None)

SUPPORT = getenv("SUPPORT", None)

OWNER_USERNAME = getenv("OWNER_USERNAME", None)

PING_PIC =[""]
