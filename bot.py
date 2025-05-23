import random
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
    # добавь остальные
]

# Список карт Ленорман
lenormand = [
    ("Клевер", "Удача, шанс, легкость"),
    ("Всадник", "Новости, движение, перемены"),
    ("Корабль", "Путешествие, торговля, движение вперед"),
    ("Дом", "Семья, безопасность, традиции"),
    ("Дерево", "Рост, здоровье, духовность"),
    # добавь остальные
]

# Стартовое сообщение с кнопками
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

# Основной запуск
if __name__ == '__main__':
    TOKEN = 7759509225:AAG4KZzoULdb8kM91H38bF8q_J3-8Yk5C5k

    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))

    print("Бот запущен...")
    app.run_polling()
