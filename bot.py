import os
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, WebAppInfo
from aiogram.filters import Command
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")
BASE_URL = "https://avo-quiz-pub.vercel.app"  # Замените на ваш URL

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: Message):
    username = message.from_user.username or "Guest"  # Если нет username, то "Guest"
    user_url = f"{BASE_URL}?user={username}"  # Добавляем параметр в URL

    keyboard = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="🎮 Начать!", web_app=WebAppInfo(url=user_url))]],
        resize_keyboard=True
    )
    await message.answer("Нажмите кнопку ниже, чтобы начать игру! 🎮", reply_markup=keyboard)

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
