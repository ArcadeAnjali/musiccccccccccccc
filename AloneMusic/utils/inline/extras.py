from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# ✅ Safe ButtonStyle import
try:
    from pyrogram.enums import ButtonStyle
except ImportError:
    ButtonStyle = None

from config import SUPPORT_CHAT


def botplaylist_markup(_):
    buttons = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["S_B_9"],
                    url=SUPPORT_CHAT,
                    style=ButtonStyle.PRIMARY if ButtonStyle else None
                ),
                InlineKeyboardButton(
                    text=_["CLOSE_BUTTON"],
                    callback_data="close",
                    style=ButtonStyle.DANGER if ButtonStyle else None
                ),
            ],
        ]
    )
    return buttons


def close_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["CLOSE_BUTTON"],
                    callback_data="close",
                    style=ButtonStyle.DANGER if ButtonStyle else None
                ),
            ]
        ]
    )
    return upl


def supp_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["S_B_9"],
                    url=SUPPORT_CHAT,
                    style=ButtonStyle.PRIMARY if ButtonStyle else None
                ),
            ]
        ]
    )
    return upl
