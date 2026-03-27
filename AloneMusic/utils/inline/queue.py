from typing import Union
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# ✅ Safe ButtonStyle import
try:
    from pyrogram.enums import ButtonStyle
except ImportError:
    ButtonStyle = None


def queue_markup(
    _,
    DURATION,
    CPLAY,
    videoid,
    played: Union[bool, int] = None,
    dur: Union[bool, int] = None,
):
    not_dur = [
        [
            InlineKeyboardButton(
                text=_["QU_B_1"],
                callback_data=f"GetQueued {CPLAY}|{videoid}",
                style=ButtonStyle.PRIMARY if ButtonStyle else None
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data="close",
                style=ButtonStyle.DANGER if ButtonStyle else None
            ),
        ]
    ]

    dur_buttons = [
        [
            InlineKeyboardButton(
                text=_["QU_B_2"].format(played, dur),
                callback_data="GetTimer",
                style=ButtonStyle.SUCCESS if ButtonStyle else None
            )
        ],
        [
            InlineKeyboardButton(
                text=_["QU_B_1"],
                callback_data=f"GetQueued {CPLAY}|{videoid}",
                style=ButtonStyle.PRIMARY if ButtonStyle else None
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data="close",
                style=ButtonStyle.DANGER if ButtonStyle else None
            ),
        ],
    ]

    upl = InlineKeyboardMarkup(not_dur if DURATION == "Unknown" else dur_buttons)
    return upl


def queue_back_markup(_, CPLAY):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"],
                    callback_data=f"queue_back_timer {CPLAY}",
                    style=ButtonStyle.PRIMARY if ButtonStyle else None
                ),
                InlineKeyboardButton(
                    text=_["CLOSE_BUTTON"],
                    callback_data="close",
                    style=ButtonStyle.DANGER if ButtonStyle else None
                ),
            ]
        ]
    )
    return upl


def aq_markup(_, chat_id):
    buttons = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="ᴄʟᴏsᴇ",
                    callback_data="close",
                    style=ButtonStyle.DANGER if ButtonStyle else None
                )
            ],
        ]
    )
    return buttons
