@register('start', private=True)
async def start(message: Message):

```
buttons = [[
    InlineKeyboardButton("Komutları Göster", callback_data="show_commands") 
],
]

await message.reply_text(
    "Merhaba, Müzik Bot'a hoş geldiniz!",
    reply_markup=InlineKeyboardMarkup(buttons)
)
```

@callback_query_handler(func=lambda call: call.data == "show_commands")
async def show_commands(call: CallbackQuery):

```
await call.message.edit_text(    """
    Komutlar:
    
    /play - Müzik oynat
    /vplay - Video oynat
    ...
    
    Geri dönmek için 'Geri' butonuna basın
    """,
    reply_markup=InlineKeyboardMarkup([[
        InlineKeyboardButton("Geri", callback_data="back_to_start") 
    ]])
```

)

@callback_query_handler(func=lambda call: call.data == "back_to_start")\
async def back_to_start(call: CallbackQuery):

await start(call.message)