# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel @Tech_VJ
# Ask Doubt on Telegram @KingVJ01

import os
import asyncio
import requests
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery

IMGBB_API_KEY = "d4cc3d793cb68b2c6cdc2197588e895c"

@Client.on_message(filters.command(["img", "telegraph"], prefixes=["/", "!"]) & filters.reply)
async def upload_to_imgbb(client, message: Message):
    reply = message.reply_to_message
    
    if not reply or not reply.media:
        return await message.reply_text("📌 Reply to any **Photo, Video, or Document** to Upload.")

    if reply.document and reply.document.file_size > 5 * 1024 * 1024:
        return await message.reply_text("🚫 File size limit is **5MB**.")

    msg = await message.reply_text("🔄 Uploading to Cloud...")

    try:
        # Download media
        media_file = await reply.download()
        if not media_file:
            return await msg.edit_text("❌ Download Failed!")

        with open(media_file, "rb") as file:
            response = requests.post(
                "https://api.imgbb.com/1/upload",
                data={"key": IMGBB_API_KEY},
                files={"image": file}
            )

        os.remove(media_file)  # Clean up downloaded file

        if response.status_code == 200:
            result = response.json()
            if result["success"]:
                image_url = result['data']['url']
                await msg.edit_text(
                    f"<b>✅ Successfully Uploaded!</b>\n\n🔗 Link: <code>{image_url}</code>",
                    disable_web_page_preview=True,
                    reply_markup=InlineKeyboardMarkup([
                        [InlineKeyboardButton("🌐 Open Link", url=image_url)],
                        [InlineKeyboardButton("🔗 Share Link", url=f"https://telegram.me/share/url?url={image_url}")],
                        [InlineKeyboardButton("✖ Close", callback_data="close")]
                    ])
                )
            else:
                await msg.edit_text("❌ Upload Failed! Try Again.")
        else:
            await msg.edit_text("❌ Error from Server! Try Again Later.")

    except Exception as e:
        await msg.edit_text(f"🚫 Error: `{str(e)}`")
