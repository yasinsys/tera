import asyncio
import cloudscraper
import re
from pyrogram.errors import MessageTooLong

# Regex to detect Terabox URL
TERABOX_REGEX = r"(https?://)?(www\.)?(teraboxapp\.com|terabox\.com)/s/\w+"
from pyrogram import Client

@Client.on_message(filters.text & ~filters.command("start"))
async def handle_terabox(client: MN_Bot, message: Message):
    text = message.text.strip()
    match = re.search(TERABOX_REGEX, text)

    if not match:
        await message.reply_text("❌ Please send a valid Terabox link.")
        return

    await message.reply_text("🔄 Fetching video info from Terabox...")

    try:
        # You can call terabox-downloader here
        # This is a dummy placeholder. Replace this with actual function.
        from terabox_downloader import get_video_link  # adjust this import as per your structure

        url = match.group(0)
        video_info = await asyncio.to_thread(get_video_link, url)  # Offload to thread if blocking

        title = video_info.get("name", "Unknown Title")
        size = video_info.get("size", "Unknown Size")
        link = video_info.get("download_url")

        if not link:
            await message.reply_text("❌ Failed to extract video link.")
            return

        caption = f"🎬 <b>{title}</b>\n💾 <i>{size}</i>\n\n🔗 <a href='{link}'>Download Link</a>"
        await message.reply_text(caption, disable_web_page_preview=True)

    except MessageTooLong:
        await message.reply_text("✅ Video extracted! But it's too long to display fully.")
    except Exception as e:
        await message.reply_text(f"❌ Error: {e}")
