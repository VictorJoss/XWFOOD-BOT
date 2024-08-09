from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from Routes import Routes
from typing import Tuple

class MenuTemplate:

     @staticmethod
     def get_principal_menu_view() -> tuple[str, InlineKeyboardMarkup]:
          
          menu_view_text = "XWFOOD MENÚ"
          keyboard = [
               [InlineKeyboardButton("👀 Ver productos", callback_data=Routes.PRODUCTS)],
               [InlineKeyboardButton("🛒 Ver mis pedidos", callback_data=Routes.GET_MY_ORDERS)],
               [InlineKeyboardButton("🤙🏼 Hacer un pedido", callback_data=Routes.CREATE_ORDER)]
          ]
          return menu_view_text, keyboard