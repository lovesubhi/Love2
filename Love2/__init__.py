import asyncio
import logging
import time
from pytgcalls import PyTgCalls
from importlib import import_module
from dotenv import load_dotenv
from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN, SESSION_STRING

loop = asyncio.get_event_loop()
load_dotenv()
boot = time.time()

logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s",
    level=logging.INFO,
)

Love2 = Client(
    ":Love2:",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
)

userbot = Client(
    ":userbot:",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=SESSION_STRING,
)

pytgcalls = PyTgCalls(userbot)

async def Love2_bot():
    global BOT_ID, BOT_NAME, BOT_USERNAME
    try:
        await Love2.start()
        await userbot.start()
        await pytgcalls.start()
        getme = await Love2.get_me()
        BOT_ID = getme.id
        BOT_USERNAME = getme.username
        if getme.last_name:
            BOT_NAME = getme.first_name + " " + getme.last_name
        else:
            BOT_NAME = getme.first_name
    except Exception as e:
        print(f"Error during authorization: {e}")

loop.run_until_complete(Love2_bot())
