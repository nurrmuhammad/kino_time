import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message
from buttons import check

BOT_TOKEN = ""
CHANNELS = []  # Kanal nomlari
CHAT_ID = 
logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


# /start komandasi
@dp.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(
        "Botdan foydalanish uchun quyidagi kanallarga obuna bo'ling! 👇",
        reply_markup=check
    )


# Obuna tekshirish funksiyasi
async def is_user_subscribed(user_id: int, bot: Bot) -> bool:
    for channel in CHANNELS:
        try:
            member = await bot.get_chat_member(chat_id=channel, user_id=user_id)
            if member.status not in ["member", "administrator", "creator"]:
                return False
        except Exception as e:
            logging.error(f"Xatolik: {e}")
            return False

        except Exception as e:
            logging.error(f"Error checking subscription: {e}")
            return False
    return True


# 🔄 Tekshirish tugmasi
from aiogram.exceptions import TelegramBadRequest

from aiogram.exceptions import TelegramBadRequest

@dp.callback_query(F.data == "Tekshirish")
async def check_subscription(callback: CallbackQuery):
    user_id = callback.from_user.id

    if await is_user_subscribed(user_id, bot):
        # Obuna bo‘lgan bo‘lsa — yangi xabar bilan bildirish
        await callback.message.delete()
        await callback.message.answer("✅ Siz kanalga obuna bo‘lgansiz! Endi botdan foydalanishingiz mumkin.\nkino kodini yozing.")
    else:
        # Obuna bo‘lmagan bo‘lsa — alert ko‘rsatish
        await callback.answer("❌ Siz hali kanalga obuna bo‘lmagansiz!", show_alert=True)
        # Tugmalarni yangilashga harakat qilamiz
        try:
            await callback.message.edit_reply_markup(reply_markup=check)
        except TelegramBadRequest as e:
            if "message is not modified" not in str(e):
                raise e



# Video qabul qilish
@dp.message(F.video)
async def receive_video(message: Message):
    file_id = message.video.file_id
    await message.answer(f"Video file_id -> {file_id}")


# "252" deb yozganda kino yuborish
@dp.message(F.text == "252")
async def send_video(message: Message):
    try:
        user_status = await bot.get_chat_member(chat_id=CHAT_ID, user_id=message.from_user.id)
        if user_status.status in ["member", "administrator", "creator"]:
            file_id = "BAACAgQAAxkBAAIFJmdIlLf6GzPTOy65JGAJ5aglI0frAAKAGAACINvoUD03nXx51VPENgQ"
            await message.answer_video(
                video=file_id,
                caption="""
#🍿| Kino Nomi: Venom 3
➖➖➖➖➖➖➖➖➖➖➖➖
🇺🇿| Tili: O'zbek tilida
💾| Sifati: Ts format 
🎞️| Janri: Jangari
⛔️| Ko'rish Kategoriyasi: 18+

🔰| Kanal: @nur02_16
🗂 Yuklash: 5903

🤖 Bizning bot: @news4sd_bot
                """
            )
        else:
            await message.answer(
                "⚠️ Siz kanalga obuna bo'lmagansiz! Obuna bo‘lib, qayta urinib ko‘ring.",
                reply_markup=check
            )
    except Exception as e:
        await message.answer("❌ Xatolik yuz berdi. Keyinroq urinib ko‘ring.")
        logging.error(f"Error in video sending: {e}")

# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
@dp.message(F.text == "552")
async def send_video(message: Message):
    print(f"Foydalanuvchi:Farsaj 10")
    try:
        user_status = await bot.get_chat_member(chat_id=CHAT_ID, user_id=message.from_user.id)
        if user_status.status in ["member", "administrator", "creator"]:
            file_id = "BAACAgQAAxkBAAMeZzb0WXQ7eUYVVieCg8OQpuKyfooAAikSAALUzxlRhiosmcCQgvk2BA"
            await message.answer_video(video=file_id,
                                       caption="#🍿|🎬 Kinoni Nomi:Farsaj 10\n➖➖➖➖➖➖➖➖➖➖➖➖\n🇺🇿| Tili: O'zbek tilida\n💾| Sifati: Ts format \n🎞️| Janri: Jangari\n⛔️| Ko'rish Kategoriyasi: 18+\n\n🔰| Kanal: @nur02_16\n🗂 Yuklash: 5903\n\n🤖 Bizning bot: @news4sd_bot"
                                       )
        else:
            await message.answer(
                "⚠️ Siz kanalga obuna bo'lmagansiz! Kanalga obuna bo'ling va qayta urinib ko'ring.",
                reply_markup=check
            )
    except Exception as e:
        await message.answer("❌ Xatolik yuz berdi. Iltimos, qayta urinib ko'ring.")
        logging.error(f"Error in video sending: {e}")


# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
@dp.message(F.text == "551")
async def send_video(message: Message):
    print(f"Foydalanuvchi: Transformerlar muqaddima")
    try:
        user_status = await bot.get_chat_member(chat_id=CHAT_ID, user_id=message.from_user.id)
        if user_status.status in ["member", "administrator", "creator"]:
            file_id = "BAACAgIAAxkBAAMpZzclZE_bCMWBjGKGSTVtGdk6zvYAAmpZAAJIR1BI_ESDx_fSRt02BA"
            await message.answer_video(video=file_id,
                                       caption="🎬Nomi: Transformerlar muqaddima\n➖➖➖➖➖➖➖➖➖➖➖➖\n🇺🇿| Tili: O'zbek tilida\n💾| Sifati: Ts format \n🎞️| Janri: Jangari\n⛔️| Ko'rish Kategoriyasi: 18+\n\n🔰| Kanal: @nur02_16\n🗂 Yuklash: 5903\n\n🤖 Bizning bot: @news4sd_bot"
                                       )
        else:
            await message.answer(
                "⚠️ Siz kanalga obuna bo'lmagansiz! Kanalga obuna bo'ling va qayta urinib ko'ring.",
                reply_markup=check
            )
    except Exception as e:
        await message.answer("❌ Xatolik yuz berdi. Iltimos, qayta urinib ko'ring.")
        logging.error(f"Error in video sending: {e}")


# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
@dp.message(F.text == "4")
async def send_video(message: Message):
    print(f"Foydalanuvchi: YENGILMAS GVARDIYA ")
    try:
        user_status = await bot.get_chat_member(chat_id=CHAT_ID, user_id=message.from_user.id)
        if user_status.status in ["member", "administrator", "creator"]:
            file_id = "BAACAgQAAxkBAAMrZzcmFE9ZtMCyZvHZxsSGrDOTHkkAAvcaAAL4c1lQF4DF0zAkr9k2BA"
            await message.answer_video(video=file_id,
                                       caption="🎬 KinoniNomi: YENGILMAS GVARDIYA\n➖➖➖➖➖➖➖➖➖➖➖➖\n🇺🇿| Tili: O'zbek tilida\n💾| Sifati: Ts format \n🎞️| Janri: Jangari\n⛔️| Ko'rish Kategoriyasi: 18+\n\n🔰| Kanal:@nur02_16\n🗂 Yuklash: 5903\n\n🤖 Bizning bot: @news4sd_bot"
                                       )
        else:
            await message.answer(
                "⚠️ Siz kanalga obuna bo'lmagansiz! Kanalga obuna bo'ling va qayta urinib ko'ring.",
                reply_markup=check
            )
    except Exception as e:
        await message.answer("❌ Xatolik yuz berdi. Iltimos, qayta urinib ko'ring.")
        logging.error(f"Error in video sending: {e}")


# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
@dp.message(F.text == "261")
async def send_video(message: Message):
    print(f"Foydalanuvchi:Godzilla va Kong: Yangi imperiya")
    try:
        user_status = await bot.get_chat_member(chat_id=CHAT_ID, user_id=message.from_user.id)
        if user_status.status in ["member", "administrator", "creator"]:
            file_id = "BAACAgQAAxkBAANfZzcyHLtduU9UGg4uAV3Cafqb4P8AAtYTAALo3xlSS6VndsmZKpk2BA"
            await message.answer_video(video=file_id,
                                       caption="🎬 Nomi: Godzilla va Kong: Yangi imperiya\n➖➖➖➖➖➖➖➖➖➖➖➖\n🇺🇿| Tili: O'zbek tilida\n💾| Sifati: Ts format \n🎞️| Janri: Jangari\n⛔️| Ko'rish Kategoriyasi: 18+\n\n🔰| Kanal: @nur02_16\n🗂 Yuklash: 5903\n\n🤖 Bizning bot: @news4sd_bot"
                                       )
        else:
            await message.answer(
                "⚠️ Siz kanalga obuna bo'lmagansiz! Kanalga obuna bo'ling va qayta urinib ko'ring.",
                reply_markup=check
            )
    except Exception as e:
        await message.answer("❌ Xatolik yuz berdi. Iltimos, qayta urinib ko'ring.")
        logging.error(f"Error in video sending: {e}")


# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
@dp.message(F.text == "5")
async def send_video(message: Message):
    print(f"Foydalanuvchi: Qizil topshiriq")
    try:
        user_status = await bot.get_chat_member(chat_id=CHAT_ID, user_id=message.from_user.id)
        if user_status.status in ["member", "administrator", "creator"]:
            file_id = "BAACAgQAAxkBAANHZzcrlXtPoNZKgcn4NsDk6jcUjUcAAsUYAAJtbLFRCQ7rTs0iFpI2BA"
            await message.answer_video(video=file_id,
                                       caption="🎬 Nomi: Qizil topshiriq\n➖➖➖➖➖➖➖➖➖➖➖➖\n🇺🇿| Tili: O'zbek tilida\n💾| Sifati: Ts format \n🎞️| Janri: Jangari\n⛔️| Ko'rish Kategoriyasi: 18+\n\n🔰| Kanal: @nur02_16\n🗂 Yuklash: 5903\n\n🤖 Bizning bot: @news4sd_bot"
                                       )
        else:
            await message.answer(
                "⚠️ Siz kanalga obuna bo'lmagansiz! Kanalga obuna bo'ling va qayta urinib ko'ring.",
                reply_markup=check
            )
    except Exception as e:
        await message.answer("❌ Xatolik yuz berdi. Iltimos, qayta urinib ko'ring.")
        logging.error(f"Error in video sending: {e}")


# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
@dp.message(F.text == "3")
async def send_video(message: Message):
    print(f"Foydalanuvchi:Arvox poygach")
    try:
        user_status = await bot.get_chat_member(chat_id=CHAT_ID, user_id=message.from_user.id)
        if user_status.status in ["member", "administrator", "creator"]:
            file_id = "BAACAgQAAxkBAAMtZzcnEKYBGJh4LJ4TlnWeHJazU5oAAhcIAAKcSUhTe9ZiSHRi-a02BA"
            await message.answer_video(video=file_id,
                                       caption="🎬Kino kodi:Arvox poygach\n➖➖➖➖➖➖➖➖➖➖➖➖\n🇺🇿| Tili: O'zbek tilida\n💾| Sifati: Ts format \n🎞️| Janri: Jangari\n⛔️| Ko'rish Kategoriyasi: 18+\n\n🔰| Kanal: @nur02_16\n🗂 Yuklash: 5903\n\n🤖 Bizning bot: @news4sd_bot"
                                       )
        else:
            await message.answer(
                "⚠️ Siz kanalga obuna bo'lmagansiz! Kanalga obuna bo'ling va qayta urinib ko'ring.",
                reply_markup=check
            )
    except Exception as e:
        await message.answer("❌ Xatolik yuz berdi. Iltimos, qayta urinib ko'ring.")
        logging.error(f"Error in video sending: {e}")


# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
@dp.message(F.text == "8")
async def send_video(message: Message):
    print(f"Foydalanuvchi: Qora pantera 2: vakanda abadiy")
    try:
        user_status = await bot.get_chat_member(chat_id=CHAT_ID, user_id=message.from_user.id)
        if user_status.status in ["member", "administrator", "creator"]:
            file_id = "BAACAgQAAxkBAANhZzc0GEjrs85eSa4flc8DsnMsld8AAjUTAAI0-rBQ4yTu77Fox_Y2BA"
            await message.answer_video(video=file_id,
                                       caption="🎬 Nomi: Qora pantera 2: vakanda abadiy\n➖➖➖➖➖➖➖➖➖➖➖➖\n🇺🇿| Tili: O'zbek tilida\n💾| Sifati: Ts format (Film rus tilida tepada adashib ketibmiz)\n🎞️| Janri: Jangari\n⛔️| Ko'rish Kategoriyasi: 18+\n\n🔰| Kanal:@nur02_16\n🗂 Yuklash: 5903\n\n🤖 Bizning bot: @news4sd_bot"
                                       )
        else:
            await message.answer(
                "⚠️ Siz kanalga obuna bo'lmagansiz! Kanalga obuna bo'ling va qayta urinib ko'ring.",
                reply_markup=check
            )
    except Exception as e:
        await message.answer("❌ Xatolik yuz berdi. Iltimos, qayta urinib ko'ring.")
        logging.error(f"Error in video sending: {e}")


# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
@dp.message(F.text == "6")
async def send_video(message: Message):
    print(f"Foydalanuvchi: O'G'RILAR ARMIYASI ")
    try:
        user_status = await bot.get_chat_member(chat_id=CHAT_ID, user_id=message.from_user.id)
        if user_status.status in ["member", "administrator", "creator"]:
            file_id = "BAACAgEAAxkBAANlZzc8BIYfXLnSzHXdp_lz3e-w9RQAApMCAAKQonFESBkbmqC9Rj02BA"
            await message.answer_video(video=file_id,
                                       caption="🎬 O'G'RILAR ARMIYASI \n➖➖➖➖➖➖➖➖➖➖➖➖\n🇺🇿| Tili: O'zbek tilida\n💾| Sifati: Ts format \n🎞️| Janri: Jangari\n⛔️| Ko'rish Kategoriyasi: 18+\n\n🔰| Kanal: @nur02_16\n🗂 Yuklash: 5903\n\n🤖 Bizning bot: @news4sd_bot"
                                       )
        else:
            await message.answer(
                "⚠️ Siz kanalga obuna bo'lmagansiz! Kanalga obuna bo'ling va qayta urinib ko'ring.",
                reply_markup=check
            )
    except Exception as e:
        await message.answer("❌ Xatolik yuz berdi. Iltimos, qayta urinib ko'ring.")
        logging.error(f"Error in video sending: {e}")


# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
@dp.message(F.text == "10")
async def send_video(message: Message):
    print(f"Foydalanuvchi:Ajdar Makoni ")
    try:
        user_status = await bot.get_chat_member(chat_id=CHAT_ID, user_id=message.from_user.id)
        if user_status.status in ["member", "administrator", "creator"]:
            file_id = "BAACAgIAAxkBAANrZzdDRnazSd9hyzYjmufkgel5-CEAAnkOAAJO00FJE6JIAAFkuo1aNgQ"
            await message.answer_video(video=file_id,
                                       caption="🎬 Ajdar Makoni \n➖➖➖➖➖➖➖➖➖➖➖➖\n🇺🇿| Tili: O'zbek tilida\n💾| Sifati: Ts format \n🎞️| Janri: Jangari\n⛔️| Ko'rish Kategoriyasi: 18+\n\n🔰| Kanal: @nur02_16\n🗂 Yuklash: 5903\n\n🤖 Bizning bot: @news4sd_bot"
                                       )
        else:
            await message.answer(
                "⚠️ Siz kanalga obuna bo'lmagansiz! Kanalga obuna bo'ling va qayta urinib ko'ring.",
                reply_markup=check
            )
    except Exception as e:
        await message.answer("❌ Xatolik yuz berdi. Iltimos, qayta urinib ko'ring.")
        logging.error(f"Error in video sending: {e}")


# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
@dp.message(F.text == "11")
async def send_video(message: Message):
    print(f"Foydalanuvchi:Anakonda 4")
    try:
        user_status = await bot.get_chat_member(chat_id=CHAT_ID, user_id=message.from_user.id)
        if user_status.status in ["member", "administrator", "creator"]:
            file_id = "BAACAgEAAxkBAAOxZzd4u0MDVgrV3QHwzujBs6wQeT8AAmkCAAKsNUhHKl8ndP4LOvA2BA"
            await message.answer_video(video=file_id,
                                       caption="🎬 Anakonda 4\n➖➖➖➖➖➖➖➖➖➖➖➖\n🇺🇿| Tili: O'zbek tilida\n💾| Sifati: Ts format\n🎞️| Janri: Jangari\n⛔️| Ko'rish Kategoriyasi: 18+\n\n🔰| Kanal: @nur02_16\n🗂 Yuklash: 5903\n\n🤖 Bizning bot: @news4sd_bot"
                                       )
        else:
            await message.answer(
                "⚠️ Siz kanalga obuna bo'lmagansiz! Kanalga obuna bo'ling va qayta urinib ko'ring.",
                reply_markup=check
            )
    except Exception as e:
        await message.answer("❌ Xatolik yuz berdi. Iltimos, qayta urinib ko'ring.")
        logging.error(f"Error in video sending: {e}")


# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
@dp.message(F.text == "12")
async def send_video(message: Message):
    print(f"Foydalanuvchi:𝗠𝘂𝗾𝗮𝗱𝗱𝗮𝘀 𝗭𝗮𝗺𝗶𝗻")
    try:
        user_status = await bot.get_chat_member(chat_id=CHAT_ID, user_id=message.from_user.id)
        if user_status.status in ["member", "administrator", "creator"]:
            file_id = "BAACAgQAAxkBAAOzZzd5gT2HnfQAAdHLY13rZzQZ8jJKAAIWEAACTLnhUaqgXB8rJcM-NgQ"
            await message.answer_video(video=file_id,
                                       caption="🎬𝗠𝘂𝗾𝗮𝗱𝗱𝗮𝘀 𝗭𝗮𝗺𝗶𝗻\n➖➖➖➖➖➖➖➖➖➖➖➖\n🇺🇿| Tili: O'zbek tilida\n💾| Sifati: Ts format\n🎞️| Janri: Jangari\n⛔️| Ko'rish Kategoriyasi: 18+\n\n🔰| Kanal: @nur02_16\n🗂 Yuklash: 5903\n\n🤖 Bizning bot: @news4sd_bot"
                                       )
        else:
            await message.answer(
                "⚠️ Siz kanalga obuna bo'lmagansiz! Kanalga obuna bo'ling va qayta urinib ko'ring.",
                reply_markup=check
            )
    except Exception as e:
        await message.answer("❌ Xatolik yuz berdi. Iltimos, qayta urinib ko'ring.")
        logging.error(f"Error in video sending: {e}")


# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
@dp.message(F.text == "13")
async def send_video(message: Message):
    print(f"Foydalanuvchi:Yomon yigitlar (2022)")
    try:
        user_status = await bot.get_chat_member(chat_id=CHAT_ID, user_id=message.from_user.id)
        if user_status.status in ["member", "administrator", "creator"]:
            file_id = "BAACAgEAAxkBAAO3Zzd65z6YVqe3tQO2ZelxgyemOc4AAoICAAJRwwlEIikmh-m2ft42BA"
            await message.answer_video(video=file_id,
                                       caption="🎬Yomon yigitlar (2022)\n➖➖➖➖➖➖➖➖➖➖➖➖\n🇺🇿| Tili: O'zbek tilida\n💾| Sifati: Ts format \n🎞️| Janri: Jangari\n⛔️| Ko'rish Kategoriyasi: 18+\n\n🔰| Kanal: @nur02_16\n🗂 Yuklash: 5903\n\n🤖 Bizning bot: @news4sd_bot"
                                       )
        else:
            await message.answer(
                "⚠️ Siz kanalga obuna bo'lmagansiz! Kanalga obuna bo'ling va qayta urinib ko'ring.",
                reply_markup=check
            )
    except Exception as e:
        await message.answer("❌ Xatolik yuz berdi. Iltimos, qayta urinib ko'ring.")
        logging.error(f"Error in video sending: {e}")


# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
@dp.message(F.text == "14")
async def send_video(message: Message):
    print(f"Foydalanuvchi:Kevin Durand")
    try:
        user_status = await bot.get_chat_member(chat_id=CHAT_ID, user_id=message.from_user.id)
        if user_status.status in ["member", "administrator", "creator"]:
            file_id = "BAACAgQAAxkBAAO5Zzd7tMdlXt7UTYwPBGjBksx1IakAAqgOAAIlU5lSl3c1XSjzWgABNgQ"
            await message.answer_video(video=file_id,
                                       caption="🎬Kevin Durand\n➖➖➖➖➖➖➖➖➖➖➖➖\n🇺🇿| Tili: O'zbek tilida\n💾| Sifati: Ts format)\n🎞️| Janri: Jangari\n⛔️| Ko'rish Kategoriyasi: 18+\n\n🔰| Kanal:@nur02_16\n🗂 Yuklash: 5903\n\n🤖 Bizning bot: @news4sd_bot"
                                       )
        else:
            await message.answer(
                "⚠️ Siz kanalga obuna bo'lmagansiz! Kanalga obuna bo'ling va qayta urinib ko'ring.",
                reply_markup=check
            )
    except Exception as e:
        await message.answer("❌ Xatolik yuz berdi. Iltimos, qayta urinib ko'ring.")
        logging.error(f"Error in video sending: {e}")


# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
@dp.message(F.text == "15")
async def send_video(message: Message):
    print(f"Foydalanuvchi:Mexanik 2")
    try:
        user_status = await bot.get_chat_member(chat_id=CHAT_ID, user_id=message.from_user.id)
        if user_status.status in ["member", "administrator", "creator"]:
            file_id = "BAACAgQAAxkBAAIBfWc4uutnz8JA-2ST0u5XcjvnrDe0AAKSCgAC9iKhUF1mMWJhLbM0NgQ"
            await message.answer_video(video=file_id,
                                       caption="🎬Mexanik 2\n➖➖➖➖➖➖➖➖➖➖➖➖\n🇺🇿| Tili: O'zbek tilida\n💾| Sifati: Ts format)\n🎞️| Janri: Jangari\n⛔️| Ko'rish Kategoriyasi: 18+\n\n🔰| Kanal: @nur02_16\n🗂 Yuklash: 5903\n\n🤖 Bizning bot: @news4sd_bot"
                                       )
        else:
            await message.answer(
                "⚠️ Siz kanalga obuna bo'lmagansiz! Kanalga obuna bo'ling va qayta urinib ko'ring.",
                reply_markup=check
            )

    except Exception as e:
        await message.answer("❌ Xatolik yuz berdi. Iltimos, qayta urinib ko'ring.")
        logging.error(f"Error in video sending: {e}")


# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
@dp.message(F.text == "16")
async def send_video(message: Message):
    print(f"Foydalanuvchi:JANNAT ONALAR OYOG'I OSTIDA")
    try:
        user_status = await bot.get_chat_member(chat_id=CHAT_ID, user_id=message.from_user.id)
        if user_status.status in ["member", "administrator", "creator"]:
            file_id = "BAACAgIAAxkBAAIBhWc4wAtjMmeSoZeiL0azIC2U6PCQAAIMZQACC7YJSewG_S3PsPlKNgQ"
            await message.answer_video(video=file_id,
                                       caption="🎬 JANNAT ONALAR OYOG'I OSTIDA \n➖➖➖➖➖➖➖➖➖➖➖➖\n🇺🇿| Tili: O'zbek tilida\n💾| Sifati: Ts format)\n🎞️| Janri: Jangari\n⛔️| Ko'rish Kategoriyasi: 18+\n\n🔰| Kanal: @nur02_16\n🗂 Yuklash: 5903\n\n🤖 Bizning bot: @news4sd_bot"
                                       )
        else:
            await message.answer(
                "⚠️ Siz kanalga obuna bo'lmagansiz! Kanalga obuna bo'ling va qayta urinib ko'ring.",
                reply_markup=check
            )

    except Exception as e:
        await message.answer("❌ Xatolik yuz berdi. Iltimos, qayta urinib ko'ring.")
        logging.error(f"Error in video sending: {e}")


# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
@dp.message(F.text == "17")
async def send_video(message: Message):
    print(f"Foydalanuvchi:172 kun")
    try:
        user_status = await bot.get_chat_member(chat_id=CHAT_ID, user_id=message.from_user.id)
        if user_status.status in ["member", "administrator", "creator"]:
            file_id = "BAACAgIAAxkBAAIBjmc42-snlynfRKQ8cJVI9ftMdhuKAALeYQACUAqwSZXMQNSIlEFYNgQ"
            await message.answer_video(video=file_id,
                                       caption="🎬 172 kun \n➖➖➖➖➖➖➖➖➖➖➖➖\n🇺🇿| Tili: O'zbek tilida\n💾| Sifati: Ts format)\n🎞️| Janri: Jangari\n⛔️| Ko'rish Kategoriyasi: 18+\n\n🔰| Kanal: @nur02_16\n🗂 Yuklash: 5903\n\n🤖 Bizning bot: @news4sd_bot"
                                       )
        else:
            await message.answer(
                "⚠️ Siz kanalga obuna bo'lmagansiz! Kanalga obuna bo'ling va qayta urinib ko'ring.",
                reply_markup=check
            )

    except Exception as e:
        await message.answer("❌ Xatolik yuz berdi. Iltimos, qayta urinib ko'ring.")
        logging.error(f"Error in video sending: {e}")


# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
@dp.message(F.text == "18")
async def send_video(message: Message):
    print(f"Foydalanuvchi: Kapernaum yoki ")
    try:
        user_status = await bot.get_chat_member(chat_id=CHAT_ID, user_id=message.from_user.id)
        if user_status.status in ["member", "administrator", "creator"]:
            file_id = "BAACAgQAAxkBAAIBlGc43cOOFmZY3qqQg_fiHxNbPJm3AAJpCgAC_hmBUfinHBmEQElaNgQ"
            await message.answer_video(video=file_id,
                                       caption="🎬 Kapernaum yoki (Suriyalik bolakay)\n➖➖➖➖➖➖➖➖➖➖➖➖\n🇺🇿| Tili: O'zbek tilida\n💾| Sifati: Ts format)\n🎞️| Janri: Jangari\n⛔️| Ko'rish Kategoriyasi: 18+\n\n🔰| Kanal: @nur02_16\n🗂 Yuklash: 5903\n\n🤖 Bizning bot: @news4sd_bot"
                                       )
        else:
            await message.answer(
                "⚠️ Siz kanalga obuna bo'lmagansiz! Kanalga obuna bo'ling va qayta urinib ko'ring.",
                reply_markup=check
            )

    except Exception as e:
        await message.answer("❌ Xatolik yuz berdi. Iltimos, qayta urinib ko'ring.")
        logging.error(f"Error in video sending: {e}")


# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
@dp.message(F.text == "19")
async def send_video(message: Message):
    print(f"Foydalanuvchi:Gerakl")
    try:
        user_status = await bot.get_chat_member(chat_id=CHAT_ID, user_id=message.from_user.id)
        if user_status.status in ["member", "administrator", "creator"]:
            file_id = "BAACAgEAAxkBAAIBsWc54JgaFW3PVKY3KR1GRsoGX4ukAAKVAQACA6CZRkL2V59dLofYNgQ"
            await message.answer_video(video=file_id,
                                       caption="🎬Gerakl\n➖➖➖➖➖➖➖➖➖➖➖➖\n🇺🇿| Tili: O'zbek tilida\n💾| Sifati: Ts format)\n🎞️| Janri: Jangari\n⛔️| Ko'rish Kategoriyasi: 18+\n\n🔰| Kanal: @nur02_16\n🗂 Yuklash: 5903\n\n🤖 Bizning bot: @news4sd_bot"
                                       )
        else:
            await message.answer(
                "⚠️ Siz kanalga obuna bo'lmagansiz! Kanalga obuna bo'ling va qayta urinib ko'ring.",
                reply_markup=check
            )

    except Exception as e:
        await message.answer("❌ Xatolik yuz berdi. Iltimos, qayta urinib ko'ring.")
        logging.error(f"Error in video sending: {e}")


# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
@dp.message(F.text == "78")
async def send_video(message: Message):
    print(f"Foydalanuvchi:Inson g'azabi")
    try:
        user_status = await bot.get_chat_member(chat_id=CHAT_ID, user_id=message.from_user.id)
        if user_status.status in ["member", "administrator", "creator"]:
            file_id = "BAACAgQAAxkBAAICFmc6BEZKUckme8VYNKkt_cLg3kipAALxDgACc4o5UcQ9K0JDRhbsNgQ"
            await message.answer_video(video=file_id,
                                       caption="🎬Inson g'azabi\n➖➖➖➖➖➖➖➖➖➖➖➖\n🇺🇿| Tili: O'zbek tilida\n💾| Sifati: Ts format)\n🎞️| Janri: Jangari\n⛔️| Ko'rish Kategoriyasi: 18+\n\n🔰| Kanal: @nur02_16\n🗂 Yuklash: 5903\n\n🤖 Bizning bot: @news4sd_bot"
                                       )
        else:
            await message.answer(
                "⚠️ Siz kanalga obuna bo'lmagansiz! Kanalga obuna bo'ling va qayta urinib ko'ring.",
                reply_markup=check
            )

    except Exception as e:
        await message.answer("❌ Xatolik yuz berdi. Iltimos, qayta urinib ko'ring.")
        logging.error(f"Error in video sending: {e}")


# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
@dp.message(F.text == "20")
async def send_video(message: Message):
    print(f"Foydalanuvchi:Hamma joyda")
    try:
        user_status = await bot.get_chat_member(chat_id=CHAT_ID, user_id=message.from_user.id)
        if user_status.status in ["member", "administrator", "creator"]:
            file_id = "BAACAgQAAxkBAAICRGc6KA2175mPUeiW8abOOL3IC-2zAAKQEAACL-ihUyjJssQIYPypNgQ"
            await message.answer_video(video=file_id,
                                       caption="🎬Hamma joyda\n➖➖➖➖➖➖➖➖➖➖➖➖\n🇺🇿| Tili: O'zbek tilida\n💾| Sifati: Ts format)\n🎞️| Janri: Jangari\n⛔️| Ko'rish Kategoriyasi: 18+\n\n🔰| Kanal: @nur02_16\n🗂 Yuklash: 5903\n\n🤖 Bizning bot: @news4sd_bot"
                                       )
        else:
            await message.answer(
                "⚠️ Siz kanalga obuna bo'lmagansiz! Kanalga obuna bo'ling va qayta urinib ko'ring.",
                reply_markup=check
            )

    except Exception as e:
        await message.answer("❌ Xatolik yuz berdi. Iltimos, qayta urinib ko'ring.")
        logging.error(f"Error in video sending: {e}")


# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
@dp.message(F.text == "21")
async def send_video(message: Message):
    print(f"Foydalanuvchi:Garoyib qobilyatli bolalar uyi")
    try:
        user_status = await bot.get_chat_member(chat_id=CHAT_ID, user_id=message.from_user.id)
        if user_status.status in ["member", "administrator", "creator"]:
            file_id = "BAACAgQAAxkBAAICa2c7StefmFJ2lrFy9dTfOWY-uhSFAAJ9BwACaykJUwNJWXo3uRgzNgQ"
            await message.answer_video(video=file_id,
                                       caption="🎬Garoyib qobilyatli bolalar uyi\n➖➖➖➖➖➖➖➖➖➖➖➖\n🇺🇿| Tili: O'zbek tilida\n💾| Sifati: Ts format)\n🎞️| Janri: Jangari\n⛔️| Ko'rish Kategoriyasi: 18+\n\n🔰| Kanal: @nur02_16\n🗂 Yuklash: 5903\n\n🤖 Bizning bot: @news4sd_bot"
                                       )
        else:
            await message.answer(
                "⚠️ Siz kanalga obuna bo'lmagansiz! Kanalga obuna bo'ling va qayta urinib ko'ring.",
                reply_markup=check
            )

    except Exception as e:
        await message.answer("❌ Xatolik yuz berdi. Iltimos, qayta urinib ko'ring.")
        logging.error(f"Error in video sending: {e}")


# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
@dp.message(F.text == "22")
async def send_video(message: Message):
    print(f"Foydalanuvchi:snowden")
    try:
        user_status = await bot.get_chat_member(chat_id=CHAT_ID, user_id=message.from_user.id)
        if user_status.status in ["member", "administrator", "creator"]:
            file_id = "BAACAgQAAxkBAAIEZGdDXn0xbcfquvO2bvdbmhZC40ybAAJwCgACEfIhU5YuLGYDcDcINgQ"
            await message.answer_video(video=file_id,
                                       caption="🎬Snowden\n➖➖➖➖➖➖➖➖➖➖➖➖\n🇺🇿| Tili: O'zbek tilida\n💾| Sifati: Ts format)\n🎞️| Janri: Jangari\n⛔️| Ko'rish Kategoriyasi: 18+\n\n🔰| Kanal: @nur02_16\n🗂 Yuklash: 5903\n\n🤖 Bizning bot: @news4sd_bot"
                                       )
        else:
            await message.answer(
                "⚠️ Siz kanalga obuna bo'lmagansiz! Kanalga obuna bo'ling va qayta urinib ko'ring.",
                reply_markup=check
            )

    except Exception as e:
        await message.answer("❌ Xatolik yuz berdi. Iltimos, qayta urinib ko'ring.")
        logging.error(f"Error in video sending: {e}")


# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
@dp.message(F.text == "23")
async def send_video(message: Message):
    print(f"Foydalanuvchi:samaritan ")
    try:
        user_status = await bot.get_chat_member(chat_id=CHAT_ID, user_id=message.from_user.id)
        if user_status.status in ["member", "administrator", "creator"]:
            file_id = "BAACAgQAAxkBAAIE82dHK9XBMcahUVoK155_l7IcUKrPAALZEQACedrBUkdNMacNO7k0NgQ"
            await message.answer_video(video=file_id,
                                       caption="🎬samaritan \n➖➖➖➖➖➖➖➖➖➖➖➖\n🇺🇿| Tili: O'zbek tilida\n💾| Sifati: Ts format)\n🎞️| Janri: Jangari\n⛔️| Ko'rish Kategoriyasi: 18+\n\n🔰| Kanal: @nur02_16\n🗂 Yuklash: 5903\n\n🤖 Bizning bot: @news4sd_bot"
                                       )
        else:
            await message.answer(
                "⚠️ Siz kanalga obuna bo'lmagansiz! Kanalga obuna bo'ling va qayta urinib ko'ring.",
                reply_markup=check
            )

    except Exception as e:
        await message.answer("❌ Xatolik yuz berdi. Iltimos, qayta urinib ko'ring.")
        logging.error(f"Error in video sending: {e}")


# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
@dp.message(F.text == "24")
async def send_video(message: Message):
    print(f"Foydalanuvchi:Elemental")
    try:
        user_status = await bot.get_chat_member(chat_id=CHAT_ID, user_id=message.from_user.id)
        if user_status.status in ["member", "administrator", "creator"]:
            file_id = "BAACAgQAAxkBAAIE-WdHLEBXtsYpNVa9Bd7daTvsf-ZxAAI6DgAC6zxIU9iAwVX0oR5MNgQ"
            await message.answer_video(video=file_id,
                                       caption="Elemental\n➖➖➖➖➖➖➖➖➖➖➖➖\n🇺🇿| Tili: O'zbek tilida\n💾| Sifati: Ts format)\n🎞️| Janri: Jangari\n⛔️| Ko'rish Kategoriyasi: 18+\n\n🔰| Kanal: @nur02_16\n🗂 Yuklash: 5903\n\n🤖 Bizning bot: @news4sd_bot"
                                       )
        else:
            await message.answer(
                "⚠️ Siz kanalga obuna bo'lmagansiz! Kanalga obuna bo'ling va qayta urinib ko'ring.",
                reply_markup=check
            )

    except Exception as e:
        await message.answer("❌ Xatolik yuz berdi. Iltimos, qayta urinib ko'ring.")
        logging.error(f"Error in video sending: {e}")


# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
@dp.message(F.text == "25")
async def send_video(message: Message):
    print(f"Foydalanuvchi:Qo'rquv ko'li ")
    try:
        user_status = await bot.get_chat_member(chat_id=CHAT_ID, user_id=message.from_user.id)
        if user_status.status in ["member", "administrator", "creator"]:
            file_id = "BAACAgIAAxkBAAIFCGdHNmDjMy7B4LlXA_WGN6kq53dsAAI6IgACxdhwSqVzSnKEu_0eNgQ"
            await message.answer_video(video=file_id,
                                       caption="Qo'rquv ko'li \n➖➖➖➖➖➖➖➖➖➖➖➖\n🇺🇿| Tili: O'zbek tilida\n💾| Sifati: Ts format)\n🎞️| Janri: Jangari\n⛔️| Ko'rish Kategoriyasi: 18+\n\n🔰| Kanal: @nur02_16\n🗂 Yuklash: 5903\n\n🤖 Bizning bot: @news4sd_bot"
                                       )
        else:
            await message.answer(
                "⚠️ Siz kanalga obuna bo'lmagansiz! Kanalga obuna bo'ling va qayta urinib ko'ring.",
                reply_markup=check
            )

    except Exception as e:
        await message.answer("❌ Xatolik yuz berdi. Iltimos, qayta urinib ko'ring.")
        logging.error(f"Error in video sending: {e}")


# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
@dp.message(F.text == "26")
async def send_video(message: Message):
    print(f"Foydalanuvchi:Lyusi")
    try:
        user_status = await bot.get_chat_member(chat_id=CHAT_ID, user_id=message.from_user.id)
        if user_status.status in ["member", "administrator", "creator"]:
            file_id = "BAACAgQAAxkBAAIFQGdJODxABAx-LWFcQFerNJOAvEYqAAK3BwACmmaJUSFx8MMDTKZ6NgQ"
            await message.answer_video(video=file_id,
                                       caption="Lyusi \n➖➖➖➖➖➖➖➖➖➖➖➖\n🇺🇿| Tili: O'zbek tilida\n💾| Sifati: Ts format)\n🎞️| Janri: Jangari\n⛔️| Ko'rish Kategoriyasi: 18+\n\n🔰| Kanal: @nur02_16\n🗂 Yuklash: 5903\n\n🤖 Bizning bot: @news4sd_bot"
                                       )
        else:
            await message.answer(
                "⚠️ Siz kanalga obuna bo'lmagansiz! Kanalga obuna bo'ling va qayta urinib ko'ring.",
                reply_markup=check
            )

    except Exception as e:
        await message.answer("❌ Xatolik yuz berdi. Iltimos, qayta urinib ko'ring.")
        logging.error(f"Error in video sending: {e}")


# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
@dp.message(F.text == "506")
async def send_video(message: Message):
    print(f"Foydalanuvchi:Morbius")
    try:
        user_status = await bot.get_chat_member(chat_id=CHAT_ID, user_id=message.from_user.id)
        if user_status.status in ["member", "administrator", "creator"]:
            file_id = "BAACAgQAAxkBAAIFQmdJOJBGPVlg5yNOyewnb86l-eltAAIsDAACf-IhUOgVwiQXzqSBNgQ"
            await message.answer_video(video=file_id,
                                       caption="Morbius\n➖➖➖➖➖➖➖➖➖➖➖➖\n🇺🇿| Tili: O'zbek tilida\n💾| Sifati: Ts format)\n🎞️| Janri: Jangari\n⛔️| Ko'rish Kategoriyasi: 18+\n\n🔰| Kanal: @nur02_16\n🗂 Yuklash: 5903\n\n🤖 Bizning bot: @news4sd_bot"
                                       )
        else:
            await message.answer(
                "⚠️ Siz kanalga obuna bo'lmagansiz! Kanalga obuna bo'ling va qayta urinib ko'ring.",
                reply_markup=check
            )

    except Exception as e:
        await message.answer("❌ Xatolik yuz berdi. Iltimos, qayta urinib ko'ring.")
        logging.error(f"Error in video sending: {e}")


# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
@dp.message(F.text == "27")
async def send_video(message: Message):
    print(f"Foydalanuvchi:Kingsman Maxfiy xizmat")
    try:
        user_status = await bot.get_chat_member(chat_id=CHAT_ID, user_id=message.from_user.id)
        if user_status.status in ["member", "administrator", "creator"]:
            file_id = "BAACAgQAAxkBAAIFRGdJOLg_fMa1RPXa5Z5s9Us-Bd61AAIVCAAChhQpUgRjWyGAw3_JNgQ"
            await message.answer_video(video=file_id,
                                       caption="Kingsman Maxfiy xizmat\n➖➖➖➖➖➖➖➖➖➖➖➖\n🇺🇿| Tili: O'zbek tilida\n💾| Sifati: Ts format)\n🎞️| Janri: Jangari\n⛔️| Ko'rish Kategoriyasi: 18+\n\n🔰| Kanal: @nur02_16\n🗂 Yuklash: 5903\n\n🤖 Bizning bot: @news4sd_bot"
                                       )
        else:
            await message.answer(
                "⚠️ Siz kanalga obuna bo'lmagansiz! Kanalga obuna bo'ling va qayta urinib ko'ring.",
                reply_markup=check
            )

    except Exception as e:
        await message.answer("❌ Xatolik yuz berdi. Iltimos, qayta urinib ko'ring.")
        logging.error(f"Error in video sending: {e}")


# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
@dp.message(F.text == "28")
async def send_video(message: Message):
    print(f"Foydalanuvchi:HIMOYACHILAR")
    try:
        user_status = await bot.get_chat_member(chat_id=CHAT_ID, user_id=message.from_user.id)
        if user_status.status in ["member", "administrator", "creator"]:
            file_id = "BAACAgIAAxkBAAIFRmdJOSVCvZfzREaBRT7T3fFDyj_jAAI4BwACARRwSGEvUR8RhKySNgQ"
            await message.answer_video(video=file_id,
                                       caption="HIMOYACHILAR\n➖➖➖➖➖➖➖➖➖➖➖➖\n🇺🇿| Tili: O'zbek tilida\n💾| Sifati: Ts format)\n🎞️| Janri: Jangari\n⛔️| Ko'rish Kategoriyasi: 18+\n\n🔰| Kanal: @nur02_16\n🗂 Yuklash: 5903\n\n🤖 Bizning bot: @news4sd_bot"
                                       )
        else:
            await message.answer(
                "⚠️ Siz kanalga obuna bo'lmagansiz! Kanalga obuna bo'ling va qayta urinib ko'ring.",
                reply_markup=check
            )

    except Exception as e:
        await message.answer("❌ Xatolik yuz berdi. Iltimos, qayta urinib ko'ring.")
        logging.error(f"Error in video sending: {e}")


# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
@dp.message(F.text == "577")
async def send_video(message: Message):
    print(f"Foydalanuvchi:Venom 1")
    try:
        user_status = await bot.get_chat_member(chat_id=CHAT_ID, user_id=message.from_user.id)
        if user_status.status in ["member", "administrator", "creator"]:
            file_id = "BAACAgEAAxkBAAIFUmdJQLJAT3LPtwjhShNzZm-MD5FSAAKWAQACvsrgREVza6YdX1I1NgQ"
            await message.answer_video(video=file_id,
                                       caption="Venom 1\n➖➖➖➖➖➖➖➖➖➖➖➖\n🇺🇿| Tili: O'zbek tilida\n💾| Sifati: Ts format)\n🎞️| Janri: Jangari\n⛔️| Ko'rish Kategoriyasi: 18+\n\n🔰| Kanal: @nur02_16\n🗂 Yuklash: 5903\n\n🤖 Bizning bot: @news4sd_bot"
                                       )
        else:
            await message.answer(
                "⚠️ Siz kanalga obuna bo'lmagansiz! Kanalga obuna bo'ling va qayta urinib ko'ring.",
                reply_markup=check
            )

    except Exception as e:
        await message.answer("❌ Xatolik yuz berdi. Iltimos, qayta urinib ko'ring.")
        logging.error(f"Error in video sending: {e}")


# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
@dp.message(F.text == "578")
async def send_video(message: Message):
    print(f"Foydalanuvchi:Venom 2")
    try:
        user_status = await bot.get_chat_member(chat_id=CHAT_ID, user_id=message.from_user.id)
        if user_status.status in ["member", "administrator", "creator"]:
            file_id = "BAACAgQAAxkBAAIFVGdJQLqRERPe6Y11Dsy18AhtQXwpAAJsCQAC3exJUByeVVD01elaNgQ"
            await message.answer_video(video=file_id,
                                       caption="Venom 2\n➖➖➖➖➖➖➖➖➖➖➖➖\n🇺🇿| Tili: O'zbek tilida\n💾| Sifati: Ts format)\n🎞️| Janri: Jangari\n⛔️| Ko'rish Kategoriyasi: 18+\n\n🔰| Kanal: @nur02_16\n🗂 Yuklash: 5903\n\n🤖 Bizning bot: @news4sd_bot"
                                       )
        else:
            await message.answer(
                "⚠️ Siz kanalga obuna bo'lmagansiz! Kanalga obuna bo'ling va qayta urinib ko'ring.",
                reply_markup=check
            )

    except Exception as e:
        await message.answer("❌ Xatolik yuz berdi. Iltimos, qayta urinib ko'ring.")
        logging.error(f"Error in video sending: {e}")


# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
@dp.message(F.text == "29")
async def send_video(message: Message):
    print(f"Foydalanuvchi:Jahannamda")
    try:
        user_status = await bot.get_chat_member(chat_id=CHAT_ID, user_id=message.from_user.id)
        if user_status.status in ["member", "administrator", "creator"]:
            file_id = "BAACAgIAAxkBAAIFcWdJ-TeDZOMZ6YUSGCf5zKMartH8AAKAOwACpAa5SVw5D9_H6SarNgQ"
            await message.answer_video(video=file_id,
                                       caption="Jahannamda\n➖➖➖➖➖➖➖➖➖➖➖➖\n🇺🇿| Tili: O'zbek tilida\n💾| Sifati: Ts format)\n🎞️| Janri: Jangari\n⛔️| Ko'rish Kategoriyasi: 18+\n\n🔰| Kanal: @nur02_16\n🗂 Yuklash: 5903\n\n🤖 Bizning bot: @news4sd_bot"
                                       )
        else:
            await message.answer(
                "⚠️ Siz kanalga obuna bo'lmagansiz! Kanalga obuna bo'ling va qayta urinib ko'ring.",
                reply_markup=check
            )

    except Exception as e:
        await message.answer("❌ Xatolik yuz berdi. Iltimos, qayta urinib ko'ring.")
        logging.error(f"Error in video sending: {e}")


# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
@dp.message(F.text == "30")
async def send_video(message: Message):
    print(f"Foydalanuvchi:Moana 2")
    try:
        user_status = await bot.get_chat_member(chat_id=CHAT_ID, user_id=message.from_user.id)
        if user_status.status in ["member", "administrator", "creator"]:
            file_id = "BAACAgIAAxkBAAIFx2dMMG3Gb_R8OllAWfQtryqjxiTwAAIFWgAC-QtYSnwUee1sSdhpNgQ"
            await message.answer_video(video=file_id,
                                       caption="Moana 2\n➖➖➖➖➖➖➖➖➖➖➖➖\n🇺🇿| Tili: O'zbek tilida\n💾| Sifati: Ts format)\n🎞️| Janri: Jangari\n⛔️| Ko'rish Kategoriyasi: 18+\n\n🔰| Kanal: @nur02_16\n🗂 Yuklash: 5903\n\n🤖 Bizning bot: @news4sd_bot"
                                       )
        else:
            await message.answer(
                "⚠️ Siz kanalga obuna bo'lmagansiz! Kanalga obuna bo'ling va qayta urinib ko'ring.",
                reply_markup=check
            )

    except Exception as e:
        await message.answer("❌ Xatolik yuz berdi. Iltimos, qayta urinib ko'ring.")
        logging.error(f"Error in video sending: {e}")


# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
@dp.message(F.text == "31")
async def send_video(message: Message):
    print(f"Foydalanuvchi:Madagascar Yevropa bo’ylab qidruv")
    try:
        user_status = await bot.get_chat_member(chat_id=CHAT_ID, user_id=message.from_user.id)
        if user_status.status in ["member", "administrator", "creator"]:
            file_id = "BAACAgIAAxkBAAIFy2dMNuqi4A1HqlvbhhSAQEdoIuXtAALICAACh-9oSi5cmSfwyqJjNgQ"
            await message.answer_video(video=file_id,
                                       caption="Madagascar Yevropa bo’ylab qidruv\n➖➖➖➖➖➖➖➖➖➖➖➖\n🇺🇿| Tili: O'zbek tilida\n💾| Sifati: Ts format)\n🎞️| Janri: Jangari\n⛔️| Ko'rish Kategoriyasi: 18+\n\n🔰| Kanal: @nur02_16\n🗂 Yuklash: 5903\n\n🤖 Bizning bot: @news4sd_bot"
                                       )
        else:
            await message.answer(
                "⚠️ Siz kanalga obuna bo'lmagansiz! Kanalga obuna bo'ling va qayta urinib ko'ring.",
                reply_markup=check
            )

    except Exception as e:
        await message.answer("❌ Xatolik yuz berdi. Iltimos, qayta urinib ko'ring.")
        logging.error(f"Error in video sending: {e}")


# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
@dp.message(F.text == "32")
async def send_video(message: Message):
    print(f"Foydalanuvchi:Sevgi va maxluqlar")
    try:
        user_status = await bot.get_chat_member(chat_id=CHAT_ID, user_id=message.from_user.id)
        if user_status.status in ["member", "administrator", "creator"]:
            file_id = "BAACAgQAAxkBAAIF_GdMSe7sqDdG5HLik4NNwgp2McqIAAJrCAACmwlxUgl1CEWPAAHrNDYE"
            await message.answer_video(video=file_id,
                                       caption="Sevgi va maxluqlar\n➖➖➖➖➖➖➖➖➖➖➖➖\n🇺🇿| Tili: O'zbek tilida\n💾| Sifati: Ts format)\n🎞️| Janri: Jangari\n⛔️| Ko'rish Kategoriyasi: 18+\n\n🔰| Kanal: @nur02_16\n🗂 Yuklash: 5903\n\n🤖 Bizning bot: @news4sd_bot"
                                       )
        else:
            await message.answer(
                "⚠️ Siz kanalga obuna bo'lmagansiz! Kanalga obuna bo'ling va qayta urinib ko'ring.",
                reply_markup=check
            )

    except Exception as e:
        await message.answer("❌ Xatolik yuz berdi. Iltimos, qayta urinib ko'ring.")
        logging.error(f"Error in video sending: {e}")


# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
@dp.message(F.text == "33")
async def send_video(message: Message):
    print(f"Foydalanuvchi:Noto'g'ri qadam")
    try:
        user_status = await bot.get_chat_member(chat_id=CHAT_ID, user_id=message.from_user.id)
        if user_status.status in ["member", "administrator", "creator"]:
            file_id = "BAACAgEAAxkBAAIGF2dMVMqEXc6RoF64SDlFY-Kkouk_AAKsAwACLbnQRNaSOuf3L-uRNgQ"
            await message.answer_video(video=file_id,
                                       caption="Noto'g'ri qadam\n➖➖➖➖➖➖➖➖➖➖➖➖\n🇺🇿| Tili: O'zbek tilida\n💾| Sifati: Ts format)\n🎞️| Janri: Jangari\n⛔️| Ko'rish Kategoriyasi: 18+\n\n🔰| Kanal: @nur02_16\n🗂 Yuklash: 5903\n\n🤖 Bizning bot: @news4sd_bot"
                                       )
        else:
            await message.answer(
                "⚠️ Siz kanalga obuna bo'lmagansiz! Kanalga obuna bo'ling va qayta urinib ko'ring.",
                reply_markup=check
            )

    except Exception as e:
        await message.answer("❌ Xatolik yuz berdi. Iltimos, qayta urinib ko'ring.")
        logging.error(f"Error in video sending: {e}")


# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
@dp.message(F.text == "34")
async def send_video(message: Message):
    print(f"Foydalanuvchi:Yer qari: yer tubi")
    try:
        user_status = await bot.get_chat_member(chat_id=CHAT_ID, user_id=message.from_user.id)
        if user_status.status in ["member", "administrator", "creator"]:
            file_id = "BAACAgQAAxkBAAIGGmdMXKoRM1XbjVUcm5d-bqAUPMhmAAIFEAACrwRpUec48CJxi9uiNgQ"
            await message.answer_video(video=file_id,
                                       caption=" Yer qari: yer tubi\n➖➖➖➖➖➖➖➖➖➖➖➖\n🇺🇿| Tili: O'zbek tilida\n💾| Sifati: Ts format)\n🎞️| Janri: Jangari\n⛔️| Ko'rish Kategoriyasi: 18+\n\n🔰| Kanal: @nur02_16\n🗂 Yuklash: 5903\n\n🤖 Bizning bot: @news4sd_bot"
                                       )
        else:
            await message.answer(
                "⚠️ Siz kanalga obuna bo'lmagansiz! Kanalga obuna bo'ling va qayta urinib ko'ring.",
                reply_markup=check
            )

    except Exception as e:
        await message.answer("❌ Xatolik yuz berdi. Iltimos, qayta urinib ko'ring.")
        logging.error(f"Error in video sending: {e}")


# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
@dp.message(F.text == "35")
async def send_video(message: Message):
    print(f"Foydalanuvchi:Enkanto")
    try:
        user_status = await bot.get_chat_member(chat_id=CHAT_ID, user_id=message.from_user.id)
        if user_status.status in ["member", "administrator", "creator"]:
            file_id = "BAACAgQAAxkBAAIGKmdMd62M3AEnC7ZRqBcReyDuixlMAAK-CQAC_FKAUovuyqv3K5CANgQ"
            await message.answer_video(video=file_id,
                                       caption="Enkanto\n➖➖➖➖➖➖➖➖➖➖➖➖\n🇺🇿| Tili: O'zbek tilida\n💾| Sifati: Ts format)\n🎞️| Janri: Jangari\n⛔️| Ko'rish Kategoriyasi: 18+\n\n🔰| Kanal: @nur02_16\n🗂 Yuklash: 5903\n\n🤖 Bizning bot: @news4sd_bot"
                                       )
        else:
            await message.answer(
                "⚠️ Siz kanalga obuna bo'lmagansiz! Kanalga obuna bo'ling va qayta urinib ko'ring.",
                reply_markup=check
            )

    except Exception as e:
        await message.answer("❌ Xatolik yuz berdi. Iltimos, qayta urinib ko'ring.")
        logging.error(f"Error in video sending: {e}")


# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
@dp.message(F.text == "36")
async def send_video(message: Message):
    print(f"Foydalanuvchi:Adolat ligasi")
    try:
        user_status = await bot.get_chat_member(chat_id=CHAT_ID, user_id=message.from_user.id)
        if user_status.status in ["member", "administrator", "creator"]:
            file_id = "BAACAgQAAxkBAAIGSmdMnP9DjYNX0z7BQxpK091vXOEqAAKuEQACf9xQUDYxGLFVcRJqNgQ"
            await message.answer_video(video=file_id,
                                       caption="Adolat ligasi\n➖➖➖➖➖➖➖➖➖➖➖➖\n🇺🇿| Tili: O'zbek tilida\n💾| Sifati: Ts format)\n🎞️| Janri: Jangari\n⛔️| Ko'rish Kategoriyasi: 18+\n\n🔰| Kanal: @nur02_16\n🗂 Yuklash: 5903\n\n🤖 Bizning bot: @news4sd_bot"
                                       )
        else:
            await message.answer(
                "⚠️ Siz kanalga obuna bo'lmagansiz! Kanalga obuna bo'ling va qayta urinib ko'ring.",
                reply_markup=check
            )

    except Exception as e:
        await message.answer("❌ Xatolik yuz berdi. Iltimos, qayta urinib ko'ring.")
        logging.error(f"Error in video sending: {e}")


# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
@dp.message(F.text == "37")
async def send_video(message: Message):
    print(f"Foydalanuvchi: intiho ")
    try:
        user_status = await bot.get_chat_member(chat_id=CHAT_ID, user_id=message.from_user.id)
        if user_status.status in ["member", "administrator", "creator"]:
            file_id = "BAACAgEAAxkBAAIGTGdMot-01SRt2ZxwruhpkdRbIg9DAAIwAQACWJRBRnX6Eh5ymjoVNgQ"
            await message.answer_video(video=file_id,
                                       caption=" intiho \n➖➖➖➖➖➖➖➖➖➖➖➖\n🇺🇿| Tili: O'zbek tilida\n💾| Sifati: Ts format)\n🎞️| Janri: Jangari\n⛔️| Ko'rish Kategoriyasi: 18+\n\n🔰| Kanal: @nur02_16\n🗂 Yuklash: 5903\n\n🤖 Bizning bot: @news4sd_bot"
                                       )
        else:
            await message.answer(
                "⚠️ Siz kanalga obuna bo'lmagansiz! Kanalga obuna bo'ling va qayta urinib ko'ring.",
                reply_markup=check
            )

    except Exception as e:
        await message.answer("❌ Xatolik yuz berdi. Iltimos, qayta urinib ko'ring.")
        logging.error(f"Error in video sending: {e}")


# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
@dp.message(F.text == "38")
async def send_video(message: Message):
    print(f"Foydalanuvchi:Yo‘l bo‘yidagi uy")
    try:
        user_status = await bot.get_chat_member(chat_id=CHAT_ID, user_id=message.from_user.id)
        if user_status.status in ["member", "administrator", "creator"]:
            file_id = "BAACAgQAAxkBAAIFvmdMAAHTbxERlg4yrhEAAeQe4EJfK70AAu8SAALtuOFREUlTvn6fj002BA"
            await message.answer_video(video=file_id,
                                       caption="Yo‘l bo‘yidagi uy\n➖➖➖➖➖➖➖➖➖➖➖➖\n🇺🇿| Tili: O'zbek tilida\n💾| Sifati: Ts format)\n🎞️| Janri: Jangari\n⛔️| Ko'rish Kategoriyasi: 18+\n\n🔰| Kanal: @nur02_16\n🗂 Yuklash: 5903\n\n🤖 Bizning bot: @news4sd_bot"
                                       )
        else:
            await message.answer(
                "⚠️ Siz kanalga obuna bo'lmagansiz! Kanalga obuna bo'ling va qayta urinib ko'ring.",
                reply_markup=check
            )

    except Exception as e:
        await message.answer("❌ Xatolik yuz berdi. Iltimos, qayta urinib ko'ring.")
        logging.error(f"Error in video sending: {e}")


# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
@dp.message(F.text == "39")
async def send_video(message: Message):
    print(f"Foydalanuvchi:Maxluqlar ta'tilda 2")
    try:
        user_status = await bot.get_chat_member(chat_id=CHAT_ID, user_id=message.from_user.id)
        if user_status.status in ["member", "administrator", "creator"]:
            file_id = "BAACAgQAAxkBAAIGcmdNWmBMDS-HkMUM8Sr8OGi1TOOYAAJGCgACcbmYU7NlK1o7rmxINgQ"
            await message.answer_video(video=file_id,
                                       caption="Maxluqlar ta'tilda 2 \n➖➖➖➖➖➖➖➖➖➖➖➖\n🇺🇿| Tili: O'zbek tilida\n💾| Sifati: Ts format)\n🎞️| Janri: Jangari\n⛔️| Ko'rish Kategoriyasi: 18+\n\n🔰| Kanal: @nur02_16\n🗂 Yuklash: 5903\n\n🤖 Bizning bot: @news4sd_bot"
                                       )
        else:
            await message.answer(
                "⚠️ Siz kanalga obuna bo'lmagansiz! Kanalga obuna bo'ling va qayta urinib ko'ring.",
                reply_markup=check
            )

    except Exception as e:
        await message.answer("❌ Xatolik yuz berdi. Iltimos, qayta urinib ko'ring.")
        logging.error(f"Error in video sending: {e}")


# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
@dp.message(F.text == "40")
async def send_video(message: Message):
    print(f"Foydalanuvchi:Avatar 2: Suv yo'li")
    try:
        user_status = await bot.get_chat_member(chat_id=CHAT_ID, user_id=message.from_user.id)
        if user_status.status in ["member", "administrator", "creator"]:
            file_id = "BAACAgQAAxkBAAIGqWdN03GrxR_SUbNutwafqD5dV86tAALgDQACbaIBUhObPqUjLVH1NgQ"
            await message.answer_video(video=file_id,
                                       caption="Avatar 2: Suv yo'li\n➖➖➖➖➖➖➖➖➖➖➖➖\n🇺🇿| Tili: O'zbek tilida\n💾| Sifati: Ts format)\n🎞️| Janri: Jangari\n⛔️| Ko'rish Kategoriyasi: 18+\n\n🔰| Kanal: @nur02_16\n🗂 Yuklash: 5903\n\n🤖 Bizning bot: @news4sd_bot"
                                       )
        else:
            await message.answer(
                "⚠️ Siz kanalga obuna bo'lmagansiz! Kanalga obuna bo'ling va qayta urinib ko'ring.",
                reply_markup=check
            )

    except Exception as e:
        await message.answer("❌ Xatolik yuz berdi. Iltimos, qayta urinib ko'ring.")
        logging.error(f"Error in video sending: {e}")


# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
@dp.message(F.text == "41")
async def send_video(message: Message):
    print(f"Foydalanuvchi: Lanatlangan ko'zyoshlar")
    try:
        user_status = await bot.get_chat_member(chat_id=CHAT_ID, user_id=message.from_user.id)
        if user_status.status in ["member", "administrator", "creator"]:
            file_id = "BAACAgIAAxkBAAIGrWdN2d5qE9QJXenm1vZPhEm8uW2HAAKKCwACm33JSklgLQg_10AaNgQ"
            await message.answer_video(video=file_id,
                                       caption=" Lanatlangan ko'zyoshlar\n➖➖➖➖➖➖➖➖➖➖➖➖\n🇺🇿| Tili: O'zbek tilida\n💾| Sifati: Ts format)\n🎞️| Janri: Jangari\n⛔️| Ko'rish Kategoriyasi: 18+\n\n🔰| Kanal: @nur02_16\n🗂 Yuklash: 5903\n\n🤖 Bizning bot: @news4sd_bot"
                                       )
        else:
            await message.answer(
                "⚠️ Siz kanalga obuna bo'lmagansiz! Kanalga obuna bo'ling va qayta urinib ko'ring.",
                reply_markup=check
            )

    except Exception as e:
        await message.answer("❌ Xatolik yuz berdi. Iltimos, qayta urinib ko'ring.")
        logging.error(f"Error in video sending: {e}")


# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
@dp.message(F.text == "42")
async def send_video(message: Message):
    print(f"Foydalanuvchi: Kung Fu Panda 4")
    try:
        user_status = await bot.get_chat_member(chat_id=CHAT_ID, user_id=message.from_user.id)
        if user_status.status in ["member", "administrator", "creator"]:
            file_id = "BAACAgEAAxkBAAIGr2dN7dQ2vt9CPzZxkmmyNxS5aOGoAALiAgACdIuQR8IXGHl6sEooNgQ"
            await message.answer_video(video=file_id,
                                       caption=" Kung Fu Panda 4\n➖➖➖➖➖➖➖➖➖➖➖➖\n🇺🇿| Tili: O'zbek tilida\n💾| Sifati: Ts format)\n🎞️| Janri: Jangari\n⛔️| Ko'rish Kategoriyasi: 18+\n\n🔰| Kanal: @nur02_16\n🗂 Yuklash: 5903\n\n🤖 Bizning bot: @news4sd_bot"
                                       )
        else:
            await message.answer(
                "⚠️ Siz kanalga obuna bo'lmagansiz! Kanalga obuna bo'ling va qayta urinib ko'ring.",
                reply_markup=check
            )

    except Exception as e:
        await message.answer("❌ Xatolik yuz berdi. Iltimos, qayta urinib ko'ring.")
        logging.error(f"Error in video sending: {e}")


# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
@dp.message(F.text == "43")
async def send_video(message: Message):
    print(f"Foydalanuvchi:Telbalar ")
    try:
        user_status = await bot.get_chat_member(chat_id=CHAT_ID, user_id=message.from_user.id)
        if user_status.status in ["member", "administrator", "creator"]:
            file_id = "BAACAgQAAxkBAAIGsmdN8PhmyZdfMwnkHCIpBGmtBzhEAAIsEgAC_PRQUuGMw4PFSRY6NgQ"
            await message.answer_video(video=file_id,
                                       caption="Telbalar \n➖➖➖➖➖➖➖➖➖➖➖➖\n🇺🇿| Tili: O'zbek tilida\n💾| Sifati: Ts format)\n🎞️| Janri: Jangari\n⛔️| Ko'rish Kategoriyasi: 18+\n\n🔰| Kanal: @nur02_16\n🗂 Yuklash: 5903\n\n🤖 Bizning bot: @news4sd_bot"
                                       )
        else:
            await message.answer(
                "⚠️ Siz kanalga obuna bo'lmagansiz! Kanalga obuna bo'ling va qayta urinib ko'ring.",
                reply_markup=check
            )

    except Exception as e:
        await message.answer("❌ Xatolik yuz berdi. Iltimos, qayta urinib ko'ring.")
        logging.error(f"Error in video sending: {e}")


# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
@dp.message(F.text == "45")
async def send_video(message: Message):
    print(f"Foydalanuvchi:Ancharted")
    try:
        user_status = await bot.get_chat_member(chat_id=CHAT_ID, user_id=message.from_user.id)
        if user_status.status in ["member", "administrator", "creator"]:
            file_id = "BAACAgEAAxkBAAIG0GdN_aaoREpE2rLJHcGvdRugaZpxAAKbAQACS-8xR4eVQG9tE7lvNgQ"
            await message.answer_video(video=file_id,
                                       caption="Ancharted\n➖➖➖➖➖➖➖➖➖➖➖➖\n🇺🇿| Tili: O'zbek tilida\n💾| Sifati: Ts format)\n🎞️| Janri: Jangari\n⛔️| Ko'rish Kategoriyasi: 18+\n\n🔰| Kanal: @nur02_16\n🗂 Yuklash: 5903\n\n🤖 Bizning bot: @news4sd_bot"
                                       )
        else:
            await message.answer(
                "⚠️ Siz kanalga obuna bo'lmagansiz! Kanalga obuna bo'ling va qayta urinib ko'ring.",
                reply_markup=check
            )

    except Exception as e:
        await message.answer("❌ Xatolik yuz berdi. Iltimos, qayta urinib ko'ring.")
        logging.error(f"Error in video sending: {e}")


# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
@dp.message(F.text == "44")
async def send_video(message: Message):
    print(f"Foydalanuvchi:Qahramon Ayol")
    try:
        user_status = await bot.get_chat_member(chat_id=CHAT_ID, user_id=message.from_user.id)
        if user_status.status in ["member", "administrator", "creator"]:
            file_id = "BAACAgQAAxkBAAIGu2dN9RIUqupaVHcufWzXgeoq74xrAAINCQACXomIU-dwFD_z2tl6NgQ"
            await message.answer_video(video=file_id,
                                       caption="Qahramon Ayol\n➖➖➖➖➖➖➖➖➖➖➖➖\n🇺🇿| Tili: O'zbek tilida\n💾| Sifati: Ts format)\n🎞️| Janri: Jangari\n⛔️| Ko'rish Kategoriyasi: 18+\n\n🔰| Kanal: @nur02_16\n🗂 Yuklash: 5903\n\n🤖 Bizning bot: @news4sd_bot"
                                       )
        else:
            await message.answer(
                "⚠️ Siz kanalga obuna bo'lmagansiz! Kanalga obuna bo'ling va qayta urinib ko'ring.",
                reply_markup=check
            )

    except Exception as e:
        await message.answer("❌ Xatolik yuz berdi. Iltimos, qayta urinib ko'ring.")
        logging.error(f"Error in video sending: {e}")


# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
@dp.message(F.text == "46")
async def send_video(message: Message):
    print(f"Foydalanuvchi:Qo'rquv badali")
    try:
        user_status = await bot.get_chat_member(chat_id=CHAT_ID, user_id=message.from_user.id)
        if user_status.status in ["member", "administrator", "creator"]:
            file_id = "BAACAgQAAxkBAAIHGWdOqqIKD1ascO5jdl6KNnhgOZ6pAAL1EgACUSuQUH2Q8VdkEYv5NgQ"
            await message.answer_video(video=file_id,
                                       caption="Qo'rquv badali\n➖➖➖➖➖➖➖➖➖➖➖➖\n🇺🇿| Tili: O'zbek tilida\n💾| Sifati: Ts format)\n🎞️| Janri: Jangari\n⛔️| Ko'rish Kategoriyasi: 18+\n\n🔰| Kanal: @nur02_16\n🗂 Yuklash: 5903\n\n🤖 Bizning bot: @news4sd_bot"
                                       )
        else:
            await message.answer(
                "⚠️ Siz kanalga obuna bo'lmagansiz! Kanalga obuna bo'ling va qayta urinib ko'ring.",
                reply_markup=check
            )

    except Exception as e:
        await message.answer("❌ Xatolik yuz berdi. Iltimos, qayta urinib ko'ring.")
        logging.error(f"Error in video sending: {e}")


# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
@dp.message(F.text == "47")
async def send_video(message: Message):
    print(f"Foydalanuvchi: Mumiyo")
    try:
        user_status = await bot.get_chat_member(chat_id=CHAT_ID, user_id=message.from_user.id)
        if user_status.status in ["member", "administrator", "creator"]:
            file_id = "BAACAgIAAxkBAAIHMmdO0DdF2TkLMsiuDlIPnzVVQHSYAAJuDgACnfoRSoJgc9VI8DVnNgQ"
            await message.answer_video(video=file_id,
                                       caption=" Mumiyo\n➖➖➖➖➖➖➖➖➖➖➖➖\n🇺🇿| Tili: O'zbek tilida\n💾| Sifati: Ts format)\n🎞️| Janri: Jangari\n⛔️| Ko'rish Kategoriyasi: 18+\n\n🔰| Kanal: @nur02_16\n🗂 Yuklash: 5903\n\n🤖 Bizning bot: @news4sd_bot"
                                       )
        else:
            await message.answer(
                "⚠️ Siz kanalga obuna bo'lmagansiz! Kanalga obuna bo'ling va qayta urinib ko'ring.",
                reply_markup=check
            )

    except Exception as e:
        await message.answer("❌ Xatolik yuz berdi. Iltimos, qayta urinib ko'ring.")
        logging.error(f"Error in video sending: {e}")


# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
@dp.message(F.text == "48")
async def send_video(message: Message):
    print(f"Foydalanuvchi:Turnir")
    try:
        user_status = await bot.get_chat_member(chat_id=CHAT_ID, user_id=message.from_user.id)
        if user_status.status in ["member", "administrator", "creator"]:
            file_id = "BAACAgIAAxkBAAIHR2dO8ibBnZJVRXSYluMIQvvVJxbOAALgXAACOUF5Su0Np4xFQzcBNgQ"

            await message.answer_video(video=file_id,
                                       caption="Turnir\n➖➖➖➖➖➖➖➖➖➖➖➖\n🇺🇿| Tili: O'zbek tilida\n💾| Sifati: Ts format)\n🎞️| Janri: Jangari\n⛔️| Ko'rish Kategoriyasi: 18+\n\n🔰| Kanal: @nur02_16\n🗂 Yuklash: 5903\n\n🤖 Bizning bot: @news4sd_bot"
                                       )
        else:
            await message.answer(
                "⚠️ Siz kanalga obuna bo'lmagansiz! Kanalga obuna bo'ling va qayta urinib ko'ring.",
                reply_markup=check
            )

    except Exception as e:
        await message.answer("❌ Xatolik yuz berdi. Iltimos, qayta urinib ko'ring.")
        logging.error(f"Error in video sending: {e}")


# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
@dp.message(F.text == "49")
async def send_video(message: Message):
    print(f"Foydalanuvchi:Turnir 2")
    try:
        user_status = await bot.get_chat_member(chat_id=CHAT_ID, user_id=message.from_user.id)
        if user_status.status in ["member", "administrator", "creator"]:
            file_id = "BAACAgIAAxkBAAIIRmdTO1aRy0LqYs5Vzq59MMSsaplhAAKDaQACcYx4SuhvnOydbVRGNgQ"

            await message.answer_video(video=file_id,
                                       caption="Turnir 2\n➖➖➖➖➖➖➖➖➖➖➖➖\n🇺🇿| Tili: O'zbek tilida\n💾| Sifati: Ts format)\n🎞️| Janri: Jangari\n⛔️| Ko'rish Kategoriyasi: 18+\n\n🔰| Kanal: @nur02_16\n🗂 Yuklash: 5903\n\n🤖 Bizning bot: @news4sd_bot"
                                       )
        else:
            await message.answer(
                "⚠️ Siz kanalga obuna bo'lmagansiz! Kanalga obuna bo'ling va qayta urinib ko'ring.",
                reply_markup=check
            )

    except Exception as e:
        await message.answer("❌ Xatolik yuz berdi. Iltimos, qayta urinib ko'ring.")
        logging.error(f"Error in video sending: {e}")


# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
@dp.message(F.text == "50")
async def send_video(message: Message):
    print(f"Foydalanuvchi:Alita")
    try:
        user_status = await bot.get_chat_member(chat_id=CHAT_ID, user_id=message.from_user.id)
        if user_status.status in ["member", "administrator", "creator"]:
            file_id = "BAACAgQAAxkBAAIHnGdQbK4oMeKAoNB2Gn47YdC-8G9PAALrEAACFRbAUbELsEScjAuqNgQ"
            await message.answer_video(
                video=file_id,
                caption="#🍿| Kino Nomi:Alita\n➖➖➖➖➖➖➖➖➖➖➖➖\n🇺🇿| Tili: O'zbek tilida\n💾| Sifati: Ts format \n🎞️| Janri: Jangari\n⛔️| Ko'rish Kategoriyasi: 18+\n\n🔰| Kanal: @nur02_16\n🗂 Yuklash: 5903\n\n🤖 Bizning bot: @news4sd_bot"
            )
        else:
            await message.answer(
                "⚠️ Siz kanalga obuna bo'lmagansiz! Kanalga obuna bo'ling va qayta urinib ko'ring.",
                reply_markup=check
            )
    except Exception as e:
        await message.answer("❌ Xatolik yuz berdi. Iltimos, qayta urinib ko'ring.")
        logging.error(f"Error in video sending: {e}")


# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
@dp.message(F.text == "51")
async def send_video(message: Message):
    print(f"Foydalanuvchi:Qashqirlar makoni: Falastin")
    try:
        user_status = await bot.get_chat_member(chat_id=CHAT_ID, user_id=message.from_user.id)
        if user_status.status in ["member", "administrator", "creator"]:
            file_id = "BAACAgEAAxkBAAIHoWdQdpD3RSvj5DujmGbb_T_QsMgcAAIYAgACpN2xRGavKKtGBYFiNgQ"
            await message.answer_video(
                video=file_id,
                caption="#🍿| Kino Nomi:Qashqirlar makoni: Falastin\n➖➖➖➖➖➖➖➖➖➖➖➖\n🇺🇿| Tili: O'zbek tilida\n💾| Sifati: Ts format \n🎞️| Janri: Jangari\n⛔️| Ko'rish Kategoriyasi: 18+\n\n🔰| Kanal: @nur02_16\n🗂 Yuklash: 5903\n\n🤖 Bizning bot: @news4sd_bot"
            )
        else:
            await message.answer(
                "⚠️ Siz kanalga obuna bo'lmagansiz! Kanalga obuna bo'ling va qayta urinib ko'ring.",
                reply_markup=check
            )
    except Exception as e:
        await message.answer("❌ Xatolik yuz berdi. Iltimos, qayta urinib ko'ring.")
        logging.error(f"Error in video sending: {e}")


# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
@dp.message(F.text == "52")
async def send_video(message: Message):
    print(f"Foydalanuvchi:Biz qahramon bo'lamiz")
    try:
        user_status = await bot.get_chat_member(chat_id=CHAT_ID, user_id=message.from_user.id)
        if user_status.status in ["member", "administrator", "creator"]:
            file_id = "BAACAgQAAxkBAAIHqWdQfKuBxV3xO8UWpFCQe5-mLhh5AAIICwACMggxUVXCk2XctVpANgQ"
            await message.answer_video(
                video=file_id,
                caption="#🍿| Kino Nomi:Qashqirlar makoni:Biz qahramon bo'lamiz\n➖➖➖➖➖➖➖➖➖➖➖➖\n🇺🇿| Tili: O'zbek tilida\n💾| Sifati: Ts format \n🎞️| Janri: Jangari\n⛔️| Ko'rish Kategoriyasi: 18+\n\n🔰| Kanal: @nur02_16\n🗂 Yuklash: 5903\n\n🤖 Bizning bot: @news4sd_bot"
            )
        else:
            await message.answer(
                "⚠️ Siz kanalga obuna bo'lmagansiz! Kanalga obuna bo'ling va qayta urinib ko'ring.",
                reply_markup=check
            )
    except Exception as e:
        await message.answer("❌ Xatolik yuz berdi. Iltimos, qayta urinib ko'ring.")
        logging.error(f"Error in video sending: {e}")


# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
@dp.message(F.text == "53")
async def send_video(message: Message):
    print(f"Foydalanuvchi: 7-Bo'lmadagi Mo'jiza")
    try:
        user_status = await bot.get_chat_member(chat_id=CHAT_ID, user_id=message.from_user.id)
        if user_status.status in ["member", "administrator", "creator"]:
            file_id = "BAACAgIAAxkBAAIHp2dQeyGyBwYr20G7QOV7VRrEeQkGAAIZKAACLnq4S8RYhVlc7CsmNgQ"
            await message.answer_video(
                video=file_id,
                caption="#🍿| Kino Nomi: 7-Bo'lmadagi Mo'jiza\n➖➖➖➖➖➖➖➖➖➖➖➖\n🇺🇿| Tili: O'zbek tilida\n💾| Sifati: Ts format \n🎞️| Janri: Jangari\n⛔️| Ko'rish Kategoriyasi: 18+\n\n🔰| Kanal: @nur02_16\n🗂 Yuklash: 5903\n\n🤖 Bizning bot: @news4sd_bot"
            )
        else:
            await message.answer(
                "⚠️ Siz kanalga obuna bo'lmagansiz! Kanalga obuna bo'ling va qayta urinib ko'ring.",
                reply_markup=check
            )
    except Exception as e:
        await message.answer("❌ Xatolik yuz berdi. Iltimos, qayta urinib ko'ring.")
        logging.error(f"Error in video sending: {e}")


# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
@dp.message(F.text == "54")
async def send_video(message: Message):
    print(f"Foydalanuvchi:Uyda yolg'iz")
    try:
        user_status = await bot.get_chat_member(chat_id=CHAT_ID, user_id=message.from_user.id)
        if user_status.status in ["member", "administrator", "creator"]:
            file_id = "BAACAgIAAxkBAAIHr2dQfcnva3OrS9IN8aII7gUMX2TuAAKGAgACbNsxSqtyMNDBJsxZNgQ"
            await message.answer_video(
                video=file_id,
                caption="#🍿| Kino Nomi:Uyda yolg'iz 1\n➖➖➖➖➖➖➖➖➖➖➖➖\n🇺🇿| Tili: O'zbek tilida\n💾| Sifati: Ts format \n🎞️| Janri: Jangari\n⛔️| Ko'rish Kategoriyasi: 6+\n\n🔰| Kanal: @nur02_16\n🗂 Yuklash: 5903\n\n🤖 Bizning bot: @news4sd_bot"
            )
        if user_status.status in ["member", "administrator", "creator"]:
            file_id = "BAACAgIAAxkBAAIHrGdQfcmLE_xnKXiuQx0e3jgWzpjWAAI7AwACQ3lpSUGa8-x2nr-RNgQ"
            await message.answer_video(
                video=file_id,
                caption="#🍿| Kino Nomi:Uyda yolg'iz 2\n➖➖➖➖➖➖➖➖➖➖➖➖\n🇺🇿| Tili: O'zbek tilida\n💾| Sifati: Ts format \n🎞️| Janri: Jangari\n⛔️| Ko'rish Kategoriyasi: 6+\n\n🔰| Kanal: @nur02_16\n🗂 Yuklash: 5903\n\n🤖 Bizning bot: @news4sd_bot"
            )
        if user_status.status in ["member", "administrator", "creator"]:
            file_id = "BAACAgIAAxkBAAIHsGdQfckVklg6eOKbFM8mt9VAv0PMAAJUIQAC542ASC3arCQXNY-UNgQ"
            await message.answer_video(
                video=file_id,
                caption="#🍿| Kino Nomi:Uyda yolg'iz 3\n➖➖➖➖➖➖➖➖➖➖➖➖\n🇺🇿| Tili: O'zbek tilida\n💾| Sifati: Ts format \n🎞️| Janri: Jangari\n⛔️| Ko'rish Kategoriyasi: 6+\n\n🔰| Kanal: @nur02_16\n🗂 Yuklash: 5903\n\n🤖 Bizning bot: @news4sd_bot"
            )
        if user_status.status in ["member", "administrator", "creator"]:
            file_id = "BAACAgIAAxkBAAIHrWdQfcl4jHgU2LbWoejdxGoYnJtlAAJFAgACCJexSYNlDlOIMOuiNgQ"
            await message.answer_video(
                video=file_id,
                caption="#🍿| Kino Nomi:Uyda yolg'iz 4\n➖➖➖➖➖➖➖➖➖➖➖➖\n🇺🇿| Tili: O'zbek tilida\n💾| Sifati: Ts format \n🎞️| Janri: Jangari\n⛔️| Ko'rish Kategoriyasi: 6+\n\n🔰| Kanal: @nur02_16\n🗂 Yuklash: 5903\n\n🤖 Bizning bot: @news4sd_bot"
            )
        if user_status.status in ["member", "administrator", "creator"]:
            file_id = "BAACAgIAAxkBAAIHq2dQfcmB7FZ4BAWHuXRn8fuI3iYxAAI6AwACQ3lpSdayTOfua4vuNgQ"
            await message.answer_video(
                video=file_id,
                caption="#🍿| Kino Nomi:Uyda yolg'iz 5\n➖➖➖➖➖➖➖➖➖➖➖➖\n🇺🇿| Tili: O'zbek tilida\n💾| Sifati: Ts format \n🎞️| Janri: Jangari\n⛔️| Ko'rish Kategoriyasi: 6+\n\n🔰| Kanal: @nur02_16\n🗂 Yuklash: 5903\n\n🤖 Bizning bot: @news4sd_bot"
            )
        if user_status.status in ["member", "administrator", "creator"]:
            file_id = "BAACAgIAAxkBAAIHrmdQfcnBlS32C8ODxyop1lNIKUB8AAJZAwACqwbISZIDmry4ula8NgQ"
            await message.answer_video(
                video=file_id,
                caption="#🍿| Kino Nomi:Uyda yolg'iz 6\n➖➖➖➖➖➖➖➖➖➖➖➖\n🇺🇿| Tili: O'zbek tilida\n💾| Sifati: Ts format \n🎞️| Janri: Jangari\n⛔️| Ko'rish Kategoriyasi: 6+\n\n🔰| Kanal: @nur02_16\n🗂 Yuklash: 5903\n\n🤖 Bizning bot: @news4sd_bot"
            )

        else:
            await message.answer(
                "⚠️ Siz kanalga obuna bo'lmagansiz! Kanalga obuna bo'ling va qayta urinib ko'ring.",
                reply_markup=check
            )
    except Exception as e:
        await message.answer("❌ Xatolik yuz berdi. Iltimos, qayta urinib ko'ring.")
        logging.error(f"Error in video sending: {e}")


# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
@dp.message(F.text == "55")
async def send_video(message: Message):
    print(f"Foydalanuvchi:Telba qasoskor")
    try:
        user_status = await bot.get_chat_member(chat_id=CHAT_ID, user_id=message.from_user.id)
        if user_status.status in ["member", "administrator", "creator"]:
            file_id = "BAACAgIAAxkBAAIHzWdQiBH7cR5ObMJQNoKnGqIqXv_kAAJGZAACBJCJSsfBhkuzOqEuNgQ"
            await message.answer_video(
                video=file_id,
                caption="#🍿| Kino Nomi:Telba qasoskor\n➖➖➖➖➖➖➖➖➖➖➖➖\n🇺🇿| Tili: O'zbek tilida\n💾| Sifati: Ts format \n🎞️| Janri: Jangari\n⛔️| Ko'rish Kategoriyasi: 18+\n\n🔰| Kanal: @nur02_16\n🗂 Yuklash: 5903\n\n🤖 Bizning bot: @news4sd_bot"
            )
        else:
            await message.answer(
                "⚠️ Siz kanalga obuna bo'lmagansiz! Kanalga obuna bo'ling va qayta urinib ko'ring.",
                reply_markup=check
            )
    except Exception as e:
        await message.answer("❌ Xatolik yuz berdi. Iltimos, qayta urinib ko'ring.")
        logging.error(f"Error in video sending: {e}")


# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
@dp.message(F.text == "56")
async def send_video(message: Message):
    print(f"Foydalanuvchi:Menga yana qara")
    try:
        user_status = await bot.get_chat_member(chat_id=CHAT_ID, user_id=message.from_user.id)
        if user_status.status in ["member", "administrator", "creator"]:
            file_id = "BAACAgQAAxkBAAIH2mdQkeiVKIn8yJA8edpidbf2TOyEAALSBwACMZuoUr6IsJajMmMDNgQ"
            await message.answer_video(
                video=file_id,
                caption="#🍿| Kino Nomi:Menga yana qara\n➖➖➖➖➖➖➖➖➖➖➖➖\n🇺🇿| Tili: O'zbek tilida\n💾| Sifati: Ts format \n🎞️| Janri: Jangari\n⛔️| Ko'rish Kategoriyasi: 18+\n\n🔰| Kanal: @nur02_16\n🗂 Yuklash: 5903\n\n🤖 Bizning bot: @news4sd_bot"
            )
        else:
            await message.answer(
                "⚠️ Siz kanalga obuna bo'lmagansiz! Kanalga obuna bo'ling va qayta urinib ko'ring.",
                reply_markup=check
            )
    except Exception as e:
        await message.answer("❌ Xatolik yuz berdi. Iltimos, qayta urinib ko'ring.")
        logging.error(f"Error in video sending: {e}")

        
# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
@dp.message(F.text == "57")
async def send_video(message: Message):
    print(f"Foydalanuvchi:Farishtalar shahri")
    try:
        user_status = await bot.get_chat_member(chat_id=CHAT_ID, user_id=message.from_user.id)
        if user_status.status in ["member", "administrator", "creator"]:
            file_id = "BAACAgIAAxkBAAIH5GdQlSv8LKNga1FO1m76kVVTLcCYAALuGQACww4QS8KpGf5zGbA2NgQ"
            await message.answer_video(
                video=file_id,
                caption="#🍿| Kino Nomi:Farishtalar shahri \n➖➖➖➖➖➖➖➖➖➖➖➖\n🇺🇿| Tili: O'zbek tilida\n💾| Sifati: Ts format \n🎞️| Janri: Jangari\n⛔️| Ko'rish Kategoriyasi: 18+\n\n🔰| Kanal: @nur02_16\n🗂 Yuklash: 5903\n\n🤖 Bizning bot: @news4sd_bot"
            )
        else:
            await message.answer(
                "⚠️ Siz kanalga obuna bo'lmagansiz! Kanalga obuna bo'ling va qayta urinib ko'ring.",
                reply_markup=check
            )
    except Exception as e:
        await message.answer("❌ Xatolik yuz berdi. Iltimos, qayta urinib ko'ring.")
        logging.error(f"Error in video sending: {e}")


# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
@dp.message(F.text == "58")
async def send_video(message: Message):
    print(f"Foydalanuvchi:Ajal poygasi")
    try:
        user_status = await bot.get_chat_member(chat_id=CHAT_ID, user_id=message.from_user.id)
        if user_status.status in ["member", "administrator", "creator"]:
            file_id = "BAACAgQAAxkBAAIH-WdR0Mg8BgPp9qiJZtAuKVwKmX7RAAKjFAACwpDgUb304iJCU6LHNgQ"
            await message.answer_video(
                video=file_id,
                caption="#🍿| Kino Nomi:Ajal poygasi\n➖➖➖➖➖➖➖➖➖➖➖➖\n🇺🇿| Tili: O'zbek tilida\n💾| Sifati: Ts format \n🎞️| Janri: Jangari\n⛔️| Ko'rish Kategoriyasi: 18+\n\n🔰| Kanal: @nur02_16\n🗂 Yuklash: 5903\n\n🤖 Bizning bot: @news4sd_bot"
            )
        else:
            await message.answer(
                "⚠️ Siz kanalga obuna bo'lmagansiz! Kanalga obuna bo'ling va qayta urinib ko'ring.",
                reply_markup=check
            )
    except Exception as e:
        await message.answer("❌ Xatolik yuz berdi. Iltimos, qayta urinib ko'ring.")
        logging.error(f"Error in video sending: {e}")


# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
@dp.message(F.text == "59")
async def send_video(message: Message):
    print(f"Foydalanuvchi:Turnir 3")
    try:
        user_status = await bot.get_chat_member(chat_id=CHAT_ID, user_id=message.from_user.id)
        if user_status.status in ["member", "administrator", "creator"]:
            file_id = "BAACAgIAAxkBAAIIQmdTOzAgWzsjbDk52dhxqMu65kUfAAKMbAACEVmISk8ePx_TMrzDNgQ"
            await message.answer_video(
                video=file_id,
                caption="#🍿| Kino Nomi:Turnir 3\n➖➖➖➖➖➖➖➖➖➖➖➖\n🇺🇿| Tili: O'zbek tilida\n💾| Sifati: Ts format \n🎞️| Janri: Jangari\n⛔️| Ko'rish Kategoriyasi: 18+\n\n🔰| Kanal: @nur02_16\n🗂 Yuklash: 5903\n\n🤖 Bizning bot: @news4sd_bot"
            )
        else:
            await message.answer(
                "⚠️ Siz kanalga obuna bo'lmagansiz! Kanalga obuna bo'ling va qayta urinib ko'ring.",
                reply_markup=check
            )
    except Exception as e:
        await message.answer("❌ Xatolik yuz berdi. Iltimos, qayta urinib ko'ring.")
        logging.error(f"Error in video sending: {e}")


# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
@dp.message(F.text == "60")
async def send_video(message: Message):
    print(f"Foydalanuvchi:Turnir 4")
    try:
        user_status = await bot.get_chat_member(chat_id=CHAT_ID, user_id=message.from_user.id)
        if user_status.status in ["member", "administrator", "creator"]:
            file_id = "BAACAgIAAxkBAAIINmdTLxdNVUUwpF4lkuoilwABARBg5gACRV4AArPOmEqc3CXMA1YENTYE"
            await message.answer_video(
                video=file_id,
                caption="#🍿| Kino Nomi:Turnir 4\n➖➖➖➖➖➖➖➖➖➖➖➖\n🇺🇿| Tili: O'zbek tilida\n💾| Sifati: Ts format \n🎞️| Janri: Jangari\n⛔️| Ko'rish Kategoriyasi: 18+\n\n🔰| Kanal: @nur02_16\n🗂 Yuklash: 5903\n\n🤖 Bizning bot: @news4sd_bot"
            )
        else:
            await message.answer(
                "⚠️ Siz kanalga obuna bo'lmagansiz! Kanalga obuna bo'ling va qayta urinib ko'ring.",
                reply_markup=check
            )
    except Exception as e:
        await message.answer("❌ Xatolik yuz berdi. Iltimos, qayta urinib ko'ring.")
        logging.error(f"Error in video sending: {e}")


# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
@dp.message(F.text == "61")
async def send_video(message: Message):
    print(f"Foydalanuvchi:Boshqotirma")
    try:
        user_status = await bot.get_chat_member(chat_id=CHAT_ID, user_id=message.from_user.id)
        if user_status.status in ["member", "administrator", "creator"]:
            file_id = "BAACAgEAAxkBAAIIimdV3krv7RgKpeu9Sr_0Cadov0imAAKhAANh4xlFH1PFb6KR4fY2BA"
            await message.answer_video(
                video=file_id,
                caption="#🍿| Kino Nomi:Boshqotirma\n➖➖➖➖➖➖➖➖➖➖➖➖\n🇺🇿| Tili: O'zbek tilida\n💾| Sifati: Ts format \n🎞️| Janri: Jangari\n⛔️| Ko'rish Kategoriyasi: 18+\n\n🔰| Kanal: @nur02_16\n🗂 Yuklash: 5903\n\n🤖 Bizning bot: @news4sd_bot"
            )
        if user_status.status in ["member", "administrator", "creator"]:
            file_id = "BAACAgQAAxkBAAIIiWdV3kropy3QaRj9bcberW4LewgaAALTEAAC82SpU1jrGeoI4KdnNgQ"
            await message.answer_video(
                video=file_id,
                caption="#🍿| Kino Nomi:Boshqotirma 2\n➖➖➖➖➖➖➖➖➖➖➖➖\n🇺🇿| Tili: O'zbek tilida\n💾| Sifati: Ts format \n🎞️| Janri: Jangari\n⛔️| Ko'rish Kategoriyasi: 18+\n\n🔰| Kanal: @nur02_16\n🗂 Yuklash: 5903\n\n🤖 Bizning bot: @news4sd_bot"
            )
        else:
            await message.answer(
                "⚠️ Siz kanalga obuna bo'lmagansiz! Kanalga obuna bo'ling va qayta urinib ko'ring.",
                reply_markup=check
            )
    except Exception as e:
        await message.answer("❌ Xatolik yuz berdi. Iltimos, qayta urinib ko'ring.")
        logging.error(f"Error in video sending: {e}")


# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
@dp.message(F.text == "62")
async def send_video(message: Message):
    print(f"Foydalanuvchi:Pishloq yomg'iri ")
    try:
        user_status = await bot.get_chat_member(chat_id=CHAT_ID, user_id=message.from_user.id)
        if user_status.status in ["member", "administrator", "creator"]:
            file_id = "BAACAgQAAxkBAAIIkGdV30z7GRnmwycEEe19GBojOyo2AALLCgACzs-JUj84jZkGUMRDNgQ"
            await message.answer_video(
                video=file_id,
                caption="#🍿| Kino Nomi:Pishloq yomg'iri \n➖➖➖➖➖➖➖➖➖➖➖➖\n🇺🇿| Tili: O'zbek tilida\n💾| Sifati: Ts format \n🎞️| Janri: Jangari\n⛔️| Ko'rish Kategoriyasi: 18+\n\n🔰| Kanal: @nur02_16\n🗂 Yuklash: 5903\n\n🤖 Bizning bot: @news4sd_bot"
            )
        if user_status.status in ["member", "administrator", "creator"]:
            file_id = "BAACAgQAAxkBAAIIkWdV30xHlmg9R6TQF-LjwK-pFQTTAAICDAACt76pUvwTCfBWgLFcNgQ"
            await message.answer_video(
                video=file_id,
                caption="#🍿| Kino Nomi:Pishloq yomg'iri 2\n➖➖➖➖➖➖➖➖➖➖➖➖\n🇺🇿| Tili: O'zbek tilida\n💾| Sifati: Ts format \n🎞️| Janri: Jangari\n⛔️| Ko'rish Kategoriyasi: 18+\n\n🔰| Kanal: @nur02_16\n🗂 Yuklash: 5903\n\n🤖 Bizning bot: @news4sd_bot"
            )
        else:
            await message.answer(
                "⚠️ Siz kanalga obuna bo'lmagansiz! Kanalga obuna bo'ling va qayta urinib ko'ring.",
                reply_markup=check
            )
    except Exception as e:
        await message.answer("❌ Xatolik yuz berdi. Iltimos, qayta urinib ko'ring.")
        logging.error(f"Error in video sending: {e}")


# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
@dp.message(F.text == "63")
async def send_video(message: Message):
    print(f"Foydalanuvchi:Deliha 2")
    try:
        user_status = await bot.get_chat_member(chat_id=CHAT_ID, user_id=message.from_user.id)
        if user_status.status in ["member", "administrator", "creator"]:
            file_id = "BAACAgQAAxkBAAIInGdV94xB3o171dDP6ARUCiCFrr9RAALwGAACFYCoU3vuMSVOa9x-NgQ"
            await message.answer_video(
                video=file_id,
                caption="#🍿| Kino Nomi:Deliha 2 \n➖➖➖➖➖➖➖➖➖➖➖➖\n🇺🇿| Tili: O'zbek tilida\n💾| Sifati: Ts format \n🎞️| Janri: Jangari\n⛔️| Ko'rish Kategoriyasi: 18+\n\n🔰| Kanal: @nur02_16\n🗂 Yuklash: 5903\n\n🤖 Bizning bot: @news4sd_bot"
            )

        else:
            await message.answer(
                "⚠️ Siz kanalga obuna bo'lmagansiz! Kanalga obuna bo'ling va qayta urinib ko'ring.",
                reply_markup=check
            )
    except Exception as e:
        await message.answer("❌ Xatolik yuz berdi. Iltimos, qayta urinib ko'ring.")
        logging.error(f"Error in video sending: {e}")


# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
@dp.message(F.text == "64")
async def send_video(message: Message):
    print(f"Foydalanuvchi:Boltalar qiroli ")
    try:
        user_status = await bot.get_chat_member(chat_id=CHAT_ID, user_id=message.from_user.id)
        if user_status.status in ["member", "administrator", "creator"]:
            file_id = "BAACAgQAAxkBAAIInmdV9-faFEbKE1uPC9DazxGAVfZEAAI_EQACD3SJUb0xWzZ4M_zqNgQ"
            await message.answer_video(
                video=file_id,
                caption="#🍿| Kino Nomi:Boltalar qiroli \n➖➖➖➖➖➖➖➖➖➖➖➖\n🇺🇿| Tili: O'zbek tilida\n💾| Sifati: Ts format \n🎞️| Janri: Jangari\n⛔️| Ko'rish Kategoriyasi: 18+\n\n🔰| Kanal: @nur02_16\n🗂 Yuklash: 5903\n\n🤖 Bizning bot: @news4sd_bot"
            )

        else:
            await message.answer(
                "⚠️ Siz kanalga obuna bo'lmagansiz! Kanalga obuna bo'ling va qayta urinib ko'ring.",
                reply_markup=check
            )
    except Exception as e:
        await message.answer("❌ Xatolik yuz berdi. Iltimos, qayta urinib ko'ring.")
        logging.error(f"Error in video sending: {e}")


# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
@dp.message(F.text == "65")
async def send_video(message: Message):
    print(f"Foydalanuvchi:Yo‘l-yo‘l pijamali bola")
    try:
        user_status = await bot.get_chat_member(chat_id=CHAT_ID, user_id=message.from_user.id)
        if user_status.status in ["member", "administrator", "creator"]:
            file_id = "BAACAgQAAxkBAAIIoGdV-CPEvnermLCZu2ogKthO9JLVAAKsBwACEzzpUyxjDVtHPLvqNgQ"
            await message.answer_video(
                video=file_id,
                caption="#🍿| Kino Nomi:Yo‘l-yo‘l pijamali bola\n➖➖➖➖➖➖➖➖➖➖➖➖\n🇺🇿| Tili: O'zbek tilida\n💾| Sifati: Ts format \n🎞️| Janri: Jangari\n⛔️| Ko'rish Kategoriyasi: 18+\n\n🔰| Kanal: @nur02_16\n🗂 Yuklash: 5903\n\n🤖 Bizning bot: @news4sd_bot"
            )

        else:
            await message.answer(
                "⚠️ Siz kanalga obuna bo'lmagansiz! Kanalga obuna bo'ling va qayta urinib ko'ring.",
                reply_markup=check
            )
    except Exception as e:
        await message.answer("❌ Xatolik yuz berdi. Iltimos, qayta urinib ko'ring.")
        logging.error(f"Error in video sending: {e}")


# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
@dp.message(F.text == "66")
async def send_video(message: Message):
    print(f"Foydalanuvchi:")
    try:
        user_status = await bot.get_chat_member(chat_id=CHAT_ID, user_id=message.from_user.id)
        if user_status.status in ["member", "administrator", "creator"]:
            file_id = "BAACAgEAAxkBAAIIomdV-GSgeESiaoMx2kSzg7wG0e3nAAL5BgAC_XgIRIEIlnBsZH-ONgQ"
            await message.answer_video(
                video=file_id,
                caption="#🍿| Kino Nomi:\n➖➖➖➖➖➖➖➖➖➖➖➖\n🇺🇿| Tili: O'zbek tilida\n💾| Sifati: Ts format \n🎞️| Janri: Jangari\n⛔️| Ko'rish Kategoriyasi: 18+\n\n🔰| Kanal: @nur02_16\n🗂 Yuklash: 5903\n\n🤖 Bizning bot: @news4sd_bot"
            )

        else:
            await message.answer(
                "⚠️ Siz kanalga obuna bo'lmagansiz! Kanalga obuna bo'ling va qayta urinib ko'ring.",
                reply_markup=check
            )
    except Exception as e:
        await message.answer("❌ Xatolik yuz berdi. Iltimos, qayta urinib ko'ring.")
        logging.error(f"Error in video sending: {e}")


# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
@dp.message(F.text == "67")
async def send_video(message: Message):
    print(f"Foydalanuvchi:Forsaj 2")
    try:
        user_status = await bot.get_chat_member(chat_id=CHAT_ID, user_id=message.from_user.id)
        if user_status.status in ["member", "administrator", "creator"]:
            file_id = "BAACAgEAAxkBAAIIpGdV-JQYUpkNVfwhHco4vjYEC_oiAAIiBAAC2pjwRJMKJsGExKT9NgQ"
            await message.answer_video(
                video=file_id,
                caption="#🍿| Kino Nomi:Forsaj 2\n➖➖➖➖➖➖➖➖➖➖➖➖\n🇺🇿| Tili: O'zbek tilida\n💾| Sifati: Ts format \n🎞️| Janri: Jangari\n⛔️| Ko'rish Kategoriyasi: 18+\n\n🔰| Kanal: @nur02_16\n🗂 Yuklash: 5903\n\n🤖 Bizning bot: @news4sd_bot"
            )

        else:
            await message.answer(
                "⚠️ Siz kanalga obuna bo'lmagansiz! Kanalga obuna bo'ling va qayta urinib ko'ring.",
                reply_markup=check
            )
    except Exception as e:
        await message.answer("❌ Xatolik yuz berdi. Iltimos, qayta urinib ko'ring.")
        logging.error(f"Error in video sending: {e}")


# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
@dp.message(F.text == "68")
async def send_video(message: Message):
    print(f"Foydalanuvchi:12yil Qullikda")
    try:
        user_status = await bot.get_chat_member(chat_id=CHAT_ID, user_id=message.from_user.id)
        if user_status.status in ["member", "administrator", "creator"]:
            file_id = "BAACAgEAAxkBAAIIpmdV-NfLSjq5aXZy_W0Ds26XfR-RAAIrBAACbr85RWZXs0MqiB2KNgQ"
            await message.answer_video(
                video=file_id,
                caption="#🍿| Kino Nomi:12yil Qullikda\n➖➖➖➖➖➖➖➖➖➖➖➖\n🇺🇿| Tili: O'zbek tilida\n💾| Sifati: Ts format \n🎞️| Janri: Jangari\n⛔️| Ko'rish Kategoriyasi: 18+\n\n🔰| Kanal: @nur02_16\n🗂 Yuklash: 5903\n\n🤖 Bizning bot: @news4sd_bot"
            )

        else:
            await message.answer(
                "⚠️ Siz kanalga obuna bo'lmagansiz! Kanalga obuna bo'ling va qayta urinib ko'ring.",
                reply_markup=check
            )
    except Exception as e:
        await message.answer("❌ Xatolik yuz berdi. Iltimos, qayta urinib ko'ring.")
        logging.error(f"Error in video sending: {e}")


# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
@dp.message(F.text == "69")
async def send_video(message: Message):
    print(f"Foydalanuvchi:QIZIL MAYOQ")
    try:
        user_status = await bot.get_chat_member(chat_id=CHAT_ID, user_id=message.from_user.id)
        if user_status.status in ["member", "administrator", "creator"]:
            file_id = "BAACAgIAAxkBAAIIqGdV-ToK0pXxgx49JvVzykTgjzZKAAMoAALyoolLrh1EHyVPh0U2BA"
            await message.answer_video(
                video=file_id,
                caption="#🍿| Kino Nomi:QIZIL MAYOQ\n➖➖➖➖➖➖➖➖➖➖➖➖\n🇺🇿| Tili: O'zbek tilida\n💾| Sifati: Ts format \n🎞️| Janri: Jangari\n⛔️| Ko'rish Kategoriyasi: 18+\n\n🔰| Kanal: @nur02_16\n🗂 Yuklash: 5903\n\n🤖 Bizning bot: @news4sd_bot"
            )

        else:
            await message.answer(
                "⚠️ Siz kanalga obuna bo'lmagansiz! Kanalga obuna bo'ling va qayta urinib ko'ring.",
                reply_markup=check
            )
    except Exception as e:
        await message.answer("❌ Xatolik yuz berdi. Iltimos, qayta urinib ko'ring.")
        logging.error(f"Error in video sending: {e}")


# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
@dp.message(F.text == "70")
async def send_video(message: Message):
    print(f"Foydalanuvchi:Kelajak Urushi")
    try:
        user_status = await bot.get_chat_member(chat_id=CHAT_ID, user_id=message.from_user.id)
        if user_status.status in ["member", "administrator", "creator"]:
            file_id = "BAACAgQAAxkBAAII-mdWiRyPxfm5hbe3icgcdz5KxVjCAAJfEgACY7OxUG7OvM4460-8NgQ"
            await message.answer_video(
                video=file_id,
                caption="#🍿| Kino Nomi:Kelajak Urushi\n➖➖➖➖➖➖➖➖➖➖➖➖\n🇺🇿| Tili: O'zbek tilida\n💾| Sifati: Ts format \n🎞️| Janri: Jangari\n⛔️| Ko'rish Kategoriyasi: 18+\n\n🔰| Kanal: @nur02_16\n🗂 Yuklash: 5903\n\n🤖 Bizning bot: @news4sd_bot"
            )

        else:
            await message.answer(
                "⚠️ Siz kanalga obuna bo'lmagansiz! Kanalga obuna bo'ling va qayta urinib ko'ring.",
                reply_markup=check
            )
    except Exception as e:
        await message.answer("❌ Xatolik yuz berdi. Iltimos, qayta urinib ko'ring.")
        logging.error(f"Error in video sending: {e}")


# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
@dp.message(F.text == "71")
async def send_video(message: Message):
    print(f"Foydalanuvchi:Yovvoyi robot")
    try:
        user_status = await bot.get_chat_member(chat_id=CHAT_ID, user_id=message.from_user.id)
        if user_status.status in ["member", "administrator", "creator"]:
            file_id = "BAACAgQAAxkBAAIJTGdXG88bJ_xAJ0d9P10UoJq_bRxTAAJhFQACQALxUD85AmgQFfM4NgQ"
            await message.answer_video(
                video=file_id,
                caption="#🍿| Kino Nomi:Yovvoyi robot\n➖➖➖➖➖➖➖➖➖➖➖➖\n🇺🇿| Tili: O'zbek tilida\n💾| Sifati: Ts format \n🎞️| Janri: Jangari\n⛔️| Ko'rish Kategoriyasi: 18+\n\n🔰| Kanal: @nur02_16\n🗂 Yuklash: 5903\n\n🤖 Bizning bot: @news4sd_bot"
            )

        else:
            await message.answer(
                "⚠️ Siz kanalga obuna bo'lmagansiz! Kanalga obuna bo'ling va qayta urinib ko'ring.",
                reply_markup=check
            )
    except Exception as e:
        await message.answer("❌ Xatolik yuz berdi. Iltimos, qayta urinib ko'ring.")
        logging.error(f"Error in video sending: {e}")


# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
@dp.message(F.text == "72")
async def send_video(message: Message):
    print(f"Foydalanuvchi: Muhabbat masofasi")
    try:
        user_status = await bot.get_chat_member(chat_id=CHAT_ID, user_id=message.from_user.id)
        if user_status.status in ["member", "administrator", "creator"]:
            file_id = "BAACAgIAAxkBAAIJYGdXN174BIkElPTRNkedKb0KZRzQAALCWwAC9ilASmzJKRKcreY4NgQ"
            await message.answer_video(
                video=file_id,
                caption="#🍿| Kino Nomi: Muhabbat masofasi\n➖➖➖➖➖➖➖➖➖➖➖➖\n🇺🇿| Tili: O'zbek tilida\n💾| Sifati: Ts format \n🎞️| Janri: Jangari\n⛔️| Ko'rish Kategoriyasi: 18+\n\n🔰| Kanal: @nur02_16\n🗂 Yuklash: 5903\n\n🤖 Bizning bot: @news4sd_bot"
            )

        else:
            await message.answer(
                "⚠️ Siz kanalga obuna bo'lmagansiz! Kanalga obuna bo'ling va qayta urinib ko'ring.",
                reply_markup=check
            )
    except Exception as e:
        await message.answer("❌ Xatolik yuz berdi. Iltimos, qayta urinib ko'ring.")
        logging.error(f"Error in video sending: {e}")


# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
@dp.message(F.text == "73")
async def send_video(message: Message):
    print(f"Foydalanuvchi:Salaar")
    try:
        user_status = await bot.get_chat_member(chat_id=CHAT_ID, user_id=message.from_user.id)
        if user_status.status in ["member", "administrator", "creator"]:
            file_id = "BAACAgQAAxkBAAIJrGdYck_aNLFbtmKj49d7ZU_BMgHtAAIZFAACrDUhUNuHf4l_6WNjNgQ"
            await message.answer_video(
                video=file_id,
                caption="#🍿| Kino Nomi:Salaar\n➖➖➖➖➖➖➖➖➖➖➖➖\n🇺🇿| Tili: O'zbek tilida\n💾| Sifati: Ts format \n🎞️| Janri: Jangari\n⛔️| Ko'rish Kategoriyasi: 18+\n\n🔰| Kanal: @nur02_16\n🗂 Yuklash: 5903\n\n🤖 Bizning bot: @news4sd_bot"
            )

        else:
            await message.answer(
                "⚠️ Siz kanalga obuna bo'lmagansiz! Kanalga obuna bo'ling va qayta urinib ko'ring.",
                reply_markup=check
            )
    except Exception as e:
        await message.answer("❌ Xatolik yuz berdi. Iltimos, qayta urinib ko'ring.")
        logging.error(f"Error in video sending: {e}")


# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
@dp.message(F.text == "74")
async def send_video(message: Message):
    print(f"Foydalanuvchi:O'lim o'yini")
    try:
        user_status = await bot.get_chat_member(chat_id=CHAT_ID, user_id=message.from_user.id)
        if user_status.status in ["member", "administrator", "creator"]:
            file_id = "BAACAgIAAxkBAAIJrmdYdHTvM5KqmlX1x4lCWO4BHHYIAAJsQQAC14_xS49fqS4MVDUyNgQ"
            await message.answer_video(
                video=file_id,
                caption="#🍿| Kino Nomi:O'lim o'yini\n➖➖➖➖➖➖➖➖➖➖➖➖\n🇺🇿| Tili: O'zbek tilida\n💾| Sifati: Ts format \n🎞️| Janri: Jangari\n⛔️| Ko'rish Kategoriyasi: 18+\n\n🔰| Kanal: @nur02_16\n🗂 Yuklash: 5903\n\n🤖 Bizning bot: @news4sd_bot"
            )

        else:
            await message.answer(
                "⚠️ Siz kanalga obuna bo'lmagansiz! Kanalga obuna bo'ling va qayta urinib ko'ring.",
                reply_markup=check
            )
    except Exception as e:
        await message.answer("❌ Xatolik yuz berdi. Iltimos, qayta urinib ko'ring.")
        logging.error(f"Error in video sending: {e}")


# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
@dp.message(F.text == "75")
async def send_video(message: Message):
    print(f"Foydalanuvchi:Josus do'stlar")
    try:
        user_status = await bot.get_chat_member(chat_id=CHAT_ID, user_id=message.from_user.id)
        if user_status.status in ["member", "administrator", "creator"]:
            file_id = "BAACAgQAAxkBAAIJsGdYdPJZd-2MOSyf-T1LRpPLKWQAA6sHAAK_O8hROFBFM1ybJvQ2BA"
            await message.answer_video(
                video=file_id,
                caption="#🍿| Kino Nomi:Josus do'stlar\n➖➖➖➖➖➖➖➖➖➖➖➖\n🇺🇿| Tili: O'zbek tilida\n💾| Sifati: Ts format \n🎞️| Janri: Jangari\n⛔️| Ko'rish Kategoriyasi: 18+\n\n🔰| Kanal: @nur02_16\n🗂 Yuklash: 5903\n\n🤖 Bizning bot: @news4sd_bot"
            )

        else:
            await message.answer(
                "⚠️ Siz kanalga obuna bo'lmagansiz! Kanalga obuna bo'ling va qayta urinib ko'ring.",
                reply_markup=check
            )
    except Exception as e:
        await message.answer("❌ Xatolik yuz berdi. Iltimos, qayta urinib ko'ring.")
        logging.error(f"Error in video sending: {e}")


# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
@dp.message(F.text == "76")
async def send_video(message: Message):
    print(f"Foydalanuvchi:Ari odamga qarshi ")
    try:
        user_status = await bot.get_chat_member(chat_id=CHAT_ID, user_id=message.from_user.id)
        if user_status.status in ["member", "administrator", "creator"]:
            file_id = "BAACAgQAAxkBAAIJsmdYdWGYqUqTT0dDLDCrmUC6AAGcuwACqAsAAsx68VGdlHlXfT1uVzYE"
            await message.answer_video(
                video=file_id,
                caption="#🍿| Kino Nomi:Ari odamga qarshi \n➖➖➖➖➖➖➖➖➖➖➖➖\n🇺🇿| Tili: O'zbek tilida\n💾| Sifati: Ts format \n🎞️| Janri: Jangari\n⛔️| Ko'rish Kategoriyasi: 18+\n\n🔰| Kanal: @nur02_16\n🗂 Yuklash: 5903\n\n🤖 Bizning bot: @news4sd_bot"
            )

        else:
            await message.answer(
                "⚠️ Siz kanalga obuna bo'lmagansiz! Kanalga obuna bo'ling va qayta urinib ko'ring.",
                reply_markup=check
            )
    except Exception as e:
        await message.answer("❌ Xatolik yuz berdi. Iltimos, qayta urinib ko'ring.")
        logging.error(f"Error in video sending: {e}")


# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
@dp.message(F.text == "77")
async def send_video(message: Message):
    print(f"Foydalanuvchi:Vavilon")
    try:
        user_status = await bot.get_chat_member(chat_id=CHAT_ID, user_id=message.from_user.id)
        if user_status.status in ["member", "administrator", "creator"]:
            file_id = "BAACAgQAAxkBAAIJtGdYdajxX0zhevdXRtIsO2VtN6DyAAJLEwACPY-YUGPNiTlw2gGxNgQ"
            await message.answer_video(
                video=file_id,
                caption="#🍿| Kino Nomi:Vavilon\n➖➖➖➖➖➖➖➖➖➖➖➖\n🇺🇿| Tili: O'zbek tilida\n💾| Sifati: Ts format \n🎞️| Janri: Jangari\n⛔️| Ko'rish Kategoriyasi: 18+\n\n🔰| Kanal: @nur02_16\n🗂 Yuklash: 5903\n\n🤖 Bizning bot: @news4sd_bot"
            )

        else:
            await message.answer(
                "⚠️ Siz kanalga obuna bo'lmagansiz! Kanalga obuna bo'ling va qayta urinib ko'ring.",
                reply_markup=check
            )
    except Exception as e:
        await message.answer("❌ Xatolik yuz berdi. Iltimos, qayta urinib ko'ring.")
        logging.error(f"Error in video sending: {e}")


# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
@dp.message(F.text == "79")
async def send_video(message: Message):
    print(f"Foydalanuvchi: Izquvar 3")
    try:
        user_status = await bot.get_chat_member(chat_id=CHAT_ID, user_id=message.from_user.id)
        if user_status.status in ["member", "administrator", "creator"]:
            file_id = "BAACAgQAAxkBAAIJtmdYdedgstC8mf2Bu70Dc6-EWC3YAALgBQAC57HZUwZDsTpdNFz7NgQ"
            await message.answer_video(
                video=file_id,
                caption="#🍿| Kino Nomi: Izquvar 3\n➖➖➖➖➖➖➖➖➖➖➖➖\n🇺🇿| Tili: O'zbek tilida\n💾| Sifati: Ts format \n🎞️| Janri: Jangari\n⛔️| Ko'rish Kategoriyasi: 18+\n\n🔰| Kanal: @nur02_16\n🗂 Yuklash: 5903\n\n🤖 Bizning bot: @news4sd_bot"
            )

        else:
            await message.answer(
                "⚠️ Siz kanalga obuna bo'lmagansiz! Kanalga obuna bo'ling va qayta urinib ko'ring.",
                reply_markup=check
            )
    except Exception as e:
        await message.answer("❌ Xatolik yuz berdi. Iltimos, qayta urinib ko'ring.")
        logging.error(f"Error in video sending: {e}")


# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
@dp.message(F.text == "80")
async def send_video(message: Message):
    print(f"Foydalanuvchi:Dahshatli masxaraboz 3")
    try:
        user_status = await bot.get_chat_member(chat_id=CHAT_ID, user_id=message.from_user.id)
        if user_status.status in ["member", "administrator", "creator"]:
            file_id = "BAACAgQAAxkBAAIJ0GdYejoCGifNvAJKVlWcuPk2biKvAAKzFgACcY1hUqjZwMe8IRIpNgQ"
            await message.answer_video(
                video=file_id,
                caption="#🍿| Kino Nomi:Dahshatli masxaraboz 3\n➖➖➖➖➖➖➖➖➖➖➖➖\n🇺🇿| Tili: O'zbek tilida\n💾| Sifati: Ts format \n🎞️| Janri: Jangari\n⛔️| Ko'rish Kategoriyasi: 18+\n\n🔰| Kanal: @nur02_16\n🗂 Yuklash: 5903\n\n🤖 Bizning bot: @news4sd_bot"
            )

        else:
            await message.answer(
                "⚠️ Siz kanalga obuna bo'lmagansiz! Kanalga obuna bo'ling va qayta urinib ko'ring.",
                reply_markup=check
            )
    except Exception as e:
        await message.answer("❌ Xatolik yuz berdi. Iltimos, qayta urinib ko'ring.")
        logging.error(f"Error in video sending: {e}")


# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
@dp.message(F.text == "81")
async def send_video(message: Message):
    print(f"Foydalanuvchi:World Disaster 2024")
    try:
        user_status = await bot.get_chat_member(chat_id=CHAT_ID, user_id=message.from_user.id)
        if user_status.status in ["member", "administrator", "creator"]:
            file_id = "BAACAgIAAxkBAAILFmdaa0Q-vaVf6injlAABDPbAkp9FsAACWl0AAk310UrAb_tbRsLP1zYE"
            await message.answer_video(
                video=file_id,
                caption="#🍿| Kino Nomi:World Disaster 2024\n➖➖➖➖➖➖➖➖➖➖➖➖\n🇺🇿| Tili:  O'zbek tilida \n💾| Sifati: Ts format \n🎞️| Janri: Jangari\n⛔️| Ko'rish Kategoriyasi: 18+\n\n🔰| Kanal: @nur02_16\n🗂 Yuklash: 5903\n\n🤖 Bizning bot: @news4sd_bot"
            )

        else:
            await message.answer(
                "⚠️ Siz kanalga obuna bo'lmagansiz! Kanalga obuna bo'ling va qayta urinib ko'ring.",
                reply_markup=check
            )
    except Exception as e:
        await message.answer("❌ Xatolik yuz berdi. Iltimos, qayta urinib ko'ring.")
        logging.error(f"Error in video sending: {e}")


# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
@dp.message(F.text == "82")
async def send_video(message: Message):
    print(f"Foydalanuvchi:parijdagi sarguzashtlar ")
    try:
        user_status = await bot.get_chat_member(chat_id=CHAT_ID, user_id=message.from_user.id)
        if user_status.status in ["member", "administrator", "creator"]:
            file_id = "BAACAgIAAxkBAAIMFWdbAAH1YJsDct4lyKiypEhUymLrzAAC2k8AAt_miEt5xpsa0qAoOjYE"
            await message.answer_video(
                video=file_id,
                caption="#🍿| Kino Nomi:parijdagi sarguzashtlar \n➖➖➖➖➖➖➖➖➖➖➖➖\n🇺🇿| Tili: O'zbek tilida \n💾| Sifati: Ts format \n🎞️| Janri: Jangari\n⛔️| Ko'rish Kategoriyasi: 18+\n\n🔰| Kanal: @nur02_16\n🗂 Yuklash: 5903\n\n🤖 Bizning bot: @news4sd_bot"
            )

        else:
            await message.answer(
                "⚠️ Siz kanalga obuna bo'lmagansiz! Kanalga obuna bo'ling va qayta urinib ko'ring.",
                reply_markup=check
            )
    except Exception as e:
        await message.answer("❌ Xatolik yuz berdi. Iltimos, qayta urinib ko'ring.")
        logging.error(f"Error in video sending: {e}")


# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
@dp.message(F.text == "97")
async def send_video(message: Message):
    print(f"Foydalanuvchi: 12 yil qullik")
    try:
        user_status = await bot.get_chat_member(chat_id=CHAT_ID, user_id=message.from_user.id)
        if user_status.status in ["member", "administrator", "creator"]:
            file_id = "BAACAgIAAxkBAAIYeWfoKR82vmTG1KT4zEmbqsA_es-fAAKKCAAClmj5SxdS9GjRJ7zlNgQ"
            await message.answer_video(
                video=file_id,
                caption="#🍿| Kino Nomi:12 yil qullik\n➖➖➖➖➖➖➖➖➖➖➖➖\n🇺🇿| Tili:  O'zbek tilida \n💾| Sifati: Ts format \n🎞️| Janri: Jangari\n⛔️| Ko'rish Kategoriyasi: 18+\n\n🔰| Kanal: @nur02_16\n🗂 Yuklash: 5903\n\n🤖 Bizning bot: @news4sd_bot"
            )

        else:
            await message.answer(
                "⚠️ Siz kanalga obuna bo'lmagansiz! Kanalga obuna bo'ling va qayta urinib ko'ring.",
                reply_markup=check
            )
    except Exception as e:
        await message.answer("❌ Xatolik yuz berdi. Iltimos, qayta urinib ko'ring.")
        logging.error(f"Error in video sending: {e}")


#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
@dp.message(F.text == "98")
async def send_video(message: Message):
    print(f"Foydalanuvchi: sonic 3")
    try:
        user_status = await bot.get_chat_member(chat_id=CHAT_ID, user_id=message.from_user.id)
        if user_status.status in ["member", "administrator", "creator"]:
            file_id = "BAACAgEAAxkBAAIYe2foKnbzlCcL91O6XFKhmFX2ro0LAAKsAwACMsqgRXvorEE4kgymNgQ"
            await message.answer_video(
                video=file_id,
                caption="#🍿| Kino Nomi:sonic 3\n➖➖➖➖➖➖➖➖➖➖➖➖\n🇺🇿| Tili:  O'zbek tilida\n💾| Sifati: Ts format \n🎞️| Janri: Jangari\n⛔️| Ko'rish Kategoriyasi: 18+\n\n🔰| Kanal: @nur02_16\n🗂 Yuklash: 5903\n\n🤖 Bizning bot: @news4sd_bot"
            )

        else:
            await message.answer(
                "⚠️ Siz kanalga obuna bo'lmagansiz! Kanalga obuna bo'ling va qayta urinib ko'ring.",
                reply_markup=check
            )
    except Exception as e:
        await message.answer("❌ Xatolik yuz berdi. Iltimos, qayta urinib ko'ring.")
        logging.error(f"Error in video sending: {e}")


