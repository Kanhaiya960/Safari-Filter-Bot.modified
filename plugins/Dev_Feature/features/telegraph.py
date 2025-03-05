# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


import os
import asyncio
import requests
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery
IMGBB_API_KEY = "d4cc3d793cb68b2c6cdc2197588e895c"

@Client.on_message(filters.command(["img", "telegraph"], prefixes="/") & filters.reply)
async def c_upload(client, message: Message):
    reply = message.reply_to_message
    if not reply.media:
        return await message.reply_text("Reply to a media to upload it to Cloud.")
    if reply.document and reply.document.file_size > 5 * 1024 * 1024:  # 5 MB
        return await message.reply_text("File size limit is 5 MB.")
    msg = await message.reply_text("Processing...")
    try:
        downloaded_media = await reply.download()
        if not downloaded_media:
            return await msg.edit_text("Something went wrong during download.")
        with open(downloaded_media, "rb") as f:
            resp = requests.post(
                "https://api.imgbb.com/1/upload",
                data={"key": IMGBB_API_KEY},
                files={"image": f}
            )
        os.remove(downloaded_media)
        
        if resp.status_code == 200:
            result = resp.json()
            if result["success"]:
                await msg.edit_text(f"{result['data']['url']}")
            else:
                await msg.edit_text("Something went wrong. Please try again later.")
        else:
            await msg.edit_text("Something went wrong. Please try again later.")

    except Exception as e:
        await msg.edit_text(f"Error: {str(e)}")
        return
    await uploading_message.edit_text(
        text=f"<b>Link :-</b>\n\n<code>{image_url}</code>",
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton(text="Open Link", url=image_url),
            InlineKeyboardButton(text="Share Link", url=f"https://telegram.me/share/url?url={image_url}")
            ],[
            InlineKeyboardButton(text="✗ Close ✗", callback_data="close")
            ]])
        )
    
