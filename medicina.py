from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery

# Sizning tokeningiz
TOKEN = "py"

# PythonAnywhere bepul serveri uchun Proxy (Telegramga ulanish uchun shart)
PROXY_URL = "http://proxy.server:3128"

# Botni proxy orqali ishga tushiramiz
bot = Bot(token=TOKEN, parse_mode=types.ParseMode.HTML, proxy=PROXY_URL)
dp = Dispatcher(bot)

# ================= MENYULAR =================

# 1. Asosiy menyu
categoryMenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🤖 AI Medicina", callback_data="AI Medical"),
            InlineKeyboardButton(text="🏥 Telemedicina", callback_data="Telemedical")
        ]
    ]
)

# 2. AI Medicina menyusi
AIMedicalMenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="AI Diagnostika", url="https://youtu.be/ihUkabnNIvU?si=eg_XNB9GEPlpVDzt")
        ],
        [
            InlineKeyboardButton(text="Robot-xirurglar jumisi", url="https://youtu.be/_8LT1qY-Qnk?si=uMIq4kebEfaQNnl6")
        ],
        [
            InlineKeyboardButton(text="MSKT (multispiral kompyuter tomografiyasi)", url="https://youtu.be/Tp7E6K-NuOU?si=Oyh8AMo5L3_youvo")
        ],
        [
            InlineKeyboardButton(text="⬅️ Izge", callback_data="category")
        ]
    ]
)

# 3. Telemedicina menyusi
TelemedicalMenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Onlayn konsultatsiya", url="https://youtu.be/5kwpR9x1PRw?si=LUK3UpmBkRwiuuIO")
        ],
        [
            InlineKeyboardButton(text="Telediagnostika", url="https://renessans-edu.uz/files/books/2023-11-09-10-38-17_4a4350a018c227fa9a45a0edf2232736.pdf")
        ],
        [
            InlineKeyboardButton(text="Elektron recept hám maǵlıwmat", url="http://renessans-edu.uz/files/books/2023-10-19-05-55-13_b6058ea6582ff3915cc74c84089b3f8a.pdf")
        ],
        [
            InlineKeyboardButton(text="⬅️ Izge", callback_data="category")
        ]
    ]
)


# ================= FUNKSIYALAR =================

# /start buyrug'i bosilganda
@dp.message_handler(commands=["start"])
async def hello(msg: Message):
    await msg.answer(text="Salem! Bólimlerdi saylań:", reply_markup=categoryMenu)

# "Medicina AI" deb yozilganda
@dp.message_handler(text="Medicina AI")
async def vrug(msg: Message):
    await msg.answer(text="Bólimlerdi saylań:", reply_markup=categoryMenu)


# "AI Medicina" tugmasi bosilganda
@dp.callback_query_handler(text="AI Medical")
async def ai_medical_answer(call: CallbackQuery):
    # Eski xabarni yangisiga o'zgartiramiz (chat to'lib ketmasligi uchun)
    await call.message.edit_text(text="🤖 AI Medicina bólimi:", reply_markup=AIMedicalMenu)
    await call.answer()


# "Telemedicina" tugmasi bosilganda
@dp.callback_query_handler(text="Telemedical")
async def open_books(call: CallbackQuery):
    await call.message.edit_text(text="🏥 Telemedicina bólimi:", reply_markup=TelemedicalMenu)
    await call.answer()


# "Izge" (Orqaga) tugmasi bosilganda
@dp.callback_query_handler(text="category")
async def category_answer(call: CallbackQuery):
    await call.message.edit_text(text="Tiykarǵı bólimlerdi saylań:", reply_markup=categoryMenu)
    await call.answer()


if __name__ == '__main__':
    # Botni xatoliklarsiz ishga tushirish
    executor.start_polling(dp, skip_updates=True)