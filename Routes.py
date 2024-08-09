import re

class Routes:
    MENU = "/menu"
    CREATE_ORDER = "/create_order"
    PRODUCT = "/products"
    GET_MY_ORDERS = "/get_my_orders"
    REGISTER_ORDER = re.compile(r'^Order:.*')