import os
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, WebAppInfo
from aiogram.filters import Command
from dotenv import load_dotenv


load_dotenv()

TOKEN = os.getenv("TOKEN")
URL = "https://avo-quiz-pub.vercel.app"


bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: Message):
    keyboard = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="🎮 Играть", web_app=WebAppInfo(url=URL))]],
        resize_keyboard=True
    )
    await message.answer("Нажмите кнопку ниже, чтобы открыть игру прямо в Telegram!", reply_markup=keyboard)

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
