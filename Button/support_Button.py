from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

keyboard = InlineKeyboardMarkup(row_width=1)
Btn1 = InlineKeyboardButton(text="پیج افرا", url="https://www.instagram.com/elias.officall")# باید تغییر کنه
Btn2 = InlineKeyboardButton(text="پیج برنامه نویس", url="https://www.instagram.com/elias.officall")# باید تغییر کنه
Btn3 = InlineKeyboardButton(text="سایت آموزشی ما", url="https://persionamooz.ir")# باید تغییر کنه

keyboard.add(Btn1,Btn2,Btn3)