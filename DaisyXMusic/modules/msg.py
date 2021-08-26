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

import os
from DaisyXMusic.config import SOURCE_CODE,ASSISTANT_NAME,PROJECT_NAME,SUPPORT_GROUP,UPDATES_CHANNEL
class Messages():
      START_MSG = "**Salam 👋 [{}](tg://user?id={})!**\n\n🤖 Mən @tag1y3v tərəfindən Telegram səsli söhbətlərdə musiqi çalmaq üçün yaradılmış bir botam.\n\n✅ Daha çox məlumat üçün /help yazın."
      HELP_MSG = [
        ".",
f"""
**Hey 👋 {PROJECT_NAME} -a yenidən xoş gəldiniz

⚪️ {PROJECT_NAME} qrupunuzun səsli söhbətində musiqi çalmaq üçündür

⚪️ Assistant adı >> @{ASSISTANT_NAME}\n\nTəlimatlar üçün növbəti düyməsini basın**
""",

f"""
**Quraşdırmaq**

1) Botu qrupda admin edin.
2) Səsli söhbət başladın.
3) Bir admin tərəfindən /play [musiqi adı] əmrini işlədin
*) Assistant qoşulubsa musiqidən zövq alın, @{ASSISTANT_NAME} qoşulmasa yenidən cəhd edin və ya @tag1y3v ilə əlaqəyə keçin.

**Əmrlər**

**=>> Oxutmaq 🎧**

- /play: İstədiyiniz musiqini səsləndirmək
- /play [yt url] : Verdiyiniz linki səsləndirmək
- /play [reply yo audio]: Yanıt verdiyiniz faylı səsləndirmək
- /ytplay: Youtube Music vasitəsilə birbaşa səsləndirmək

**=>> İdarəetmə ⏯**

- /player: Parametrlər menyusunu açmaq
- /skip: Oxunan musiqinu dəyişdirmək
- /pause: Pause vermək
- /resume: Davam etdirmək
- /end: Musiqi axınını dayandırmaq
- /current: Oxunan mahnını göstərmək
- /playlist: Playlistə baxmaq

*Player cmd və /play, /current, /playlist  istisna olmaqla digər əmrlər qrup adminləri üçündür.
""",
        
f"""

""",

f"""
**=>> Daha çox 🧑‍🔧**

- /musicplayer [on/off]: Playeri aktiv/deaktiv etmək
- /admincache: Admin listi yeniləmək.
- /userbotjoin: @{ASSISTANT_NAME} -u qrupa əlavə etmək

**=>> Bot sahibləri(Sudo Users) üçün əmrlər ⚔️**

 - /userbotleaveall - Assistantı bütün qruplardan çıxarmaq
 - /gcast <reply to message> - Bütün qruplara qlobal mesaj vermək
 - /pmpermit [on/off] - pmpermit açmaq/bağlamaq
*Sudo Users istənilən qrupda istənilən əmrləri yerinə yetirə bilərlər

"""
      ]
