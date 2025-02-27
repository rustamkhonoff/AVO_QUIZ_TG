import os
import asyncio
import json
import urllib.parse
from aiogram import Bot, Dispatcher
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, WebAppInfo
from aiogram.filters import Command
from dotenv import load_dotenv

# Загружаем переменные окружения
load_dotenv()

# Берем токен и URL из .env
TOKEN = os.getenv("TOKEN")
BASE_URL = os.getenv("BASE_URL")  # Читаем Web App URL из .env

# Проверяем, загружены ли переменные
if not TOKEN or not BASE_URL:
    raise ValueError("Ошибка: переменные окружения TOKEN или BASE_URL не заданы!")

# Создаём бота и диспетчер
bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: Message):
    """Обрабатывает команду /start и отправляет Web App кнопку со всеми данными о пользователе"""

    # Получаем все данные из from_user
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

    # Конвертируем данные в JSON и кодируем для передачи в URL
    user_json = json.dumps(user_data)
    encoded_user_json = urllib.parse.quote(user_json)

    # Формируем ссылку с JSON параметром
    user_url = f"{BASE_URL}?user_data={encoded_user_json}"

    # Создаём клавиатуру с Web App кнопкой
    keyboard = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="🎮 Начать!", web_app=WebAppInfo(url=user_url))]],
        resize_keyboard=True
    )

    # Отправляем сообщение с кнопкой
    await message.answer("Нажмите кнопку ниже, чтобы начать игру! 🎮", reply_markup=keyboard)

async def main():
    """Главная асинхронная функция"""
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
