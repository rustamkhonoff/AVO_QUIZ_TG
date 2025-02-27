import os
import asyncio
import json
import urllib.parse
from aiogram import Bot, Dispatcher
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, WebAppInfo
from aiogram.filters import Command
from dotenv import load_dotenv


load_dotenv()


TOKEN = os.getenv("TOKEN")
BASE_URL = os.getenv("BASE_URL")

if not TOKEN or not BASE_URL:
    raise ValueError("Ошибка: переменные окружения TOKEN или BASE_URL не заданы!")

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: Message):
    user_data = {
        "id": message.from_user.id,
        "is_bot": message.from_user.is_bot,
        "first_name": message.from_user.first_name,
        "last_name": message.from_user.last_name,
        "username": message.from_user.username,
        "language_code": message.from_user.language_code,
        "can_join_groups": message.from_user.can_join_groups,
        "can_read_all_group_messages": message.from_user.can_read_all_group_messages,
        "supports_inline_queries": message.from_user.supports_inline_queries
    }
    user_json = json.dumps(user_data)
    encoded_user_json = urllib.parse.quote(user_json)

    user_url = f"{BASE_URL}?user_data={encoded_user_json}"

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
