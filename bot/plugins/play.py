import os
import re
import sys
import time
import ffmpeg
import asyncio
import subprocess
from asyncio import sleep
from youtube_dl import YoutubeDL
from pyrogram import Client, filters
from pyrogram.types import Message
from pytgcalls import GroupCallFactory
from bot.config import AUDIO_CALL, VIDEO_CALL
from youtubesearchpython import VideosSearch
from bot.helpers.decorators import authorized_users_only
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery

from bot import kay

ydl_opts = {
        "quiet": True,
        "geo_bypass": True,
        "nocheckcertificate": True,
}
ydl = YoutubeDL(ydl_opts)
group_call = GroupCallFactory(GroupCallFactory.MTPROTO_CLIENT_TYPE.PYROGRAM).get_group_call()

LOG_GROUP_ID = -1001576388235


STREAM = {8}
GROUP_CALLS = {}

@kay.on_callback_query(filters.regex("end_callback"))
async def end_callbacc(client, CallbackQuery):
    chat_id = CallbackQuery.message.chat.id
    if chat_id in AUDIO_CALL:
        text = f"⏹️ Stopped !"
        await AUDIO_CALL[chat_id].stop()
        AUDIO_CALL.pop(chat_id)
    elif chat_id in VIDEO_CALL:
        text = f"⏹️ Stopped !"
        await VIDEO_CALL[chat_id].stop()
        VIDEO_CALL.pop(chat_id)
    else:
        text = f"❌ Nothing is Playing !"
    await Client.answer_callback_query(
        CallbackQuery.id, text, show_alert=True
    )
    await Client.send_message(
        chat_id=CallbackQuery.message.chat.id,
        text=f"✅ **Streaming Stopped & Left The Video Chat !**"
    )
    await CallbackQuery.message.delete()


@kay.on_message(filters.command(["svc"]) & filters.group & ~filters.edited)
@authorized_users_only
async def stream(client, m: Message):
    msg = await m.reply_text("🔄 `Processing ...`")
    chat_id = m.chat.id
    media = m.reply_to_message
    if not media and not ' ' in m.text:
        await msg.edit("❗ __Send Me An Live Stream Link / YouTube Video Link / Reply To An Video To Start Video Streaming!__")

    elif ' ' in m.text:
        text = m.text.split(' ', 1)
        query = text[1]
        if not 'http' in query:
            return await msg.edit("❗ __Send Me An Live Stream Link / YouTube Video Link / Reply To An Video To Start Video Streaming!__")
        regex = r"^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/.+"
        match = re.match(regex, query)
        if match:
            await msg.edit("🔄 `Starting YouTube Video Stream ...`")
            try:
                meta = ydl.extract_info(query, download=False)
                formats = meta.get('formats', [meta])
                for f in formats:
                    ytstreamlink = f['url']
                link = ytstreamlink
                search = VideosSearch(query, limit=1)
                opp = search.result()["result"]
                oppp = opp[0]
                thumbid = oppp["thumbnails"][0]["url"]
                split = thumbid.split("?")
                thumb = split[0].strip()
            except Exception as e:
                return await msg.edit(f"❌ **YouTube Download Error !** \n\n`{e}`")
                print(e)

        else:
            await msg.edit("🔄 `Starting Live Video Stream ...`")
            link = query
            thumb = "https://telegra.ph/file/3e14128ad5c9ec47801bd.jpg"

        vid_call = VIDEO_CALL.get(chat_id)
        if vid_call:
            await VIDEO_CALL[chat_id].stop()
            VIDEO_CALL.pop(chat_id)
            await sleep(3)

        aud_call = AUDIO_CALL.get(chat_id)
        if aud_call:
            await AUDIO_CALL[chat_id].stop()
            AUDIO_CALL.pop(chat_id)
            await sleep(3)

        try:
            await sleep(2)
            await group_call.join(chat_id)
            await group_call.start_video(link, with_audio=True, repeat=False)
            VIDEO_CALL[chat_id] = group_call
            await msg.delete()
            await m.reply_photo(
               photo=thumb, 
               caption=f"▶️ **Started [Video Streaming]({query}) In {m.chat.title} !**",
               reply_markup=InlineKeyboardMarkup(
               [
                   [
                       InlineKeyboardButton(
                          text="⏸",
                          callback_data="pause_callback",
                       ),
                       InlineKeyboardButton(
                          text="▶️",
                          callback_data="resume_callback",
                       ),
                       InlineKeyboardButton(
                          text="⏹️",
                          callback_data="end_callback",
                       ),
                   ],
               ]),
            )
        except Exception as e:
            await msg.edit(f"❌ **An Error Occoured !** \n\nError: `{e}`")

    elif media.video or media.document:
        await msg.edit("🔄 `Downloading ...`")
        if media.video.thumbs:
            lol = media.video.thumbs[0]
            lel = await client.download_media(lol['file_id'])
            thumb = lel
        else:
            thumb = "https://telegra.ph/file/62e86d8aadde9a8cbf9c2.jpg"
        video = await client.download_media(media)

        vid_call = VIDEO_CALL.get(chat_id)
        if vid_call:
            await VIDEO_CALL[chat_id].stop()
            VIDEO_CALL.pop(chat_id)
            await sleep(3)

        aud_call = AUDIO_CALL.get(chat_id)
        if aud_call:
            await AUDIO_CALL[chat_id].stop()
            AUDIO_CALL.pop(chat_id)
            await sleep(3)

        try:
            await sleep(2)
            await group_call.join(chat_id)
            await group_call.start_video(video, with_audio=True, repeat=False)
            VIDEO_CALL[chat_id] = group_call
            await msg.delete()
            await m.reply_photo(
               photo=thumb,
               caption=f"▶️ **Started [Video Streaming](https://t.me/famouskaykay3) In {m.chat.title} !**",
               reply_markup=InlineKeyboardMarkup(
               [
                   [
                       InlineKeyboardButton(
                          text="⏸",
                          callback_data="pause_callback",
                       ),
                       InlineKeyboardButton(
                          text="▶️",
                          callback_data="resume_callback",
                       ),
                       InlineKeyboardButton(
                          text="⏹️",
                          callback_data="end_callback",
                       ),
                   ],
               ]),
            )
        except Exception as e:
            await msg.edit(f"❌ **An Error Occoured !** \n\nError: `{e}`")

    else:
        await msg.edit(
            "💁🏻‍♂️ Do you want to search for a YouTube video?",
            reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✅ Yes", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "No ❌", callback_data="close"
                    )
                ]
            ]
        )
    )


