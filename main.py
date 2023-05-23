import aiogram
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor
import os

TOKEN = "5893925659:AAEO79yU45vxTlsTOXrbLwssMhe-MPvgeDw"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Main page

@dp.message_handler(commands=["start"])
async def start_command(msg: types.Message):
    option_lang = ReplyKeyboardMarkup(resize_keyboard=True).row(
        KeyboardButton("Uzbek"), KeyboardButton("Russian"), KeyboardButton("English")
    )
    await bot.send_message(
        msg.from_user.id,
        "Tilni tanlang\nВыберите язык\nChoose your language",
        reply_markup=option_lang,
    )

@dp.message_handler(text="Uzbek")
async def uzbek_language(msg: types.Message):
    option_btn = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton("Back to menu"))
    await bot.send_message(
        msg.from_user.id, "Assalomu aleykum! Comfort marketing botiga xush kelibsiz", reply_markup=option_btn
    )

@dp.message_handler(text="Russian")
async def russian_language(msg: types.Message):
    option_btn = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton("Back to menu"))
    await bot.send_message(
        msg.from_user.id, "Здравствуйте, добро пожаловать в бот Центра Маркетинга Комфорт", reply_markup=option_btn
    )

@dp.message_handler(text="English")
async def english_language(msg: types.Message):
    option_btn = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton("Back to menu"))
    await bot.send_message(
        msg.from_user.id, "Good afternoon ladies and gentlemen! Welcome to Comfort marketing telegram bot", reply_markup=option_btn
    )

@dp.message_handler(text="Back to menu")
async def back_to_menu(msg: types.Message):
    option_btn1 = ReplyKeyboardMarkup(resize_keyboard=True).row(
        KeyboardButton("Comfort marketing haqida"),
        KeyboardButton("Comfort marketing Aloqa"),
        KeyboardButton("Comfort marketing tarif rejalari"),
        KeyboardButton("Ortga"),
    )
    await bot.send_message(
        msg.from_user.id,
        "Assalomu aleikum! Sizga qanday yordam bera olamiz? Iltimos quyidagilardan birini tanlang",
        reply_markup=option_btn1,
    )

# Main information part

@dp.message_handler(text="Comfort marketing haqida")
async def about_comfort_marketing(msg: types.Message):
    await bot.send_message(
        msg.from_user.id, "Assalomu aleykum! Comfort marketing botiga xush kelibsiz."
                          " Biz Comfort marketing jamoasi O'zbekistonda yirik marketing jamoasi tuzish va biznes egalari va shaxsiy brand va mahsulot"
                          " brandlarini bozor segmentidan kelib chiqqan holda O'zbekison bozorida yuqori o'rinlarga olib chiqsh va savdoni oshirish va biz bu yo'lda Social media va Digital M"
                          "marketing bozor va reklama strategiyalaridan foydalanamiz yani biz faqatgina instagram va facebook bilan cheklanibgina qolmay Google yandexdan ham foydalanamiz"
    )


# Start the bot
if __name__ == "__main__":
    executor.start_polling(dp)
