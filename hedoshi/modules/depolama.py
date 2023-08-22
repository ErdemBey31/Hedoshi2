import subprocess


# Copyright (C) 2023 frknkrc44 <https://gitlab.com/frknkrc44>
#
# This file is part of HedoshiMusicBot project,
# and licensed under GNU Affero General Public License v3.
# See the GNU Affero General Public License for more details.
#
# All rights reserved. See COPYING, AUTHORS.
# n

from pyrogram.types import Message
from ..helpers.telegram.cmd_register import register
from time import time


@register('run|calistir|komut', owner=True)
async def ping(message: Message) -> None:
    try:
      output = subprocess.check_output(message.command[1:]).decode('utf-8')
      await message.reply_text(f"<code>{output}</code>")
    except Exception as e:
      await message.reply_text(f"**HATA:⛔⛔**\n\n`{e}`")
