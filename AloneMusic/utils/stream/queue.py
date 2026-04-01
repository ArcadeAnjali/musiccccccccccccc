import asyncio
from typing import Union

from AloneMusic.misc import db
from AloneMusic.utils.formatters import check_duration, seconds_to_min
from config import autoclean, time_to_seconds


async def put_queue(
    chat_id,
    original_chat_id,
    file,
    title,
    duration,
    user,
    vidid,
    user_id,
    stream,
    forceplay: Union[bool, str] = None,
):
    # 🔥 SAFE VALUES
    title = str(title) if title else "Unknown Song"
    user = str(user) if user else "Unknown User"
    duration = str(duration) if duration else "0:00"
    vidid = str(vidid) if vidid else "unknown"

    # 🔥 FIX title crash
    try:
        title = title.title()
    except Exception as e:
        print("❌ title error:", e)
        title = "Unknown Song"

    # 🔥 FIX duration crash
    try:
        duration_in_seconds = time_to_seconds(duration) - 3
    except Exception as e:
        print("❌ duration error:", e)
        duration_in_seconds = 0

    put = {
        "title": title,
        "dur": duration,
        "streamtype": stream,
        "by": user,
        "user_id": user_id,
        "chat_id": original_chat_id,
        "file": file,
        "vidid": vidid,
        "seconds": duration_in_seconds,
        "played": 0,
    }

    # 🔥 FIX db crash
    if chat_id not in db:
        db[chat_id] = []

    if forceplay:
        check = db.get(chat_id)
        if check:
            check.insert(0, put)
        else:
            db[chat_id] = []
            db[chat_id].append(put)
    else:
        db[chat_id].append(put)

    # 🔥 FIX autoclean crash
    try:
        if file:
            autoclean.append(file)
    except Exception as e:
        print("❌ autoclean error:", e)


async def put_queue_index(
    chat_id,
    original_chat_id,
    file,
    title,
    duration,
    user,
    vidid,
    stream,
    forceplay: Union[bool, str] = None,
):
    # 🔥 SAFE VALUES
    title = str(title) if title else "Unknown Stream"
    user = str(user) if user else "Unknown User"
    vidid = str(vidid) if vidid else "unknown"

    if "20.212.146.162" in vidid:
        try:
            dur = await asyncio.get_event_loop().run_in_executor(
                None, check_duration, vidid
            )
            duration = seconds_to_min(dur)
        except Exception as e:
            print("❌ duration fetch error:", e)
            duration = "ᴜʀʟ sᴛʀᴇᴀᴍ"
            dur = 0
    else:
        dur = 0

    put = {
        "title": title,
        "dur": duration,
        "streamtype": stream,
        "by": user,
        "chat_id": original_chat_id,
        "file": file,
        "vidid": vidid,
        "seconds": dur,
        "played": 0,
    }

    # 🔥 FIX db crash
    if chat_id not in db:
        db[chat_id] = []

    if forceplay:
        check = db.get(chat_id)
        if check:
            check.insert(0, put)
        else:
            db[chat_id] = []
            db[chat_id].append(put)
    else:
        db[chat_id].append(put)
