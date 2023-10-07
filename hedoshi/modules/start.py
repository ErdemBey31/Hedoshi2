# Copyright (C) 2023 frknkrc44 <https://gitlab.com/frknkrc44>
#
# This file is part of HedoshiMusicBot project,
# and licensed under GNU Affero General Public License v3.
# See the GNU Affero General Public License for more details.
#
# All rights reserved. See COPYING, AUTHORS.

from pyrogram.types import Message
from ..helpers.telegram.cmd_register import register
from time import time
@register('start', private=True)
async def start(message: Message):
    await message.reply_photo("https://telegra.ph/file/dd3b29610f7d702500f9d.jpg", caption="""
        ** KOMUTLAR:**

        ** /play - Müzik oynatır, bir dosyaya yanıt veya bir müzik adı**
        ** /vplay - Videolu oynat **
        ** /end - Bitir**
        ** /skip - Sonraki müziğe geç**
        ** /seek-[ileri,geri] - Buraya yazılan saniye kadar ileri sarar**
        ** /ping - pingi ölçmek**
        ** /pause - durdur**
        ** /resume - devam et**
        ** /loop - döngü**
        ** /leave - sesliden ayrıl**
        ** /query - Oynatılan müziği göster(Not: ismin sonunda ki -a şarkı -v video demektir)**
        ** GÜNCELLEME KANALINA KATIL @username**""")
