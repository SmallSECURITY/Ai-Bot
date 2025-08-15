import telebot
import requests
from Button.support_Button import keyboard
# --- تنظیمات ---
TELEGRAM_API_TOKEN = 'َApi token خود را وارد کنید '
GROQ_API_KEY = 'کلید api خود را اینجا قرار دهید '

bot = telebot.TeleBot(TELEGRAM_API_TOKEN, parse_mode="Markdown")

user_histories = {}

def clean_text(text):
    # حذف فاصله اضافی و خطوط اضافی
    return " ".join(text.strip().split())

def chat_with_groq(user_id, prompt):
    if user_id not in user_histories:
        user_histories[user_id] = [
            {"role": "system", "content": (
                "تو یک دستیار هوشمند فارسی هستی. پاسخ‌هایت باید مرتب، خوانا و با قالب‌بندی Markdown باشند.\n"
                "از تیترهای بولد (مثل ### برای عنوان‌ها)، لیست‌های نشانه‌گذاری شده (-) و اموجی‌ها استفاده کن تا متن جذاب و ساده برای خواندن باشد.\n"
                "پاسخ‌ها را به پاراگراف‌های کوتاه تقسیم کن و از فاصله مناسب بین پاراگراف‌ها استفاده کن.\n"
                "در انتهای هر پاسخ، عبارت زیر را اضافه کن:\n"
                "— توسعه داده شده توسط تیم آموزشی پرشین آموز 🌟"
            )}
        ]
    user_histories[user_id].append({"role": "user", "content": prompt})

    # محدود کردن طول تاریخچه پیام‌ها
    if len(user_histories[user_id]) > 20:
        user_histories[user_id] = user_histories[user_id][-20:]

    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "llama3-70b-8192",
        "messages": user_histories[user_id],
        "max_tokens": 1500,
        "temperature": 0.8
    }

    response = requests.post(url, headers=headers, json=data).json()

    if "choices" in response and len(response["choices"]) > 0:
        bot_reply = response["choices"][0]["message"]["content"]
    else:
        bot_reply = "⚠️ پاسخ نامعتبر از سرور دریافت شد."

    bot_reply = clean_text(bot_reply)
    # نیازی به اضافه کردن دستی پیام توسعه داده شده نیست چون مدل خودش اضافه می‌کند
    user_histories[user_id].append({"role": "assistant", "content": bot_reply})

    return bot_reply


# جوین به گروه
@bot.message_handler(commands=["new_chat_members"])
def new_chat_member(message):
    for member in message.new_chat_members:
        name = message.new_chat_members[0].first_name
        is_bot = message.new_chat_members[0].is_bot
        print(message)
  
        if (is_bot == False):
            text_msg =  f"""
سلام {name} به گروه ما خوش آمدید
 وضعیت شما کاربر 🙋‍♂️
"""
            bot.reply_to(message,text_msg)
        
        elif(is_bot == True):
            text_msg =  f"""
سلام {name} به گروه ما خوش آمدید
 وضعیت شما ربات 🤖
"""
            bot.reply_to(message,text_msg)

# شروع ربات 
@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcome_text = (
        "سلام! 🤖 من دستیار فارسی شما هستم.\n"
        "برای شروع چت لطفا پیام‌هات رو با /chat شروع کن.\n"
        "مثال: /chat سلام، حالت چطوره؟\n\n"
        "— توسعه داده شده توسط تیم آموزشی پرشین آموز 🌟"
    )
    bot.reply_to(message, welcome_text)

# اطلاعات برنامه نویس
@bot.message_handler(commands=["programmer"])
def program(message):
    text = ("""
            اطلاعات برنامه نویس

👨‍💻 **Programmer:** @eliaspro  
📢 **Channel:** @minyhack  
📜 **License:** persionamooz.ir
🤖 **AI:** GROQ

""")
    bot.reply_to(message=message,text=text)

# راه های ارتباطی با پشتیبانی
@bot.message_handler(commands=["support"])
def support_handler(message):
    bot.send_message(chat_id=message.chat.id, text="اطلاعات پشتیبانی و برنامه نویس", reply_markup=keyboard)

# کنترل چت ربات
@bot.message_handler(commands=['chat'])
def handle_chat(message):
    user_id = message.from_user.id
    user_input = message.text[5:].strip()  # حذف "/chat" و فضای اضافی

    if not user_input:
        bot.reply_to(message, "❌ لطفا بعد از /chat یک پیام وارد کنید.")
        return

    try:
        response = chat_with_groq(user_id, user_input)
    except Exception as e:
        response = f"❌ خطا در پردازش درخواست: {e}\n\n— توسعه داده شده توسط تیم آموزشی پرشین آموز 🌟"

    bot.reply_to(message, response)

# ایگنور کردن پیام ها
@bot.message_handler(func=lambda message: True)
def ignore_other_messages(message):
    # پیام‌هایی که با /chat شروع نشده‌اند را نادیده می‌گیریم
    pass



if __name__ == "__main__":
    print("🤖 Persian Assistant Bot is running with Groq + Markdown + Emojis...")
    bot.polling(none_stop=True)
