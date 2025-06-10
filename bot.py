import os
import openai
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Установка токенов
TELEGRAM_TOKEN = os.getenv("7716344841:AAH7KPM-prv4bVvAb0TbA3e3RAGjlZmeSvc")  # Токен вашего Telegram-бота
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")  # Ваш ключ API OpenAI

openai.api_key = OPENAI_API_KEY

# Команда /start
def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Привет! Я ИИ бот. Как я могу помочь вам сегодня?"
    )

# Обработка текстовых сообщений
def respond_to_message(update: Update, context: CallbackContext):
    user_message = update.message.text

    try:
        # Генерация ответа с использованием OpenAI
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Укажите нужную модель
            messages=[{"role": "user", "content": user_message}]
        )
        bot_reply = response.choices[0].message['content']
        update.message.reply_text(bot_reply)
    except Exception as e:
        update.message.reply_text("Произошла ошибка. Попробуйте еще раз.")
        print(e)

def main():
    # Создание бота
    updater = Updater(7716344841:AAH7KPM-prv4bVvAb0TbA3e3RAGjlZmeSvc)

    dispatcher = updater.dispatcher

    # Обработка команд
    dispatcher.add_handler(CommandHandler("start", start))

    # Обработка текстовых сообщений
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, respond_to_message))

    # Запуск бота
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
