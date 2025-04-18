
import telebot

TOKEN = '7742479143:AAHzp86TrQwLngS7BPko2xcWRpmY3HW-cIo'
ADMIN_ID = 6662120440
bot = telebot.TeleBot(TOKEN)

user_data = {}

@bot.message_handler(commands=['start'])
def start(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('إضافة شحنة', 'حالة الشحنات')
    if message.from_user.id == ADMIN_ID:
        markup.row('لوحة تحكم الأدمن')
    bot.send_message(message.chat.id, "مرحباً بك في نظام شركة ShahenX للشحن!", reply_markup=markup)

@bot.message_handler(func=lambda m: m.text == 'إضافة شحنة')
def add_shipment(message):
    user_data[message.chat.id] = {}
    msg = bot.send_message(message.chat.id, "ادخل اسم العميل:")
    bot.register_next_step_handler(msg, get_name)

def get_name(message):
    user_data[message.chat.id]['name'] = message.text
    msg = bot.send_message(message.chat.id, "ادخل رقم الهاتف:")
    bot.register_next_step_handler(msg, get_phone)

def get_phone(message):
    user_data[message.chat.id]['phone'] = message.text
    msg = bot.send_message(message.chat.id, "ادخل العنوان:")
    bot.register_next_step_handler(msg, get_address)

def get_address(message):
    user_data[message.chat.id]['address'] = message.text
    msg = bot.send_message(message.chat.id, "ادخل رقم التتبع:")
    bot.register_next_step_handler(msg, save_shipment)

def save_shipment(message):
    user_data[message.chat.id]['tracking'] = message.text
    bot.send_message(message.chat.id, f"تم حفظ بيانات الشحنة:
الاسم: {user_data[message.chat.id]['name']}
"
                                      f"الهاتف: {user_data[message.chat.id]['phone']}
"
                                      f"العنوان: {user_data[message.chat.id]['address']}
"
                                      f"رقم التتبع: {user_data[message.chat.id]['tracking']}")

bot.polling()
