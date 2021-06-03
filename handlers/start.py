from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_sticker("CAACAgUAAxkBAAEKLOFgtzauneaP6WbcRfJlPMvPz_CCLgAC0AIAAvbj0VQ6KQtObIJRdR8E")
    await message.reply_text(
        f"""<b>Hey {message.from_user.first_name}!
\nI can play music in your group's voice chat
And Also I Can Manage Ur Group.. ❤️
\nUse the buttons below to know more about me.
\nContact my owner :- @TheRiZoeL
 </b>""",


        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " RɪZᴏᴇL 🖤", url="https://t.me/TheRiZoeL"
                    ),
                    InlineKeyboardButton(
                        " Assistant 😌 ", url="https://t.me/RiZoeL_VC?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Aᴅᴅ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴘ ➕", url="https://t.me/RiZoeLvcBoT?startgroup=true"
                    )
                ]
            ]
        )
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**ʜᴇʏ ɪ'ᴍ ᴀʟɪᴠᴇ ✌️ ᴀɴᴅ ʀᴇᴀᴅʏ ᴛᴏ ᴘʟᴀʏ ᴍᴜsɪᴄ ғᴏʀ ʏᴏᴜ🎛️**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " ViBes Channel ☺️", url="https://t.me/REALVIBESn"
                    )
                ],[
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


@Client.on_message(
    filters.command("help")
    & filters.private
    & ~ filters.edited
)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""<b>Here Is Cmd Of RiZoeL_MuSic !
╔━━━━━━━━⊰✦⊱━━━━━━━━╗
\n/play <song name> - play song you requested
/dplay <song name> - play song you requested via deezer
/splay <song name> - play song you requested via jio saavn
/playlist - Show now playing list
/current - Show now playing
/song <song name> - download songs you want quickly
/search <query> - search videos on youtube with details
/deezer <song name> - download songs you want quickly via deezer
/saavn <song name> - download songs you want quickly via saavn
/video <song name> - download videos you want quickly
\n*Admins only*
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
                        " ⚫ Channel", url="https://t.me/REALVIBESn"
                   ),
                    InlineKeyboardButton(
                        " Aᴅᴅ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴘ ➕", url="https://t.me/RiZoeLvcBoT?startgroup=true"
                    )
                ]
            ]
        )
    )