#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
@dp.message(F.text == "100")
async def send_video(message: Message):
    print(f"Foydalanuvchi:  sening aybing")
    try:
        user_status = await bot.get_chat_member(chat_id=CHAT_ID, user_id=message.from_user.id)
        if user_status.status in ["member", "administrator", "creator"]:
            file_id = "BAACAgIAAxkBAAIYfWfoLAOQ-mGvRWkWcycRogvTw_zDAALMZwACgE-4SCrfPJ-z6DW0NgQ"
            await message.answer_video(
                video=file_id,
                caption="#🍿| Kino Nomi: sening aybing\n➖➖➖➖➖➖➖➖➖➖➖➖\n🇺🇿| Tili:  O'zbek tilida \n💾| Sifati: Ts format \n🎞️| Janri: Jangari\n⛔️| Ko'rish Kategoriyasi: 18+\n\n🔰| Kanal: @nur02_16\n🗂 Yuklash: 5903\n\n🤖 Bizning bot: @news4sd_bot"
            )

        else:
            await message.answer(
                "⚠️ Siz kanalga obuna bo'lmagansiz! Kanalga obuna bo'ling va qayta urinib ko'ring.",
                reply_markup=check
            )
    except Exception as e:
        await message.answer("❌ Xatolik yuz berdi. Iltimos, qayta urinib ko'ring.")
        logging.error(f"Error in video sending: {e}")


# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
@dp.message(F.text == "101")
async def send_video(message: Message):
    print(f"Foydalanuvchi:Jarlik (ha osha kino mergan bola)")
    try:
        user_status = await bot.get_chat_member(chat_id=CHAT_ID, user_id=message.from_user.id)
        if user_status.status in ["member", "administrator", "creator"]:
            file_id = "BAACAgQAAxkBAAIYf2foLSbLCaeGms9xpPI4IRdAkRWAAAIxFQACotoQUtCmeqGLUwgINgQ"
            await message.answer_video(
                video=file_id,
                caption="#🍿| Kino Nomi:Jarlik (ha osha kino mergan bola)\n➖➖➖➖➖➖➖➖➖➖➖➖\n🇺🇿| Tili:  O'zbek tilida \n💾| Sifati: Ts format \n🎞️| Janri: Jangari\n⛔️| Ko'rish Kategoriyasi: 18+\n\n🔰| Kanal: @nur02_16\n🗂 Yuklash: 5903\n\n🤖 Bizning bot: @news4sd_bot"
            )

        else:
            await message.answer(
                "⚠️ Siz kanalga obuna bo'lmagansiz! Kanalga obuna bo'ling va qayta urinib ko'ring.",
                reply_markup=check
            )
    except Exception as e:
        await message.answer("❌ Xatolik yuz berdi. Iltimos, qayta urinib ko'ring.")
        logging.error(f"Error in video sending: {e}")


# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
@dp.message(F.text == "102")
async def send_video(message: Message):
    print(f"Foydalanuvchi:Ovchi Kreyven (2024)")
    try:
        user_status = await bot.get_chat_member(chat_id=CHAT_ID, user_id=message.from_user.id)
        if user_status.status in ["member", "administrator", "creator"]:
            file_id = "BAACAgQAAxkBAAIYgWfoLXbv8JKFE2-dSV1IM_-p4shnAALrFgACB_gRUDbZOmFi3FIYNgQ"
            await message.answer_video(
                video=file_id,
                caption="#🍿| Kino Nomi:Ovchi Kreyven (2024)\n➖➖➖➖➖➖➖➖➖➖➖➖\n🇺🇿| Tili:  O'zbek tilida \n💾| Sifati: Ts format \n🎞️| Janri: Jangari\n⛔️| Ko'rish Kategoriyasi: 18+\n\n🔰| Kanal: @nur02_16\n🗂 Yuklash: 5903\n\n🤖 Bizning bot: @news4sd_bot"
            )

        else:
            await message.answer(
                "⚠️ Siz kanalga obuna bo'lmagansiz! Kanalga obuna bo'ling va qayta urinib ko'ring.",
                reply_markup=check
            )
    except Exception as e:
        await message.answer("❌ Xatolik yuz berdi. Iltimos, qayta urinib ko'ring.")
        logging.error(f"Error in video sending: {e}")


# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
@dp.message(F.text == "103")
async def send_video(message: Message):
    print(f"Foydalanuvchi: ARISTOKRATLAR JAMOASI SHOU KONSERT DASTURI 2024")
    try:
        user_status = await bot.get_chat_member(chat_id=CHAT_ID, user_id=message.from_user.id)
        if user_status.status in ["member", "administrator", "creator"]:
            file_id = "BAACAgIAAxkBAAIaP2frjg3Vw1H2bna4Bx0ntnVQ-ClVAALLYAACPbmAS2gHdpKJdBaoNgQ"
            await message.answer_video(
                video=file_id,
                caption="#🍿| Kino Nomi: ARISTOKRATLAR JAMOASI SHOU KONSERT DASTURI 2024\n➖➖➖➖➖➖➖➖➖➖➖➖\n🇺🇿| Tili:  O'zbek tilida \n💾| Sifati: Ts format \n🎞️| Janri: Jangari\n⛔️| Ko'rish Kategoriyasi: 18+\n\n🔰| Kanal: @nur02_16\n🗂 Yuklash: 5903\n\n🤖 Bizning bot: @nur02_17"
            )

        else:
            await message.answer(
                "⚠️ Siz kanalga obuna bo'lmagansiz! Kanalga obuna bo'ling va qayta urinib ko'ring.",
                reply_markup=check
            )
    except Exception as e:
        await message.answer("❌ Xatolik yuz berdi. Iltimos, qayta urinib ko'ring.")
        logging.error(f"Error in video sending: {e}")


# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
@dp.message(F.text == "96")
async def send_video(message: Message):
    print(f"Foydalanuvchi: :Qabr la’nati")
    try:
        user_status = await bot.get_chat_member(chat_id=CHAT_ID, user_id=message.from_user.id)
        if user_status.status in ["member", "administrator", "creator"]:
            file_id = "BAACAgQAAxkBAAIaS2frzRGh9z45UZIUakCtxrl2DCbHAAJpHgACu2iJUczkMPrMbiocNgQ"
            await message.answer_video(
                video=file_id,
                caption="#🍿| Kino Nomi: Qabr la’nati\n➖➖➖➖➖➖➖➖➖➖➖➖\n🇺🇿| Tili:  O'zbek tilida \n💾| Sifati: Ts format \n🎞️| Janri: Jangari\n⛔️| Ko'rish Kategoriyasi: 18+\n\n🔰| Kanal: @nur02_16\n🗂 Yuklash: 5903\n\n🤖 Bizning bot: @nur02_17"
            )

        else:
            await message.answer(
                "⚠️ Siz kanalga obuna bo'lmagansiz! Kanalga obuna bo'ling va qayta urinib ko'ring.",
                reply_markup=check
            )
    except Exception as e:
        await message.answer("❌ Xatolik yuz berdi. Iltimos, qayta urinib ko'ring.")
        logging.error(f"Error in video sending: {e}")


# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
@dp.message(F.text == "87")
async def send_video(message: Message):
    print(f"Foydalanuvchi: O’LMAS")
    try:
        user_status = await bot.get_chat_member(chat_id=CHAT_ID, user_id=message.from_user.id)
        if user_status.status in ["member", "administrator", "creator"]:
            file_id = "BAACAgIAAxkBAAIaamfutE5eTLOkSb2ca04XNPOMhsDfAAK9ZwACQF14SybbmfQ4WIb7NgQ"
            await message.answer_video(
                video=file_id,
                caption="#🍿| Kino Nomi:  O’LMAS\n➖➖➖➖➖➖➖➖➖➖➖➖\n🇺🇿| Tili:  O'zbek tilida \n💾| Sifati: Ts format \n🎞️| Janri: Jangari\n⛔️| Ko'rish Kategoriyasi: 18+\n\n🔰| Kanal: @nur02_16\n🗂 Yuklash: 5903\n\n🤖 Bizning bot: @nur02_17"
            )

        else:
            await message.answer(
                "⚠️ Siz kanalga obuna bo'lmagansiz! Kanalga obuna bo'ling va qayta urinib ko'ring.",
                reply_markup=check
            )
    except Exception as e:
        await message.answer("❌ Xatolik yuz berdi. Iltimos, qayta urinib ko'ring.")
        logging.error(f"Error in video sending: {e}")


# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
@dp.message(F.text == "88")
async def send_video(message: Message):
    print(f"Foydalanuvchi:Interstellar")
    try:
        user_status = await bot.get_chat_member(chat_id=CHAT_ID, user_id=message.from_user.id)
        if user_status.status in ["member", "administrator", "creator"]:
            file_id = "BAACAgEAAxkBAAIaimfwEeXxsUejYRsiLl8v96VeoBhLAAKgAAMlgfBHd6vMifnVm6s2BA"
            await message.answer_video(
                video=file_id,
                    caption="#🍿| Kino Nomi:Interstellar\n➖➖➖➖➖➖➖➖➖➖➖➖\n🇺🇿| Tili: O'zbek tilida\n💾| Sifati: Ts format \n🎞️| Janri: Jangari\n⛔️| Ko'rish Kategoriyasi: 18+\n\n🔰| Kanal: @nur02_16\n🗂 Yuklash: 5903\n\n🤖 Bizning bot: @news4sd_bot"
            )

        else:
            await message.answer(
                "⚠️ Siz kanalga obuna bo'lmagansiz! Kanalga obuna bo'ling va qayta urinib ko'ring.",
                reply_markup=check
            )
    except Exception as e:
        await message.answer("❌ Xatolik yuz berdi. Iltimos, qayta urinib ko'ring.")
        logging.error(f"Error in video sending: {e}")
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
@dp.message(F.text == "104")
async def send_video(message: Message):
    print(f"Foydalanuvchi:Sahro ovchilari")
    try:
        user_status = await bot.get_chat_member(chat_id=CHAT_ID, user_id=message.from_user.id)
        if user_status.status in ["member", "administrator", "creator"]:
            file_id = "BAACAgQAAxkBAAIbZ2gYwxdOTAxySQzBnwOKi_d60OE6AALmGwACj33IUNVpb9I2mwnSNgQ"
            await message.answer_video(
                video=file_id,
                    caption="#🍿| Kino Nomi:Sahro ovchilari\n➖➖➖➖➖➖➖➖➖➖➖➖\n🇺🇿| Tili: O'zbek tilida\n💾| Sifati: Ts format \n🎞️| Janri: Jangari\n⛔️| Ko'rish Kategoriyasi: 18+\n\n🔰| Kanal: @nur02_16\n🗂 Yuklash: 5903\n\n🤖 Bizning bot: @news4sd_bot"
            )

        else:
            await message.answer(
                "⚠️ Siz kanalga obuna bo'lmagansiz! Kanalga obuna bo'ling va qayta urinib ko'ring.",
                reply_markup=check
            )
    except Exception as e:
        await message.answer("❌ Xatolik yuz berdi. Iltimos, qayta urinib ko'ring.")
        logging.error(f"Error in video sending: {e}")
# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
@dp.message(F.text == "105")
async def send_video(message: Message):
    print(f"Foydalanuvchi:Jinoyat shahri 3")
    try:
        user_status = await bot.get_chat_member(chat_id=CHAT_ID, user_id=message.from_user.id)
        if user_status.status in ["member", "administrator", "creator"]:
            file_id = "BAACAgEAAxkBAAIbbGgY8aMHd0VGRdlsxVEuvFn3r1eFAAJGBAACbkm5RRNWRzJvFsVgNgQ"
            await message.answer_video(
                video=file_id,
                    caption="#🍿| Kino Nomi:Jinoyat shahri 3\n➖➖➖➖➖➖➖➖➖➖➖➖\n🇺🇿| Tili: O'zbek tilida\n💾| Sifati: Ts format \n🎞️| Janri: Jangari\n⛔️| Ko'rish Kategoriyasi: 18+\n\n🔰| Kanal: @nur02_16\n🗂 Yuklash: 5903\n\n🤖 Bizning bot: @news4sd_bot"
            )

        else:
            await message.answer(
                "⚠️ Siz kanalga obuna bo'lmagansiz! Kanalga obuna bo'ling va qayta urinib ko'ring.",
                reply_markup=check
            )
    except Exception as e:
        await message.answer("❌ Xatolik yuz berdi. Iltimos, qayta urinib ko'ring.")
        logging.error(f"Error in video sending: {e}")
async def main() -> None:

    bot = Bot(token=BOT_TOKEN)
    await dp.start_polling(bot)



# ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
@dp.message(F.text == "106")
async def send_video(message: Message):
    print(f"Foydalanuvchi:Bezori yigitlar / Bezorilar Koreya seriali")
    try:
        user_status = await bot.get_chat_member(chat_id=CHAT_ID, user_id=message.from_user.id)
        if user_status.status in ["member", "administrator", "creator"]:
            file_id = "BAACAgIAAxkBAAIbfmgcLEsfNKeOAWBTHh9XOg9jLWOoAAITaAACzzPQS1HhZgeslOTlNgQ"
            await message.answer_video(
                video=file_id,
                caption="#🍿| Kino Nomi:Bezori yigitlar / Bezorilar Koreya seriali\n1 chi qism\n➖➖➖➖➖➖➖➖➖➖➖➖\n🇺🇿| Tili: O'zbek tilida\n💾| Sifati: Ts format \n🎞️| Janri: Jangari\n⛔️| Ko'rish Kategoriyasi: 6+\n\n🔰| Kanal: @nur02_16\n🗂 Yuklash: 5903\n\n🤖 Bizning bot: @news4sd_bot"
            )
        if user_status.status in ["member", "administrator", "creator"]:
            file_id = "BAACAgIAAxkBAAIbgGgcLIMJ6F_3yM1NBmK2xe8Jk1pKAAIUaAACzzPQS2hH6gS9WvF2NgQ"
            await message.answer_video(
                video=file_id,
                caption="#🍿| Kino Nomi:Bezori yigitlar / Bezorilar Koreya seriali\n2 chi qism\n➖➖➖➖➖➖➖➖➖➖➖➖\n🇺🇿| Tili: O'zbek tilida\n💾| Sifati: Ts format \n🎞️| Janri: Jangari\n⛔️| Ko'rish Kategoriyasi: 6+\n\n🔰| Kanal: @nur02_16\n🗂 Yuklash: 5903\n\n🤖 Bizning bot: @news4sd_bot"
            )
        if user_status.status in ["member", "administrator", "creator"]:
            file_id = "BAACAgIAAxkBAAIbhGgcLINIUxUssVezvkQG-P9ORFDSAAJpdgACzzPYS2P3eUcvMA3iNgQ"
            await message.answer_video(
                video=file_id,
                caption="#🍿| Kino Nomi:Bezori yigitlar / Bezorilar Koreya seriali\n3 chi qism\n➖➖➖➖➖➖➖➖➖➖➖➖\n🇺🇿| Tili: O'zbek tilida\n💾| Sifati: Ts format \n🎞️| Janri: Jangari\n⛔️| Ko'rish Kategoriyasi: 6+\n\n🔰| Kanal: @nur02_16\n🗂 Yuklash: 5903\n\n🤖 Bizning bot: @news4sd_bot"
            )
        if user_status.status in ["member", "administrator", "creator"]:
            file_id = "BAACAgIAAxkBAAIbgWgcLIPm-1On_JOUq1hpLtzTBU9kAAL5bgACzzPYSw05uctJlf7GNgQ"
            await message.answer_video(
                video=file_id,
                caption="#🍿| Kino Nomi:Bezori yigitlar / Bezorilar Koreya seriali\n4 chi qism\n➖➖➖➖➖➖➖➖➖➖➖➖\n🇺🇿| Tili: O'zbek tilida\n💾| Sifati: Ts format \n🎞️| Janri: Jangari\n⛔️| Ko'rish Kategoriyasi: 6+\n\n🔰| Kanal: @nur02_16\n🗂 Yuklash: 5903\n\n🤖 Bizning bot: @news4sd_bot"
            )
        if user_status.status in ["member", "administrator", "creator"]:
            file_id = "BAACAgIAAxkBAAIbg2gcLIN8IIIWEwSz8t9QW3dfnyprAAJWdQACzzPYSxcHdASt-rmWNgQ"
            await message.answer_video(
                video=file_id,
                caption="#🍿| Kino Nomi:Bezori yigitlar / Bezorilar Koreya seriali\n5 chi qism\n➖➖➖➖➖➖➖➖➖➖➖➖\n🇺🇿| Tili: O'zbek tilida\n💾| Sifati: Ts format \n🎞️| Janri: Jangari\n⛔️| Ko'rish Kategoriyasi: 6+\n\n🔰| Kanal: @nur02_16\n🗂 Yuklash: 5903\n\n🤖 Bizning bot: @news4sd_bot"
            )
        if user_status.status in ["member", "administrator", "creator"]:
            file_id = "BAACAgIAAxkBAAIbgmgcLIMyzXOqDbkjohvXscoDu92XAAJfbAACzzPYS1bS0tfjcv8dNgQ"
            await message.answer_video(
                video=file_id,
                caption="#🍿| Kino Nomi:Bezori yigitlar / Bezorilar Koreya seriali\n6 chi qism\n➖➖➖➖➖➖➖➖➖➖➖➖\n🇺🇿| Tili: O'zbek tilida\n💾| Sifati: Ts format \n🎞️| Janri: Jangari\n⛔️| Ko'rish Kategoriyasi: 6+\n\n🔰| Kanal: @nur02_16\n🗂 Yuklash: 5903\n\n🤖 Bizning bot: @news4sd_bot"
            )

        else:
            await message.answer(
                "⚠️ Siz kanalga obuna bo'lmagansiz! Kanalga obuna bo'ling va qayta urinib ko'ring.",
                reply_markup=check
            )
    except Exception as e:
        await message.answer("❌ Xatolik yuz berdi. Iltimos, qayta urinib ko'ring.")
        logging.error(f"Error in video sending: {e}")


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
