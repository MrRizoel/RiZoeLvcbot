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
     await message.reply_sticker("CAACAgUAAxkBAAEKLOFgtzauneaP6WbcRfJlPMvPz_CCLgAC0AIAAvbj0VQ6KQtObIJRdR8E")
     await message.reply_text(
        f"""βΌ Helloow π {message.from_user.first_name}! I can play music in voice chats of Telegeam Groups. I have a lot of cool feature that will amaze you!\n\nβ€ Do you want me to play music in your Telegram groups'voice chats? Please click the " cΟΠΌΠΌΞ±Ξ·βs " button below to know how you can use me.\n\nβ€ Use the buttons below to know more about me π€\n\nβ€ Contact my owner [π€ βπβ€π ππ π€](https://t.me/TheRiZoeL)""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "π cΟΠΌΠΌΞ±Ξ·βs π", url="https://telegra.ph/RiZoeL-MuSic-06-03-2")
                  ],[
                    InlineKeyboardButton(
                        "π€ ππ’ ππ πππ π€οΈ", url="https://t.me/TheRiZoeL"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "β€οΈ Ο??ΞΉcΞΉΞ±β gΡΟΟΟ β€οΈ", url="https://t.me/X_F0RCE_TEAM"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**β€ Music player is online**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "π€ α·α½ Ο΄αΞα¬α‘ π€", url="https://t.me/TheRiZoeL")
                ]
            ]
        )
   )
@Client.on_message(
    filters.command("help")
    & filters.private
    & ~ filters.edited
)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""<b>Here Is Cmd Of ΚΙͺα΄’α΄α΄Κ_α΄α΄sΙͺα΄ !
ββββββββββ°β¦β±βββββββββ
/ply  - play audio or link you requested
/play  - play song you requested
/dplay  - play song you requested via deezer
/splay  - play song you requested via jio saavn
/playlist - Show now playing list
/current - Show now playing
/song  - download songs you want quickly
/search  - search videos on youtube with details
/deezer  - download songs you want quickly via deezer
/saavn  - download songs you want quickly via saavn

β’Admins onlyβ’
/player - open music player settings panel
/pause - pause song play
/resume - resume song play
/skip - play next song
/end - stop music play
/userbotjoin - invite assistant to your chat
/admincache - Refresh admin list
ββββββββββ°β¦β±βββββββββ
 </b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "β² AssΙͺsα΄α΄Ι΄α΄ β³", url="https://t.me/RiZoeL_VC?startgroup=true"
                    )
                ],[
                    InlineKeyboardButton(
                        "β οΌ―ο½ο½ο½ο½ β", url="https://t.me/TheRiZoeL"
                    ),
                    InlineKeyboardButton(
                        "βα΄α΄α΄ α΄α΄ ΙͺΙ΄ Κα΄α΄Κ Ι’Κα΄α΄α΄β", url="https://t.me/RiZoeLvcBoT?startgroup=true"
                    )
                ]
            ]
        )
    )

    