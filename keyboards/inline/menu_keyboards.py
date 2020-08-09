from aiogram.utils.callback_data import CallbackData

menu_cd = CallbackData("show_menu", "level", "subcategory", "item_url")

async def make_callback_data(level, category="0", subcategory="0", item_url=0):
    return menu_cd.new(level=level, category=category,
                       subcategory=subcategory, item_url=item_url)

async def categories_keyboard():
    CURRENT LEVEL = 0
