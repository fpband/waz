# (c) @FarshidBand

import asyncio
from configs import Config
from pyrogram.errors import FloodWait, UserNotParticipant
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def handle_force_subscribe(bot, cmd):
    try:
        invite_link = await bot.create_chat_invite_link(int(Config.UPDATES_CHANNEL))
    except FloodWait as e:
        await asyncio.sleep(e.x)
        return 400
    try:
        user = await bot.get_chat_member(int(Config.UPDATES_CHANNEL), cmd.from_user.id)
        if user.status == "kicked":
            await bot.send_message(
                chat_id=cmd.from_user.id,
                text="Sorry Sir, You are Banned to use me. Contact my [Support Group](https://t.me/farshidband).",
                parse_mode="markdown",
                disable_web_page_preview=True
            )
            return 400
    except UserNotParticipant:
        await bot.send_message(
            chat_id=cmd.from_user.id,
            text="**• برای کارکردن ربات در کانال زیر عضو شوید.**\n\n**🔚 سپس /start را کلیک کنید.😊👇👇**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🌸 عضویت 🌸", url=invite_link.invite_link)
                    ],
                    [
                        InlineKeyboardButton("✅ عضو شدم 👍", callback_data="refreshmeh")
                    ]
                ]
            ),
            parse_mode="markdown"
        )
        return 400
    except Exception:
        await bot.send_message(
            chat_id=cmd.from_user.id,
            text="😏 مشکلی پیش آمد. [گزارش مشکل](https://t.me/farshidband).",
            parse_mode="markdown",
            disable_web_page_preview=True
        )
        return 400
