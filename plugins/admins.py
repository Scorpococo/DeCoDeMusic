from asyncio.queues import QueueEmpty
from config import que
from pyrogram import Client, filters
from pyrogram.types import Message
import sira
import DeCalls
from cache.admins import set
from helpers.decorators import authorized_users_only, errors
from helpers.channelmusic import get_chat_id
from helpers.filters import command, other_filters
from Client import callsmusic


@Client.on_message(command(["pause", "jeda"]) & other_filters)
@errors
@authorized_users_only
async def pause(_, message: Message):
    callsmusic.pytgcalls.pause_stream(message.chat.id)
    await message.reply_photo(
                             photo="https://telegra.ph/file/dd6814e241bfc4c0255cd.jpg", 
                             caption="**⏸ Music Paused.\n use /resume**"
    )


@Client.on_message(command(["resume", "lanjut"]) & other_filters)
@errors
@authorized_users_only
async def resume(_, message: Message):
    callsmusic.pytgcalls.resume_stream(message.chat.id)
    await message.reply_photo(
                             photo="https://telegra.ph/file/d0f2dd5b7519bb5444139.jpg", 
                             caption="**▶️ Music Resumed.\n use /pause**"
    )


@Client.on_message(command(["end", "stop"]) & other_filters)
@errors
@authorized_users_only
async def stop(_, message: Message):
    try:
        callsmusic.queues.clear(message.chat.id)
    except QueueEmpty:
        pass

    callsmusic.pytgcalls.leave_group_call(message.chat.id)
    await message.reply_photo(
                             photo="https://telegra.ph/file/8d22aa7d53b6acb9a125e.jpg", 
                             caption="🏷️ **ꜱᴛᴏᴘᴘᴇᴅ ꜱᴛʀᴇᴀᴍɪɴɢ ꜰʀᴏᴍ ᴄʀᴇᴀᴛᴏʀ ᴘᴀᴠᴀɴ ꜱᴇʀᴠᴇʀ.**"
    )


@Client.on_message(command(["skip", "next"]) & other_filters)
@errors
@authorized_users_only
async def skip(_, message: Message):
    global que
    chat_id = get_chat_id(message.chat)
    if chat_id not in callsmusic.pytgcalls.active_calls:
        await message.reply_text("ɴᴏᴛʜɪɴɢ ᴘʟᴀʏɪɴɢ..!")
    else:
        callsmusic.queues.task_done(chat_id)

        if callsmusic.queues.is_empty(chat_id):
            callsmusic.pytgcalls.leave_group_call(chat_id)
        else:
            callsmusic.pytgcalls.change_stream(
                chat_id, callsmusic.queues.get(chat_id)["file"]
            )

    qeue = que.get(chat_id)
    if qeue:
        skip = qeue.pop(0)
    if not qeue:
        return
    await message.reply_photo(
                             photo="https://telegra.ph/file/96129f4d0e984d2432e55.jpg", 
                             caption="f- ꜱᴋɪᴘᴘᴇᴅ **{skip[0]}**\n- ɴᴏᴡ ᴘʟᴀʏɪɴɢ **{qeue[0][0]}** ʙʏ ᴄʀᴇᴀᴛᴏʀ ᴘᴀᴠᴀɴ."
    )


@Client.on_message(filters.command(["reload", "refresh"]))
@errors
@authorized_users_only
async def admincache(client, message: Message):
    set(
        message.chat.id,
        (
            member.user
            for member in await message.chat.get_members(filter="administrators")
        ),
    )

    await message.reply_photo(
                              photo="https://telegra.ph/file/d881ea9de7620ecc36d08.jpg",
                              caption="**ʀᴇʟᴏᴀᴅᴇᴅ ♻️\n ᴀᴅᴍɪɴ ʟɪꜱᴛ ᴜᴘᴅᴀᴛᴇᴅ ʙʏ ᴄʀᴇᴀᴛᴏʀ ᴘᴀᴠᴀɴ.**"
    )
