import random
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Данные для рун
runes = [
    "Феху (Богатство)", "Уруз (Сила)", "Турисаз (Защита)", "Ансуз (Знание)",
    # ... остальные руны
]

# Данные для карт Ленорман
cards = [
    "1. Всадник (Новости)", "2. Клевер (Удача)", "3. Корабль (Путешествие)",
    # ... все 36 карт
]

def rune_of_day(update: Update, context: CallbackContext):
    rune = random.choice(runes)
    update.message.reply_text(f"Руна дня: {rune}")

def card_of_day(update: Update, context: CallbackContext):
    card = random.choice(cards)
    update.message.reply_text(f"Карта дня: {card}")

def main():
    updater = Updater("7759509225:AAHtyCpSdoC4l9Maij1n5mESuVe5IiulsyQ")  # Замените на токен бота
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("rune", rune_of_day))
    dp.add_handler(CommandHandler("card", card_of_day))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
