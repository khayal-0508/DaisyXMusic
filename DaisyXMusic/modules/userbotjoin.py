# Daisyxmusic (Telegram bot project )
# Copyright (C) 2021  Inukaasith

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
from pyrogram.errors import UserAlreadyParticipant
import asyncio
from DaisyXMusic.helpers.decorators import authorized_users_only, errors
from DaisyXMusic.services.callsmusic.callsmusic import client as USER
from DaisyXMusic.config import SUDO_USERS

@Client.on_message(filters.command(["userbotjoin"]) & ~filters.private & ~filters.bot)
@authorized_users_only
@errors
async def addchannel(client, message):
    chid = message.chat.id
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        await message.reply_text(
            "<b>İlk olaraq məni qrupda admin edin</b>",
        )
        return

    try:
        user = await USER.get_me()
    except:
        user.first_name = "Khan Music Bot"

    try:
        await USER.join_chat(invitelink)
        await USER.send_message(message.chat.id, "Tələbinizə uyğun olaraq qrupa qatıldım")
    except UserAlreadyParticipant:
        await message.reply_text(
            "<b>Assistant qrupunuza qoşuldu</b>",
        )
    except Exception as e:
        print(e)
        await message.reply_text(
            f"<b>🔴 Flood Wait Xətası 🔴 \nƏziz {user.first_name} assistant sizdən asılı olan səbəblərə görə qrupa qoşula bilmədi! Assistantın qrupdan çıxarılmadığını(ban olunmadığını) yoxlayın."
            "\n\nvə ya @KhanMusicAssistant -ı əl ilə əlavə edin</b>",
        )
        return
    await message.reply_text(
        "<b>Assistant qrupa qoşuldu</b>",
    )


@USER.on_message(filters.group & filters.command(["userbotleave"]))
@authorized_users_only
async def rem(USER, message):
    try:
        await USER.leave_chat(message.chat.id)
    except:
        await message.reply_text(
            f"<b>Assistant qrupdan çıxa bilmədi! Flood Wait ola bilər."
            "\n\nban verərək qrupdan ata bilərsiniz.</b>",
        )
        return
    
@Client.on_message(filters.command(["userbotleaveall"]))
async def bye(client, message):
    if message.from_user.id in SUDO_USERS:
        left=0
        failed=0
        lol = await message.reply("Assistant bütün qruplardan çıxdı")
        async for dialog in USER.iter_dialogs():
            try:
                await USER.leave_chat(dialog.chat.id)
                left = left+1
                await lol.edit(f"Assistant çıxır... Left: {left} chats. Failed: {failed} chats.")
            except:
                failed=failed+1
                await lol.edit(f"Assistant leaving... Left: {left} chats. Failed: {failed} chats.")
            await asyncio.sleep(0.7)
        await client.send_message(message.chat.id, f"Left {left} chats. Failed {failed} chats.")
    
    
@Client.on_message(filters.command(["userbotjoinchannel","ubjoinc"]) & ~filters.private & ~filters.bot)
@authorized_users_only
@errors
async def addcchannel(client, message):
    try:
      conchat = await client.get_chat(message.chat.id)
      conid = conchat.linked_chat.id
      chid = conid
    except:
      await message.reply("Is chat even linked")
      return    
    chat_id = chid
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        await message.reply_text(
            "<b>Məni qrupda admin edin</b>",
        )
        return

    try:
        user = await USER.get_me()
    except:
        user.first_name = "Khan Music Bot"

    try:
        await USER.join_chat(invitelink)
        await USER.send_message(message.chat.id, "İstəyinizə uyğun olaraq qrupa qatıldım")
    except UserAlreadyParticipant:
        await message.reply_text(
            "<b>Assistant qrupa qatıldı</b>",
        )
        return
    except Exception as e:
        print(e)
        await message.reply_text(
            f"<b>🔴 Flood Wait Xətası 🔴 \nƏziz {user.first_name} assistant sizdən asılı olan səbəblərə görə qrupa qoşula bilmədi! Assistantın qrupdan çıxarılmadığını(ban olunmadığını) yoxlayın."
            "\n\nvə ya @KhanMusicAssistant -ı əl ilə əlavə edin </b>",
        )
        return
    await message.reply_text(
        "<b>Assistant kanala qatıldı</b>",
    )
    
