from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler, CallbackContext
from SheetsService import SheetsService
from MenuTemplate import MenuTemplate
from Routes import Routes
from telegram.constants import ParseMode


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text, reply_markup = MenuTemplate.get_principal_menu_view()
    await update.message.reply_text(text, reply_markup=reply_markup, parse_mode=ParseMode.MARKDOWN)

async def show_menu(update: Update, context: CallbackContext):
    text, reply_markup = MenuTemplate.get_principal_menu_view()
    await update.callback_query.answer()
    await update.callback_query.message.edit_text(text, reply_markup=reply_markup, parse_mode=ParseMode.MARKDOWN)


async def show_products(update: Update, context: CallbackContext):
    all_value = sheet.sheet1.get_all_values()
    message = update.callback_query.message
    text, reply_markup = MenuTemplate.get_products_vew_from_table_values(all_value)
    await update.callback_query.answer()
    await message.edit_text(text, reply_markup=reply_markup, parse_mode=ParseMode.MARKDOWN)

async def make_order(update: Update, context: CallbackContext):
    all_value = sheet.sheet1.get_all_values()
    message = update.callback_query.message
    text, reply_markup = MenuTemplate.get_create_order_view(all_value)
    await update.callback_query.answer()
    await message.edit_text(text, reply_markup=reply_markup)
    pass

async def register_order(update: Update, context: CallbackContext):
    message = update.callback_query.message
    username = update.effective_user.username
    full_name = update.effective_user.full_name
    product_name = update.callback_query.data.split(":")[1]
    worksheet = sheet.get_worksheet(1)
    worksheet.append_row([username, full_name, product_name])
    await update.callback_query.answer()
    await message.reply_text(f"Pedido realizado: {product_name}")
    pass

async def get_my_orders(update: Update, context: CallbackContext):
    worksheet = sheet.get_worksheet(1)
    all_values = worksheet.get_all_values()
    username = update.effective_user.username
    message = update.callback_query.message
    text, reply_markup = MenuTemplate.get_my_orders_view(all_values, username)
    await update.callback_query.answer()
    await message.edit_text(text, reply_markup=reply_markup)
    

TOKEN = "BOT_TOKEN"
app = ApplicationBuilder().token(TOKEN).build()

sheetConfig = SheetsService("creds.json")
sheet = sheetConfig.get_sheet_by_id("SHEET_ID")


app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(show_products, pattern=Routes.PRODUCTS))
app.add_handler(CallbackQueryHandler(show_menu, pattern=Routes.MENU))
app.add_handler(CallbackQueryHandler(make_order, pattern=Routes.CREATE_ORDER))
app.add_handler(CallbackQueryHandler(register_order, pattern=Routes.REGISTER_ORDER))
app.add_handler(CallbackQueryHandler(get_my_orders, pattern=Routes.GET_MY_ORDERS))
app.run_polling(allowed_updates=Update.ALL_TYPES)