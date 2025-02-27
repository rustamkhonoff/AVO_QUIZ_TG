from telegram import Bot, InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackContext

TOKEN = "YOUR_BOT_TOKEN"
WEBGL_URL = "https://avo-quiz-pub.vercel.app/"

def start(update: Update, context: CallbackContext) -> None:
    username = update.message.from_user.username
    user_url = f"{WEBGL_URL}?user={username}"

    keyboard = [
        [InlineKeyboardButton("🎮 Play Now", web_app={"url": user_url})]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    update.message.reply_text(
        "Click below to play the game inside Telegram! 🚀",
        reply_markup=reply_markup
    )

updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher
dp.add_handler(CommandHandler("start", start))
updater.start_polling()
updater.idle()
