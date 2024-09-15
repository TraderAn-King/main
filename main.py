from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# توکن ربات تلگرام خود را اینجا وارد کنید
TOKEN = '7277553648:AAGpWMoCSGw1M7-vd7rC0K7SXrctq20BnnI'
CHANNEL_ID = '@devil_team_hack'  # یا 'YourChannelID' بدون @
POST_ID = '73'  # آیدی پست که می‌خواهید فوروارد کنید
POSTT_ID = '74'  # آیدی پست که می‌خواهید فوروارد کنید

# تابعی برای بررسی عضویت کاربر در کانال
async def is_member(update: Update, context: CallbackContext) -> bool:
    user_id = update.message.from_user.id
    try:
        chat_member = await context.bot.get_chat_member(chat_id=CHANNEL_ID, user_id=user_id)
        return chat_member.status in ['member', 'administrator', 'creator']
    except Exception as e:
        print(f"Error checking membership: {e}")
        return False

# تابعی برای دستور /cube
async def cube_command(update: Update, context: CallbackContext) -> None:
    if await is_member(update, context):
        # اگر کاربر عضو کانال است، دستور را اجرا کن
        keyboard = [
            [InlineKeyboardButton("Get Stone Keys 🔑", url="https://t.me/Gethamcodbot/keys")],
            [InlineKeyboardButton("Hamster Channel 🐹", url="https://t.me/HamsterkombCombo")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text("Click on Get Cube keys\n\nHamster Channel : @HamsterkombCombo", reply_markup=reply_markup)
    else:
        # اگر عضو نیست، پیام عضویت ارسال کن
        keyboard = [
                          [InlineKeyboardButton("Join Channel", url="https://t.me/devil_team_hack")],
                          [InlineKeyboardButton("Join Channel", url="https://t.me/HamsterkombCombo")],
                          [InlineKeyboardButton("Join Channel", url="https://t.me/Karwantech12")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text("First Join Channel and again send /cube Thanks 👍🏻", reply_markup=reply_markup)

async def train_command(update: Update, context: CallbackContext) -> None:
    if await is_member(update, context):
        # اگر کاربر عضو کانال است، دستور را اجرا کن
        keyboard = [
            [InlineKeyboardButton("Get Stone Keys 🔑", url="https://t.me/Gethamcodbot/keys")],
            [InlineKeyboardButton("Hamster Channel 🐹", url="https://t.me/HamsterkombCombo")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text("Click on Get Train keys\n\nHamster Channel : @HamsterkombCombo", reply_markup=reply_markup)
    else:
        # اگر عضو نیست، پیام عضویت ارسال کن
        keyboard = [
                          [InlineKeyboardButton("Join Channel", url="https://t.me/devil_team_hack")],
                          [InlineKeyboardButton("Join Channel", url="https://t.me/HamsterkombCombo")],
                          [InlineKeyboardButton("Join Channel", url="https://t.me/Karwantech12")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text("First Join Channel and again send /cube Thanks 👍🏻", reply_markup=reply_markup)

async def merge_command(update: Update, context: CallbackContext) -> None:
    if await is_member(update, context):
        # اگر کاربر عضو کانال است، دستور را اجرا کن
        keyboard = [
            [InlineKeyboardButton("Get Stone Keys 🔑", url="https://t.me/Gethamcodbot/keys")],
            [InlineKeyboardButton("Hamster Channel 🐹", url="https://t.me/HamsterkombCombo")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text("Click on Get Merge keys\n\nHamster Channel : @HamsterkombCombo", reply_markup=reply_markup)
    else:
        # اگر عضو نیست، پیام عضویت ارسال کن
        keyboard = [
                          [InlineKeyboardButton("Join Channel", url="https://t.me/devil_team_hack")],
                          [InlineKeyboardButton("Join Channel", url="https://t.me/HamsterkombCombo")],
                          [InlineKeyboardButton("Join Channel", url="https://t.me/Karwantech12")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text("First Join Channel and again send /merge Thanks 👍🏻", reply_markup=reply_markup)

        
async def twerk_command(update: Update, context: CallbackContext) -> None:
    if await is_member(update, context):
        # اگر کاربر عضو کانال است، دستور را اجرا کن
        keyboard = [
            [InlineKeyboardButton("Get Stone Keys 🔑", url="https://t.me/Gethamcodbot/keys")],
            [InlineKeyboardButton("Hamster Channel 🐹", url="https://t.me/HamsterkombCombo")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text("Click on Get Twerk keys\n\nHamster Channel : @HamsterkombCombo", reply_markup=reply_markup)
    else:
        # اگر عضو نیست، پیام عضویت ارسال کن
        keyboard = [
                          [InlineKeyboardButton("Join Channel", url="https://t.me/devil_team_hack")],
                          [InlineKeyboardButton("Join Channel", url="https://t.me/HamsterkombCombo")],
                          [InlineKeyboardButton("Join Channel", url="https://t.me/karwantech12")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text("First Join Channel and again send /twerk Thanks 👍🏻", reply_markup=reply_markup)


async def poly_command(update: Update, context: CallbackContext) -> None:
    if await is_member(update, context):
        # اگر کاربر عضو کانال است، دستور را اجرا کن
        keyboard = [
            [InlineKeyboardButton("Get Stone Keys 🔑", url="https://t.me/Gethamcodbot/keys")],
            [InlineKeyboardButton("Hamster Channel 🐹", url="https://t.me/HamsterkombCombo")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text("Click on Get Poly keys\n\nHamster Channel : @HamsterkombCombo", reply_markup=reply_markup)
    else:
        # اگر عضو نیست، پیام عضویت ارسال کن
        keyboard = [
                          [InlineKeyboardButton("Join Channel", url="https://t.me/devil_team_hack")],
                          [InlineKeyboardButton("Join Channel", url="https://t.me/HamsterkombCombo")],
                          [InlineKeyboardButton("Join Channel", url="https://t.me/karwantech12")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text("First Join Channel and again send /poly Thanks 👍🏻", reply_markup=reply_markup)


async def trim_command(update: Update, context: CallbackContext) -> None:
    if await is_member(update, context):
        # اگر کاربر عضو کانال است، دستور را اجرا کن
        keyboard = [
            [InlineKeyboardButton("Get Stone Keys 🔑", url="https://t.me/Gethamcodbot/keys")],
            [InlineKeyboardButton("Hamster Channel 🐹", url="https://t.me/HamsterkombCombo")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text("Click on Get Trim keys\n\nHamster Channel : @HamsterkombCombo", reply_markup=reply_markup)
    else:
        # اگر عضو نیست، پیام عضویت ارسال کن
        keyboard = [
                          [InlineKeyboardButton("Join Channel", url="https://t.me/devil_team_hack")],
                          [InlineKeyboardButton("Join Channel", url="https://t.me/HamsterkombCombo")],
                          [InlineKeyboardButton("Join Channel", url="https://t.me/karwantech12")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text("First Join Channel and again send /trim Thanks 👍🏻", reply_markup=reply_markup)


async def zoo_command(update: Update, context: CallbackContext) -> None:
    if await is_member(update, context):
        # اگر کاربر عضو کانال است، دستور را اجرا کن
        keyboard = [
            [InlineKeyboardButton("Get Stone Keys 🔑", url="https://t.me/Gethamcodbot/keys")],
            [InlineKeyboardButton("Hamster Channel 🐹", url="https://t.me/HamsterkombCombo")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text("Click on Get Zoo keys\n\nHamster Channel : @HamsterkombCombo", reply_markup=reply_markup)
    else:
        # اگر عضو نیست، پیام عضویت ارسال کن
        keyboard = [
                          [InlineKeyboardButton("Join Channel", url="https://t.me/devil_team_hack")],
                          [InlineKeyboardButton("Join Channel", url="https://t.me/HamsterkombCombo")],
                          [InlineKeyboardButton("Join Channel", url="https://t.me/karwantech12")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text("First Join Channel and again send /zoo Thanks 👍🏻", reply_markup=reply_markup)
        
        

async def tile_command(update: Update, context: CallbackContext) -> None:
    if await is_member(update, context):
        # اگر کاربر عضو کانال است، دستور را اجرا کن
        keyboard = [
            [InlineKeyboardButton("Get Stone Keys 🔑", url="https://t.me/Gethamcodbot/keys")],
            [InlineKeyboardButton("Hamster Channel 🐹", url="https://t.me/HamsterkombCombo")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text("Click on Get Tile keys\n\nHamster Channel : @HamsterkombCombo", reply_markup=reply_markup)
    else:
        # اگر عضو نیست، پیام عضویت ارسال کن
        keyboard = [
                          [InlineKeyboardButton("Join Channel", url="https://t.me/devil_team_hack")],
                          [InlineKeyboardButton("Join Channel", url="https://t.me/HamsterkombCombo")],
                          [InlineKeyboardButton("Join Channel", url="https://t.me/karwantech12")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text("First Join Channel and again send /tile Thanks 👍🏻", reply_markup=reply_markup)


async def crusade_command(update: Update, context: CallbackContext) -> None:
    if await is_member(update, context):
        # اگر کاربر عضو کانال است، دستور را اجرا کن
        keyboard = [
            [InlineKeyboardButton("Get Stone Keys 🔑", url="https://t.me/Gethamcodbot/keys")],
            [InlineKeyboardButton("Hamster Channel 🐹", url="https://t.me/HamsterkombCombo")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text("Click on Get Crusade keys\n\nHamster Channel : @HamsterkombCombo", reply_markup=reply_markup)
    else:
        # اگر عضو نیست، پیام عضویت ارسال کن
        keyboard = [
                          [InlineKeyboardButton("Join Channel", url="https://t.me/devil_team_hack")],
                          [InlineKeyboardButton("Join Channel", url="https://t.me/HamsterkombCombo")],
                          [InlineKeyboardButton("Join Channel", url="https://t.me/karwantech12")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text("First Join Channel and again send /crusade Thanks 👍🏻", reply_markup=reply_markup)



async def stone_command(update: Update, context: CallbackContext) -> None:
    if await is_member(update, context):
        # اگر کاربر عضو کانال است، دستور را اجرا کن
        keyboard = [
            [InlineKeyboardButton("Get Stone Keys 🔑", url="https://t.me/Gethamcodbot/keys")],
            [InlineKeyboardButton("Hamster Channel 🐹", url="https://t.me/HamsterkombCombo")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text("Click on Get Stone keys\n\nHamster Channel : @HamsterkombCombo", reply_markup=reply_markup)
    else:
        # اگر عضو نیست، پیام عضویت ارسال کن
        keyboard = [
                          [InlineKeyboardButton("Join Channel", url="https://t.me/devil_team_hack")],
                          [InlineKeyboardButton("Join Channel", url="https://t.me/HamsterkombCombo")],
                          [InlineKeyboardButton("Join Channel", url="https://t.me/karwantech12")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text("First Join Channel and again send /stone Thanks 👍🏻", reply_markup=reply_markup)
        
        
        
        
async def dailycombo_command(update: Update, context: CallbackContext) -> None:
    if await is_member(update, context):
        # اگر کاربر عضو کانال است، دستور را اجرا کن
        keyboard = [
            [InlineKeyboardButton("Get Today Hamster Daily Combo 🔑", url="https://t.me/HamsterkombCombo")],
            [InlineKeyboardButton("Hamster Channel 🐹", url="https://t.me/HamsterkombCombo")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text("Click on Get Today Daily Combo\n\nHamster Channel : @HamsterkombCombo", reply_markup=reply_markup)
    else:
        # اگر عضو نیست، پیام عضویت ارسال کن
        keyboard = [
                          [InlineKeyboardButton("Join Channel", url="https://t.me/devil_team_hack")],
                          [InlineKeyboardButton("Join Channel", url="https://t.me/HamsterkombCombo")],
                          [InlineKeyboardButton("Join Channel", url="https://t.me/karwantech12")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text("First Join Channel and again send /dailycomboThanks 👍🏻", reply_markup=reply_markup)
        
        
async def dailycipher_command(update: Update, context: CallbackContext) -> None:
    if await is_member(update, context):
        # اگر کاربر عضو کانال است، دستور را اجرا کن
        keyboard = [
            [InlineKeyboardButton("Get Today Hamster Daily Cipher 🔑", url="https://t.me/HamsterkombCombo")],
            [InlineKeyboardButton("Hamster Channel 🐹", url="https://t.me/HamsterkombCombo")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text("Click on Get Today Daily Cipher\n\nHamster Channel : @HamsterkombCombo", reply_markup=reply_markup)
    else:
        # اگر عضو نیست، پیام عضویت ارسال کن
        keyboard = [
                          [InlineKeyboardButton("Join Channel", url="https://t.me/devil_team_hack")],
                          [InlineKeyboardButton("Join Channel", url="https://t.me/HamsterkombCombo")],
                          [InlineKeyboardButton("Join Channel", url="https://t.me/karwantech12")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text("First Join Channel and again send /dailycipherThanks 👍🏻", reply_markup=reply_markup)
        
        
async def support_command(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('contact on @kingamir_01 admin')
    
async def start_command(update: Update, context: CallbackContext) -> None:
	keyboard = [
                          [InlineKeyboardButton("Join Channel", url="https://t.me/devil_team_hack")]
        reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('👋 Welcome, I m a bot to help you get Hamster key Codes Daily Cipher and Daily Combo 🗓️🔑\n\nTo use this bot you need to join our channel : @devil_team_hack\n\nThere are commands to get Codes 🔑\n/cube - For cube key codes\n/train - For train key codes\n/merge - For merge key codes\n/twerk - For twerk key codes\n/poly - For polysphere key codes\n/trim - For trim key codes\n/tile - For Tile Key\n/crusade - For Crusade Key\n/stone - For Stone Age Key\n/dailycipher - Get Today Daily Cipher\n/dailycombo - Get Today Daily Combo\n/help - How to use Tech\n/support - contact on admin\n\nNote : If the codes didn come up  just use VPN Now Check 🐱', reply_markup=reply_markup)

async def help_command(update: Update, context: CallbackContext) -> None:
    try:
        # فوروارد کردن پست از کانال به کاربر
        await context.bot.forward_message(
            chat_id=update.effective_chat.id,
            from_chat_id=CHANNEL_ID,
            message_id=POST_ID
        )
        await context.bot.forward_message(
            chat_id=update.effective_chat.id,
            from_chat_id=CHANNEL_ID,
            message_id=POSTT_ID
        )
    except Exception as e:
        await update.message.reply_text("eror check @devil_team_hack")
        print(f"Error forwarding post: {e}")


def main() -> None:
    # ساخت اپلیکیشن و افزودن توکن
    app = Application.builder().token(TOKEN).build()
    
    #برای‌دستور start
    app.add_handler(CommandHandler("start", start_command))
    
    #بزای دستور cube
    app.add_handler(CommandHandler("cube", cube_command))
    
    #   train برای دستور 
    app.add_handler(CommandHandler("train", train_command))
    
    #برای دستور help
    app.add_handler(CommandHandler("help", help_command))

    #برای دستور support 
    app.add_handler(CommandHandler("support", support_command))
    
    #برای دستور dailycombo
    app.add_handler(CommandHandler("dailycombo", dailycombo_command))
    
    #براب   dailycipher dailyipher 
    app.add_handler(CommandHandler("dailycipher", dailycipher_command)) 
    
    #   merge برای دستور 
    app.add_handler(CommandHandler("merge", merge_command))
    
    #   merge برای دستور 
    app.add_handler(CommandHandler("twerk", twerk_command))
    
    #   merge برای دستور 
    app.add_handler(CommandHandler("poly", poly_command))
    
    #   merge برای دستور 
    app.add_handler(CommandHandler("trim", trim_command))
    
    #   merge برای دستور 
    app.add_handler(CommandHandler("zoo", zoo_command))
    
    #   merge برای دستور 
    app.add_handler(CommandHandler("tile", tile_command))
    
    #   merge برای دستور 
    app.add_handler(CommandHandler("crusade", crusade_command))
    
    #   merge برای دستور 
    app.add_handler(CommandHandler("stone", stone_command))
    

    # اضافه کردن MessageHandler برای پیام‌های متنی
    

    # شروع ربات
    app.run_polling()

if __name__ == '__main__':
    main() 