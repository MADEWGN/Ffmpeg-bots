from pyrogram import Client, filters

from ffmpegbot import (
    HELP_STICKER,
    TMP_DOWNLOAD_DIRECTORY
)


@Client.on_message(filters.command(["start"]))
async def start_text(client, message):
    await message.reply_sticker(HELP_STICKER, quote=True)
