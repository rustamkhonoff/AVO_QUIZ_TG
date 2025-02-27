import os
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, WebAppInfo
from aiogram.filters import Command
from dotenv import load_dotenv

# Загружаем переменные окружения
load_dotenv()

# Берём токен и URL из .env
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
    """Обрабатывает команду /start и отправляет Web App кнопку"""
    username = message.from_user.username or "Guest"
    first_name = message.from_user.first_name or "Unknown"
    user_id = message.from_user.id

    # Формируем ссылку с параметрами
    user_url = f"{BASE_URL}?user={message.from_user}&name={first_name}&id={user_id}"

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
