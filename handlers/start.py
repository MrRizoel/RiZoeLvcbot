# OxyXmusic (Telegram bot project )
# Copyright (C) 2021 RiZoeL

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.



from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn




@Client.on_message(filters.command("start") & filters.private & ~filters.channel)
async def start(_, message: Message):
     await message.reply_sticker("CAACAgUAAxkBAAEKP8NgvTDX7MzbIpbtB3WzX0AfUiSw_gAC0AIAAvbj0VQ6KQtObIJRdR8E")
     await message.reply_text(
        f"""➼ Helloow 👋 {message.from_user.first_name}! I can play music in voice chats of Telegeam Groups. I have a lot of cool feature that will amaze you!\n\n➤ Do you want me to play music in your Telegram groups'voice chats? Please click the " cσммαη∂s " button below to know how you can use me.\n\n➤ Use the buttons below to know more about me 🖤\n\n➤ Contact my owner [🖤 ℝ𝕚ℤ𝕠𝕖𝕃 🖤](https://t.me/TheRiZoeL)""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "📜 cσммαη∂s 📜", url="https://telegra.ph/RiZoeL-MuSic-06-03-2")
                  ],[
                    InlineKeyboardButton(
                        "🖤 𝕄𝚢 𝕆𝚠𝚗𝚎𝚛 🖤️", url="https://t.me/TheRiZoeL"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "❤️ σғғιcιαℓ gяσυρ ❤️", url="https://t.me/X_F0RCE_TEAM"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**➤ Music player is online**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🖤 ᎷᎽ ϴᏔΝᎬᎡ 🖤", url="https://t.me/TheRiZoeL")
                ]
            ]
        )
   )
@Client.on_message(
    filters.private & filters.incoming & filters.command(['help']))
def _help(client, message):
    client.send_message(chat_id = message.chat.id,
        text = tr.HELP_MSG[1],
        parse_mode="markdown",
        disable_web_page_preview=True,
        disable_notification=True,
        reply_markup = InlineKeyboardMarkup(map(1)),
        reply_to_message_id = message.message_id
    )

help_callback_filter = filters.create(lambda _, __, query: query.data.startswith('help+'))

@Client.on_callback_query(help_callback_filter)
def help_answer(client, callback_query):
    chat_id = callback_query.from_user.id
    disable_web_page_preview=True
    message_id = callback_query.message.message_id
    msg = int(callback_query.data.split('+')[1])
    client.edit_message_text(chat_id=chat_id,    message_id=message_id,
        text=tr.HELP_MSG[msg],    reply_markup=InlineKeyboardMarkup(map(msg))
    )


def map(pos):
    if(pos==1):
        button = [
            [InlineKeyboardButton(text = '⊳️', callback_data = "help+2")]
        ]
    elif(pos==len(tr.HELP_MSG)-1):
        url = f"https://t.me/cartoons_007"
        button = [
            [InlineKeyboardButton("✙ᴀᴅᴅ ᴍᴇ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ✙", url=f"https://t.me/RiZoeLvcBoT?startgroup=true")],
            [InlineKeyboardButton(text = 'Assɪsᴛᴀɴᴛ', url=f"https://t.me/RiZoeL_VC?startgroup=true"),
             InlineKeyboardButton(text = '⛊ Ｏｗｎｅｒ ⛊', url=f"https://t.me/TheRiZoeL")],
            [InlineKeyboardButton(text = '⊲', callback_data = f"help+{pos-1}")]
        ]
    else:
        button = [
            [
                InlineKeyboardButton(text = '⊲️', callback_data = f"help+{pos-1}"),
                InlineKeyboardButton(text = '️⊳', callback_data = f"help+{pos+1}")
            ],
        ]
    return button

@Client.on_message(filters.command("help") & ~filters.private & ~filters.channel)
async def ghelp(_, message: Message):
    await message.reply_text(
        f"""**ʜᴇʟʟᴏ ᴛʜᴇʀᴇ ! ɪ ᴄᴀɴ ᴘʟᴀʏ ᴍᴜsɪᴄ ɪɴ ᴛʜᴇ ᴠᴏɪᴄᴇ ᴄʜᴀᴛs ᴏғ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘs & ᴄʜᴀɴɴᴇʟs**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "༆ ᴄʟɪᴄᴋ ʜᴇʀᴇ ғᴏʀ ʜᴇʟᴘ", url=f"https://t.me/RiZoeLvcBoT?start"
                    )
                ]
            ]
        ),
    )


