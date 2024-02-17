from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
from config import BOT_USERNAME, OWNER_ID, SUPPORT
from pyrogram.types import InlineKeyboardButton as ib
import asyncio
from Love2 import Love2 as app


START_TEXT = """
ʜᴇʏ, {0} \n\nɪ'ᴍ {1}, \n\n⊱ᴀ ʙᴏᴛ ᴍᴀᴅᴇ ʙʏ ᴀ ʙʀᴏᴋᴇɴ💔ʜᴇᴀʀᴛ ᴀꜱ ᴛʜᴇ ʟᴀꜱᴛ ᴛʜɪɴɢ ꜰʀᴏᴍ ʜɪꜱ ᴍᴇᴍᴏʀɪᴇꜱ🥺.\n\n⊱ʟᴇᴛ ᴜꜱ ꜱᴛᴀʀᴛ ᴀ ᴊᴏᴜʀɴᴇʏ ʙᴜᴛ ᴀʟᴏɴᴇ ʙᴇᴄᴀᴜꜱᴇ ᴇᴠᴇʀʏ ᴘᴀʀᴛɴᴇʀ ʟᴇᴀᴠᴇ ᴀꜰᴛᴇʀ ᴀ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ᴛɪᴍᴇ .\n\nᴍʏ ᴄʀᴇᴀᴛᴇʀ ɪꜱ ᴠᴇʀʏ ɪɴɴᴏᴄᴇɴᴛ🥺ɪꜰ ʏᴏᴜ ᴡᴀɴᴛ ʜᴇʟᴘ ᴛᴏ ᴍᴀᴋᴇ ʙᴏᴛ ᴏʀ ʜᴀᴠᴇ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ ᴀʙᴏᴜᴛ  ɪᴛ ᴅᴍ || [ᴄʜɪᴋᴜ💔](https://t.me/Subhi_love)|| ɪ ᴡɪʟʟ ᴛᴇᴀᴄʜ ʏᴏᴜ ꜰʀɪᴇɴᴅ**"
"""
# ------------------------------------------------------------------------------- #




@app.on_message(filters.command("start") & filters.private)
async def start(client, message):
    buttons = [
        [
            InlineKeyboardButton("↠↠ᗩᗪᗪ--ᒪOᐯE--Iᑎ↞↞", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
            InlineKeyboardButton("↠↠𝗚𝗥𝗢𝗨𝗣↞↞", url=f"https://t.me/{SUPPORT}"),
            InlineKeyboardButton("----#𝙾𝚆𝙽𝙴𝚁#----", user_id=OWNER_ID)
        ]
    ]

    reply_markup = InlineKeyboardMarkup(buttons)

    await message.reply_video(
        video="https://telegra.ph/file/11bbd93331dbcde9cb1f7.mp4",
        caption=START_TEXT,
        reply_markup=reply_markup
    )
