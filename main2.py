import aiogram
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor

TOKEN = ""
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def on_start(msg: types.Message):
    option_lang = ReplyKeyboardMarkup(resize_keyboard=True).row(KeyboardButton("Uz"), KeyboardButton("Ру"))
    await bot.send_message(msg.from_user.id, "Tilni tanlang  \nВыберите язык", reply_markup=option_lang)


@dp.message_handler(text="Uz")
async def on_start(msg: types.Message):
    # option_btn = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton("Encode oquv markazi haqida")).row(KeyboardButton("Darslar"), KeyboardButton("Aloqa")).add(KeyboardButton("Manzil"))
    await bot.send_message(msg.from_user.id,
                           "Assalomu aleykum.Encode school o'quv markazining botiga xush kelibsiz")  # ,reply_markup=option_btn)


if name == "main":
    executor.start_polling(dp)