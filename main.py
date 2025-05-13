from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
import os

# Load bot token from environment variable
TOKEN = os.environ["BOT_TOKEN"]

# Text in 3 languages
messages = {
    "en": """Welcome to EdenVault – Your Personal Digital Agent

Looking for the best deals on VPNs, subscriptions, gift cards, game top-ups, or social media growth?

EdenVault is your go-to assistant for all things digital — fast, secure, and reliable.

We offer:
- VPN Services – Top-tier privacy & protection
- Subscriptions – Netflix, Spotify, YouTube, ChatGPT & more
- Game Top-Ups – Fast, safe, multi-platform credits
- Gift Cards – Local & international options
- Social Media Boost – Real engagement, real growth

No bots. No hassle. Just real support, real service.

EdenVault – Your digital life, delivered.""",

    "mm": """EdenVault မှ ကြိုဆိုပါတယ် – သင့်ကိုယ်ပိုင် ဒစ်ဂျစ်တယ်အကူအညီ

VPN, subscription ဝန်ဆောင်မှုတွေ၊ gift card များ၊ game top-up၊ social media တိုးတက်မှုလိုအပ်လား?

EdenVault သည် သင့်အတွက် အမြန်ဆုံး၊ အလုံခြုံဆုံး၊ ယုံကြည်စိတ်ချရသော ဒစ်ဂျစ်တယ် အကူအညီဖြစ်ပါတယ်။

ကျွန်ုပ်တိုမှာရှိသည်မှာ:
- VPN ဝန်ဆောင်မှု – သီးသန့်ရေးနှင့်လုံခြုံရေးအတွက်
- Subscription – Netflix, Spotify, YouTube, ChatGPT စသည်တို
- Game Top-Up – အမြန်နှုန်းမြင့်၊ လုံခြုံမှုရှိသော ဂိမ်းငွေဖြည့်ဝန်ဆောင်မှု
- Gift Card – ပြည်တွင်းနှင့်နိုင်ငံတကာ ရွေးချယ်စရာများ
- Social Media Boost – တကယ်သော followers နှင့် engagement

ဘော့မဟုတ်ပါ။ အဆင်မပြေတာမျိုးမရှိပါဘူး။ တကယ်သော ဝန်ဆောင်မှု၊ တကယ်သောအထောက်အကူ။

EdenVault – သင့် ဒစ်ဂျစ်တယ်ဘဝကို ပေးဆောင်ပေးပါသည်။""",

    "cn": """欢迎来到 EdenVault —— 您的专属数字助理

正在寻找最优惠的 VPN、订阅服务、礼品卡、游戏充值或社交媒体推广？

EdenVault 是您的一站式数字助手 —— 快速、安全、可靠。

我们提供：
- VPN服务 —— 顶级隐私保护
- 订阅服务 —— Netflix、Spotify、YouTube、ChatGPT 等
- 游戏充值 —— 多平台、快速又安全
- 礼品卡 —— 本地及国际选择
- 社交媒体增长 —— 真实互动，真实增长

不使用机器人。没有麻烦。只有真正的服务与支持。

EdenVault —— 数字生活，由我们送达。"""
}

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton("Myanmar", callback_data="lang_mm"),
            InlineKeyboardButton("中文", callback_data="lang_cn"),
            InlineKeyboardButton("English", callback_data="lang_en"),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Choose your language:", reply_markup=reply_markup)

# Handle language selection
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    lang = query.data.replace("lang_", "")
    await query.edit_message_text(text=messages.get(lang, "Unknown language."))

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))
    app.run_polling()

if name == "__main__":
    main()