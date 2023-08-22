# Copyright (C) 2023 frknkrc44 <https://gitlab.com/frknkrc44>
#
# This file is part of HedoshiMusicBot project,
# and licensed under GNU Affero General Public License v3.
# See the GNU Affero General Public License for more details.
#
# All rights reserved. See COPYING, AUTHORS.
#

from pyrogram.types import Message
from ..helpers.telegram.cmd_register import register
from time import time


@register('start|baslat|alive', private=True, owner=True)
async def ping(message: Message) -> None:    
    await message.reply_text('''**Merhaba sayın yöneticim❤️, **\n\n__Şuan da aktif olarak çalışıyorum__''')
''')
    
