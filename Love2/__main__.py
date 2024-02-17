import asyncio
import importlib
from pyrogram import idle
from Love2 import Love2
from Love2.modules import ALL_MODULES

 

loop = asyncio.get_event_loop()


async def subhi_boot():
    for all_module in ALL_MODULES:
        importlib.import_module("Love2.modules." + all_module)
    print("»»»» 𝗟𝗼𝘃𝗲💔 𝗗𝗲𝗽𝗹𝗼𝘆 𝗦𝘂𝗰𝗰𝗲𝘀𝘀𝗳𝘂𝗹𝗹𝘆 🤧")
    await idle()
    print("♡---𝗦𝗮𝘆𝗼𝗻𝗮𝗿𝗮!! 𝗦𝘁𝗼𝗽𝗽𝗶𝗻𝗴 𝗕𝗼𝘁🧐--♡")


if __name__ == "__main__":
    loop.run_until_complete(subhi_boot())
