import os
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✨ Привет! Я бот для гаданий. Используй /rune или /card.")

# Команда /rune (руна дня)
async def rune_of_day(update: Update, context: ContextTypes.DEFAULT_TYPE):
    runes = [
        "Феху (Богатство)", "Уруз (Сила)", "Турисаз (Защита)", 
        "Ансуз (Знание)", "Райдо (Путешествие)", "Кано (Озарение)",
        # ... добавьте все 24 руны
    ]
    chosen_rune = random.choice(runes)
    await update.message.reply_text(f"🔮 Руна дня: {chosen_rune}")

# Команда /card (карта Ленорман)
async def card_of_day(update: Update, context: ContextTypes.DEFAULT_TYPE):
    cards = [
        "1. Всадник (Новости)", "2. Клевер (Удача)", "3. Корабль (Путешествие)",
        # ... добавьте все 36 карт
    ]
    chosen_card = random.choice(cards)
    await update.message.reply_text(f"🃏 Карта дня: {chosen_card}")

# Настройка и запуск бота
def main():
    # Получаем токен из переменных окружения
    token = os.getenv("BOT_TOKEN")
    if not token:
        raise ValueError("Токен бота не найден! Добавьте BOT_TOKEN в Environment Variables.")

    # Создаем Application
    app = Application.builder().token(token).build()

    # Регистрируем команды
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("rune", rune_of_day))
    app.add_handler(CommandHandler("card", card_of_day))

    # Запускаем бота
    print("Бот запущен...")
    app.run_polling()

if __name__ == "__main__":
    import random  # Для случайного выбора рун/карт
    main()
