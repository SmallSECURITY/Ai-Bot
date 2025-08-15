![My Image](https://github.com/SmallSECURITY/Ai-Bot/blob/main/Aichat.png?raw=true)
# Persian Assistant Bot – ربات دستیار فارسی

---

## English Version

### Overview

Persian Assistant Bot is a Telegram bot that provides interactive AI-powered chat in Persian using **Groq API**.
It supports Markdown formatting, emojis, and maintains conversation history per user.

**Features:**

* Interactive Persian chat using Groq AI.
* Welcome messages for new group members.
* Display programmer info.
* Support buttons for easy access.
* Maintains last 20 messages per user for context.

---

### Requirements

* Python 3.10+
* Libraries:

  ```bash
  pip install pyTelegramBotAPI requests
  ```
* Telegram Bot Token (from BotFather)
* Groq API Key ([https://www.groq.com/](https://www.groq.com/))

---

### Setup

1. Clone this repository:

   ```bash
   git clone https://github.com/SmallSECURITY/Ai_chat_bot.git
   cd Ai_chat_bot
   unzip Ai-bot.zip
   cd Ai-bot
   ```

2. Install dependencies:

   ```bash
   pip install pyTelegramBotAPI requests

   ```

   *(or manually: `pyTelegramBotAPI` and `requests`)*

3. Edit `bot.py`:

   ```python
   TELEGRAM_API_TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'
   GROQ_API_KEY = 'YOUR_GROQ_API_KEY'
   ```

---

### Running the Bot

```bash
python bot.py
```

* The bot will start polling Telegram and respond to `/chat` commands.
* Use `/start` to see welcome message.
* Use `/programmer` for developer info.
* Use `/support` to access support buttons.

---

### Commands

| Command       | Description                            |
| ------------- | -------------------------------------- |
| `/start`      | Start interaction with bot             |
| `/chat`       | Chat with Groq AI (e.g., `/chat سلام`) |
| `/programmer` | Show developer info                    |
| `/support`    | Show support buttons                   |

---



### معرفی

<div dir="rtl">
ربات دستیار فارسی یک ربات تلگرام است که امکان **چت تعاملی با هوش مصنوعی** را فراهم می‌کند و از **Groq API** استفاده می‌کند.  
این ربات از فرمت Markdown و ایموجی‌ها پشتیبانی می‌کند و تاریخچه مکالمه کاربران را نگه می‌دارد.
</div>

**ویژگی‌ها:**

<div dir="rtl">
- چت تعاملی فارسی با Groq AI  
- پیام خوش‌آمدگویی برای اعضای جدید گروه  
- نمایش اطلاعات برنامه‌نویس  
- دکمه‌های پشتیبانی  
- ذخیره آخرین ۲۰ پیام هر کاربر برای حفظ زمینه مکالمه  
</div>

---

### نیازمندی‌ها

<div dir="rtl">
- Python 3.10+  
- کتابخانه‌ها:
  ```bash
  pip install pyTelegramBotAPI requests
  ```
- توکن ربات تلگرام (از BotFather)
- کلید API Groq (https://www.groq.com/)
</div>

---

### نصب و راه‌اندازی

<div dir="rtl">
1. کلون کردن مخزن:
   ```bash

   git clone https://github.com/SmallSECURITY/Ai_chat_bot.git
   cd Ai_chat_bot
   unzip Ai-bot.zip
   cd Ai-bot
   
   ```
2. نصب کتابخانه‌ها:
   ```bash
   pip install pyTelegramBotAPI requests

   ```
   *(یا نصب دستی: `pyTelegramBotAPI` و `requests`)*

3. ویرایش فایل `bot.py`:

   ```python
   TELEGRAM_API_TOKEN = 'توکن ربات تلگرام شما'
   GROQ_API_KEY = 'کلید API Groq شما'
   ```

</div>

---

### اجرای ربات

<div dir="rtl">
```bash
python bot.py
```
- ربات شروع به کار می‌کند و به فرمان‌های `/chat` پاسخ می‌دهد.  
- از `/start` برای مشاهده پیام خوش‌آمدگویی استفاده کنید.  
- از `/programmer` برای نمایش اطلاعات برنامه‌نویس.  
- از `/support` برای دسترسی به دکمه‌های پشتیبانی.
</div>

---

### دستورات

| دستور         | توضیح                                      |
| ------------- | ------------------------------------------ |
| `/start`      | شروع تعامل با ربات                         |
| `/chat`       | چت با هوش مصنوعی Groq (مثال: `/chat سلام`) |
| `/programmer` | نمایش اطلاعات برنامه‌نویس                  |
| `/support`    | نمایش دکمه‌های پشتیبانی                    |
