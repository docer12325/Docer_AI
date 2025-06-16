from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import openai
import os

TOKEN = os.getenv("7716344841:AAH7KPM-prv4bVvAb0TbA3e3RAGjlZmeSvc")
OPENAI_KEY = os.getenv("proj-bpe7cFPZm79PS-mH5fBoy7ZUoAH1D5JTy-DUiPNDlBT0lbpvHQjU-6-YBp0RRRuZNuazecYy_MT3BlbkFJ3fA0kQf60YI2V2aqKWJH3kqX_r8ymsA_M-17nJv1XRjvE8GeRT-8UoAObvc2obZlLdEhhdVMwA") # Ключ от OpenAI

openai.api_key = OPENAI_KEY

async def chat_gpt(update: Update, context: CallbackContext):
    user_text = update.message.text
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_text}]
    )
    answer = response.choices[0].message["content"]
    await update.message.reply_text(answer)

def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, chat_gpt))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
