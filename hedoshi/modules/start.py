@register('start', private=True)
async def start(message: Message):


buttons = [[
    InlineKeyboardButton("Komutları Göster", callback_data="show_commands") 
],
]

await message.reply_text(
    "__Merhaba, Müzik Botuna hoş geldiniz! Komutlarım aşağıdaki butondan görülebilir.__",
    reply_markup=InlineKeyboardMarkup(buttons)
)


@callback_query_handler(func=lambda call: call.data == "show_commands")
async def show_commands(call: CallbackQuery):


await call.message.edit_text(    """
   ** KOMUTLAR:**
    
    **/play - Müzik oynatır, bir dosyaya yanıt veya bir müzik adı**
    **/vplay - Videolu oynat **
   ** /end - Bitir**
   ** /skip - Sonraki müziğe geç**
   ** /seek - Buraya yazılan saniye kadar ileri sarar**
   ** /ping - pingi ölçmek**
   ** /pause - durdur**
  **  /resume - devam et**
  **  /loop - döngü**
   ** /leave - sesliden ayrıl**
   ** /query - Oynatılan müziği göster(Not: ismin sonunda ki -a şarkı -v video demektir)**
   ** GÜNCELLEME KANALINA KATIL @ruyamuzikguncelleme**
    """,
    reply_markup=InlineKeyboardMarkup([[
        InlineKeyboardButton("Geri 🔙", callback_data="back_to_start") 
    ]])


)

@callback_query_handler(func=lambda call: call.data == "back_to_start")\
async def back_to_start(call: CallbackQuery):

await start(call.message)
