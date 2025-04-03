from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

check = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="✅ Obuna bo‘lish", url="https://t.me/nur02_17")],
        [InlineKeyboardButton(text="🔄 Tekshirish", callback_data="Tekshirish")]
    ]
)
