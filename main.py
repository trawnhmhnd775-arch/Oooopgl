from telegram import Bot, Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler

# تهيئة البوت باستخدام التوكن
updater = Updater('7976155862:AAGOM51VcSzwQ1SVXkfktnxLdgeCMBtWrng', use_context=True)
dispatcher = updater.dispatcher

# الرد على الأمر /start
def start(update, context):
    update.message.reply_text("أهلاً بك في البوت! اختر من الخيارات التالية:")

# إضافة الأمر لفتح الأقسام
def show_sections(update, context):
    keyboard = [
        ['إيداع رصيد', 'شحن الألعاب'],
        ['معلومات المستخدم', 'إحصائيات']
    ]
    update.message.reply_text('اختر خدمة:', reply_markup=InlineKeyboardMarkup(keyboard, one_time_keyboard=True))

# إضافة أمر لإيداع الرصيد
def deposit(update, context):
    update.message.reply_text("أدخل المبلغ الذي تريد إيداعه:")

# إضافة أمر لشحن الألعاب
def game_recharge(update, context):
    update.message.reply_text("اختر اللعبة التي ترغب في شحنها:")

# إضافة أمر للإحصائيات
def show_statistics(update, context):
    update.message.reply_text("إحصائيات المستخدمين:")

# إضافة الأمر /start
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

# إضافة استجابة لطلبات الأقسام
section_handler = CommandHandler('sections', show_sections)
dispatcher.add_handler(section_handler)

# إضافة استجابة للأوامر المختلفة
deposit_handler = CommandHandler('deposit', deposit)
dispatcher.add_handler(deposit_handler)

game_recharge_handler = CommandHandler('game_recharge', game_recharge)
dispatcher.add_handler(game_recharge_handler)

# بدء البوت
updater.start_polling()
updater.idle()
