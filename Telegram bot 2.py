from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Функція для відповіді на команду /start
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hi! Send me "Hi" and I will reply with "Very good"!')

# Функція для обробки текстових повідомлень
def handle_message(update: Update, context: CallbackContext) -> None:
    if update.message.text.lower() == 'hi':
        update.message.reply_text('Very good')

def main() -> None:
    # Замініть 'YOUR_TOKEN' на ваш токен, отриманий від BotFather
    updater = Updater("7455231817:AAG50eOwrdsMDucP8dZxr6AaoysoR0nH-4s")

    dispatcher = updater.dispatcher

    # Обробник для команди /start
    dispatcher.add_handler(CommandHandler("start", start))

    # Обробник для текстових повідомлень
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    # Запуск бота
    updater.start_polling()

    # Утримання бота в робочому стані до завершення
    updater.idle()

if __name__ == "__main__":
    main()