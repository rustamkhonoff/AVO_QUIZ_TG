import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")
URL = "https://avo-quiz-pub.vercel.app"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("🎮 Запустить!", url=URL))
    await message.answer("Нажмите кнопку ниже, чтобы начать!:", reply_markup=keyboard)

async def main():
    await dp.start_polling()

if __name__ == "__main__":
    asyncio.run(main())
