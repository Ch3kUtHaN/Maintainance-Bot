# (c) HeimanPictures

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import Config

@Client.on_message(filters.private & filters.command(['start', 'help', 'about']))
async def start(bot, update):
    await update.reply_text(
        text=Config.MAINTAINANCE_TEXT.format(update.from_user.first_name),
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [
              [InlineKeyboardButton("📌 Bot Updates 📌", url=Config.UPDATE_CHANNEL)],
              [InlineKeyboardButton("🎈 Channel 🎈", url=Config.SUPPORT_GROUP)]
            ]
        )
    )
