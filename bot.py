import random
import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# Список рун
runes = [
    ("Феху", "Богатство, начало, успех"),
    ("Уруз", "Сила, здоровье, энергия"),
    ("Турисаз", "Испытание, защита, внутренний рост"),
    ("Ансуз", "Знание, вдохновение, речь"),
    ("Райдо", "Путь, путешествие, движение"),
    ("Кеназ", "Прояснение, креативность, факел"),
    # Добавь остальные по желанию
]

# Список карт Ленорман
lenormand = [
    ("Клевер", "Удача, шанс, легкость"),
    ("Всадник", "Новости, движение, перемены"),
    ("Корабль", "Путешествие, торговля, движение вперед"),
    ("Дом", "Семья, безопасность, традиции"),
    ("Дерево", "Рост, здоровье, духовность"),
    # Добавь остальные по желанию
]

# Стартовая команда
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Руна дня", callback_data="rune")],
        [InlineKeyboardButton("Ленорман дня", callback_data="lenormand")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Выбери гадание:", reply_markup=reply_markup)

# Обработка кнопок
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "rune":
        symbol = random.choice(runes)
        await query.edit_message_text(text=f"Руна дня: {symbol[0]}\nЗначение: {symbol[1]}")
    elif query.data == "lenormand":
        card = random.choice(lenormand)
        await query.edit_message_text(text=f"Карта Ленорман: {card[0]}\nЗначение: {card[1]}")

# Запуск бота
if __name__ == '__main__':
    TOKEN = os.getenv("TOKEN")  # Получение токена из переменных окружения
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))

    print("Бот запущен...")
    app.run_polling()