@kay.on_message(filters.command(["pause"]) & filters.group & ~filters.edited)
@authorized_users_only
async def pause(_, m: Message):
    chat_id = m.chat.id

    if chat_id in AUDIO_CALL:
        await AUDIO_CALL[chat_id].set_audio_pause(True)
        await m.reply_text("⏸ **Paused Audio Streaming !**")

    elif chat_id in VIDEO_CALL:
        await VIDEO_CALL[chat_id].set_video_pause(True)
        await m.reply_text("⏸ **Paused Video Streaming !**")

    else:
        await m.reply_text("❌ **Noting Is Streaming !**")
        
        
        

@kay.on_message(filters.command(["resume"]) & filters.group & ~filters.edited)
@authorized_users_only
async def resume(_, m: Message):
    chat_id = m.chat.id

    if chat_id in AUDIO_CALL:
        await AUDIO_CALL[chat_id].set_audio_pause(False)
        await m.reply_text("▶️ **Resumed Audio Streaming !**")

    elif chat_id in VIDEO_CALL:
        await VIDEO_CALL[chat_id].set_video_pause(False)
        await m.reply_text("▶️ **Resumed Video Streaming !**")

    else:
        await m.reply_text("❌ **Noting Is Streaming !**")


@kay.on_message(filters.command(["endstream"]) & filters.group & ~filters.edited)
@authorized_users_only
async def endstream(client, m: Message):
    msg = await m.reply_text("🔄 `Processing ...`")
    chat_id = m.chat.id

    if chat_id in AUDIO_CALL:
        await AUDIO_CALL[chat_id].stop()
        AUDIO_CALL.pop(chat_id)
        await msg.edit("⏹️ **Stopped Audio Streaming !**")

    elif chat_id in VIDEO_CALL:
        await VIDEO_CALL[chat_id].stop()
        VIDEO_CALL.pop(chat_id)
        await msg.edit("⏹️ **Stopped Video Streaming !**")

    else:
        await msg.edit("🤖 **Please Start An Stream First !**")

        
@group_call.on_audio_playout_ended
async def audio_ended_handler(_, __):
    await sleep(3)
    await group_call.stop()
    print(f"[INFO] - AUDIO_CALL ENDED !")

@group_call.on_video_playout_ended
async def video_ended_handler(_, __):
    await sleep(3)
    await group_call.stop()
    print(f"[INFO] - VIDEO_CALL ENDED !")
