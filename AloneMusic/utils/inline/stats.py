from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# ✅ Safe ButtonStyle import
try:
    from pyrogram.enums import ButtonStyle
except ImportError:
    ButtonStyle = None


def stats_buttons(_, status):
    not_sudo = [
        InlineKeyboardButton(
            text=_["SA_B_1"],
            callback_data="TopOverall",
            style=ButtonStyle.PRIMARY if ButtonStyle else None
        )
    ]

    sudo = [
        InlineKeyboardButton(
            text=_["SA_B_2"],
            callback_data="bot_stats_sudo",
            style=ButtonStyle.SUCCESS if ButtonStyle else None
        ),
        InlineKeyboardButton(
            text=_["SA_B_3"],
            callback_data="TopOverall",
            style=ButtonStyle.PRIMARY if ButtonStyle else None
        ),
    ]

    upl = InlineKeyboardMarkup(
        [
            sudo if status else not_sudo,
            [
                InlineKeyboardButton(
                    text=_["CLOSE_BUTTON"],
                    callback_data="close",
                    style=ButtonStyle.DANGER if ButtonStyle else None
                ),
            ],
        ]
    )
    return upl


def back_stats_buttons(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"],
                    callback_data="stats_back",
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
    return upl
