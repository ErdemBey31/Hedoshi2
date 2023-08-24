# Copyright (C) 2023 frknkrc44 <https://gitlab.com/frknkrc44>
#
# This file is part of HedoshiMusicBot project,
# and licensed under GNU Affero General Public License v3.
# See the GNU Affero General Public License for more details.
#
# All rights reserved. See COPYING, AUTHORS.
from pyrogram import Client, CallbackQuery
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram import filters
from time import time
from ..helpers.telegram.cmd_register import register

@register('start', private=True)
async def start(message: Message):
    buttons = [
        [InlineKeyboardButton("KOMUTLAR ✨", callback_data="show_commands")]
    ]

    await message.reply_text(
        "__Merhaba, Müzik Botuna hoş geldiniz! Komutlarım aşağıdaki butondan görülebilir.__",
        reply_markup=InlineKeyboardMarkup(buttons)
    )


@Client.on_callback_query(filters.regex("show_commands"))
async def show_commands(_, query: CallbackQuery):
    await query.edit_message_text(
        """
        ** KOMUTLAR:**

        ** /play - Müzik oynatır, bir dosyaya yanıt veya bir müzik adı**
        ** /vplay - Videolu oynat **
        ** /end - Bitir**
        ** /skip - Sonraki müziğe geç**
        ** /seek - Buraya yazılan saniye kadar ileri sarar**
        ** /ping - pingi ölçmek**
        ** /pause - durdur**
        ** /resume - devam et**
        ** /loop - döngü**
        ** /leave - sesliden ayrıl**
        ** /query - Oynatılan müziği göster(Not: ismin sonunda ki -a şarkı -v video demektir)**
        ** GÜNCELLEME KANALINA KATIL @ruyamuzikguncelleme**
        """,
        reply_markup=InlineKeyboardMarkup([[
            InlineKeyboardButton("Geri 🔙", callback_data="back_to_start")
        ]])
    )


@Client.on_callback_query(filters.regex("back_to_start"))
async def back_to_start(_, query: CallbackQuery):
    await start(query.message)
