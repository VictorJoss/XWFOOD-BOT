from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def say_hello(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hola my friend")

TOKEN = "BOT_TOKEN"

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", say_hello))

app.run_polling(allowed_updates=Update.ALL_TYPES)