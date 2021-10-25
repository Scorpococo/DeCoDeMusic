from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from config import BOT_NAME as bn
from helpers.filters import other_filters2
from time import time
from datetime import datetime
from helpers.decorators import authorized_users_only
from config import BOT_USERNAME, ASSISTANT_USERNAME

START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("week", 60 * 60 * 24 * 7),
    ("day", 60 ** 2 * 24),
    ("hour", 60 ** 2),
    ("min", 60),
    ("sec", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else "s"))
    return ", ".join(parts)


@Client.on_message(other_filters2)
async def start(_, message: Message):
        await message.reply_text(
        f"""**Hᴇʏ, ɪ ᴀᴍ 𝗖𝗿𝗲𝗽𝗮𝗻 🤴
ᴀɴ ᴀᴅᴠᴀɴᴄᴇᴅ ᴘʀᴇᴍɪᴜᴍ
sᴜᴘᴇʀғᴀsᴛ ᴀɴᴅ ʜɪɢʜ ǫᴜᴀʟɪᴛʏ ᴠᴄ ᴍᴜsɪᴄ
ᴘʟᴀʏᴇʀ ʙᴏᴛ ᴄʀᴇᴀᴛᴇᴅ ʙʏ [ᴄʀᴇᴀᴛᴏʀ ᴘᴀᴠᴀɴ](https://t.me/creatorpavan) ...**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝗖𝗢𝗠𝗠𝗔𝗡𝗗 𝗟𝗜𝗦𝗧", url="https://telegra.ph/Creator-Pavan-10-24")
                  ],[
                    InlineKeyboardButton(
                       "𝗦𝗨𝗣𝗣𝗢𝗥𝗧", url="https://t.me/TheCreatorPavan"
                    ),
                    InlineKeyboardButton(
                        "𝗦𝗘𝗥𝗩𝗘𝗥", url="https://t.me/creatorpavan"
                    )
                ],[
                    InlineKeyboardButton(
                        "➕ ᴀᴅᴅ ᴍᴇ ᴛᴏ ᴜʀ ɢʀᴜᴘ ➕",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )
