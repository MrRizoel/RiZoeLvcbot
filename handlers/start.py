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
    filters.command("help")
    & filters.private
    & ~ filters.edited
)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""<b>Here Is Cmd Of ʀɪᴢᴏᴇʟ_ᴍᴜsɪᴄ !
╔━━━━━━━━⊰✦⊱━━━━━━━━╗
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

•Admins only•
/player - open music player settings panel
/pause - pause song play
/resume - resume song play
/skip - play next song
/end - stop music play
/userbotjoin - invite assistant to your chat
/admincache - Refresh admin list
╚━━━━━━━━⊰✦⊱━━━━━━━━╝
 </b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⊲ Assɪsᴛᴀɴᴛ ⊳", url="https://t.me/RiZoeL_VC?startgroup=true"
                    )
                ],[
                    InlineKeyboardButton(
                        "⛊ Ｏｗｎｅｒ ⛊", url="https://t.me/TheRiZoeL"
                    ),
                    InlineKeyboardButton(
                        "✙ᴀᴅᴅ ᴍᴇ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ✙", url="https://t.me/RiZoeLvcBoT?startgroup=true"
                    )
                ]
            ]
        )
    )

    
