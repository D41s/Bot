import telebot
from telebot import types

# токен-бота
bot = telebot.TeleBot('1440608671:AAE3BOK3gubP8gAHfqDs3HMB8tsmAtnxKXY')


# если /help, /start
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Привет "
                     + message.from_user.first_name
                     + ", здесь можно купить скины из CS:GO",
                     reply_markup=markup_menu)


markup_menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
btn_1 = types.KeyboardButton('Пистолеты')
btn_2 = types.KeyboardButton('ПП')
btn_3 = types.KeyboardButton('Винтовки')
btn_4 = types.KeyboardButton('Тяжелое')
markup_menu.add(btn_1, btn_2, btn_3, btn_4)


Pistols = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
btn_p1 = types.KeyboardButton('glock-18')
btn_p2 = types.KeyboardButton('Deagle')
btn_p3 = types.KeyboardButton('Five-seven')
btn_p4 = types.KeyboardButton('Tec-9')
btn_p5 = types.KeyboardButton('В меню')
Pistols.add(btn_p1, btn_p2, btn_p3, btn_p4, btn_p5)


PP = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
btn_pp1 = types.KeyboardButton('MAC-10')
btn_pp2 = types.KeyboardButton('MP7')
btn_pp3 = types.KeyboardButton('UMP-45')
btn_pp4 = types.KeyboardButton('P90')
btn_pp5 = types.KeyboardButton('В меню')
PP.add(btn_pp1, btn_pp2, btn_pp3, btn_pp4, btn_pp5)


Rifles = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
btn_r1 = types.KeyboardButton('M4A4')
btn_r2 = types.KeyboardButton('AK-47')
btn_r3 = types.KeyboardButton('Famas')
btn_r4 = types.KeyboardButton('AWP')
btn_r5 = types.KeyboardButton('В меню')
Rifles.add(btn_r1, btn_r2, btn_r3, btn_r4, btn_r5)


Heavy = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
btn_h1 = types.KeyboardButton('MAG-7')
btn_h2 = types.KeyboardButton('XM1014')
btn_h3 = types.KeyboardButton('M249')
btn_h4 = types.KeyboardButton('Negev')
btn_h5 = types.KeyboardButton('В меню')
Heavy.add(btn_h1, btn_h2, btn_h3, btn_h4, btn_h5)

vmenyu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
btn_naz5 = types.KeyboardButton('В меню')
vmenyu.add(btn_naz5)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.text == "В меню":
        bot.reply_to(message, "Назад", reply_markup=markup_menu)
    if message.text == "Пистолеты":
        bot.reply_to(message, "Выберите пистолет", reply_markup=Pistols)
    if message.text == "ПП":
        bot.reply_to(message, "Выберите ПП", reply_markup=PP)
    if message.text == "Винтовки":
        bot.reply_to(message, "Выберите винтовку", reply_markup=Rifles)
    if message.text == "Тяжелое":
        bot.reply_to(message, "Выберите оружие", reply_markup=Heavy)
    if message.text == "glock-18":
        bot.reply_to(message, "вот скин", reply_markup=Pistols)
        text = """
glock-18 Дух воды
цена 1550-3520
                """
        bot.send_photo(chat_id=message.chat.id,
                       photo='https://blackbox.style/wp-content/uploads/9f65698e-d364-4acb-851c-9f71bdeff471.jpg',
                       caption=text, parse_mode='Markdown')
    if message.text == "Deagle":
        bot.reply_to(message, "вот скин", reply_markup=Pistols)
        text = """
Deagle Пламя
цена 145300-169800
                """
        bot.send_photo(chat_id=message.chat.id,
                       photo='https://blackbox.style/wp-content/uploads/fd422b3d-69cb-424a-a968-e1fd9d212883.jpg',
                       caption=text, parse_mode='Markdown')
    if message.text == "Five-seven":
            bot.reply_to(message, "вот скин", reply_markup=Pistols)
            text = """
Five-seven Скоростной зверь
цена 3940-35300
                    """
            bot.send_photo(chat_id=message.chat.id,
                           photo='https://blackbox.style/wp-content/uploads/746df82d-5272-4904-a920-f1fcd84e8cef.jpg',
                           caption=text, parse_mode='Markdown')
    if message.text == "Tec-9":
        bot.reply_to(message, "вот скин", reply_markup=Pistols)
        text = """
Tec-9 Топливный инжектор
цена 671-2960
                """
        bot.send_photo(chat_id=message.chat.id,
                       photo='https://blackbox.style/wp-content/uploads/c00d850c-f485-4e5f-bc67-4ea34b61bc69.jpg',
                       caption=text, parse_mode='Markdown')
    if message.text == "MAC-10":
        bot.reply_to(message, "вот скин", reply_markup=PP)
        text = """
MAC-10 Неоновый гонщик
цена 2300-3850
                """
        bot.send_photo(chat_id=message.chat.id,
                       photo='https://blackbox.style/wp-content/uploads/2fb080d7-fe0a-4c13-898e-7a79ead500ac.jpg',
                       caption=text, parse_mode='Markdown')
    if message.text == "MP7":
            bot.reply_to(message, "вот скин", reply_markup=PP)
            text = """
MP7 Заклятый враг
цена 1740-3070
                    """
            bot.send_photo(chat_id=message.chat.id,
                           photo='https://blackbox.style/wp-content/uploads/f7ce31a6-d628-4f0b-9a84-0920fa7ebd37.jpg',
                           caption=text, parse_mode='Markdown')

    if message.text == "UMP-45":
        bot.reply_to(message, "вот скин", reply_markup=PP)
        text = """
UMP-45 Первобытный саблезуб
цена 708-2930
                """
        bot.send_photo(chat_id=message.chat.id,
                       photo='https://blackbox.style/wp-content/uploads/d31821b4-58dc-46ad-951c-f7032485fdbd.jpg',
                       caption=text, parse_mode='Markdown')
    if message.text == "P90":
        bot.reply_to(message, "вот скин", reply_markup=PP)
        text = """
P90 Азимов
цена 2075-14550
                """
        bot.send_photo(chat_id=message.chat.id,
                       photo='https://blackbox.style/wp-content/uploads/afc0288e-4ff1-4c8e-8078-76fc34a935f0.jpg',
                       caption=text, parse_mode='Markdown')
    if message.text == "M4A4":
        bot.reply_to(message, "вот скин", reply_markup=Rifles)
        text = """
M4A4 Безлюдный космос
цена 3020-12200
                """
        bot.send_photo(chat_id=message.chat.id,
                       photo='https://blackbox.style/wp-content/uploads/676dd703-c102-4680-af4f-243b3d9531e4.jpg',
                       caption=text, parse_mode='Markdown')
    if message.text == "AK-47":
        bot.reply_to(message, "вот скин", reply_markup=Rifles)
        text = """
AK-47 Императрица
цена 10070-41370
                """
        bot.send_photo(chat_id=message.chat.id,
                       photo='https://blackbox.style/wp-content/uploads/0c44e74f-94b5-42e0-85b2-efcfcaa18fde.jpg',
                       caption=text, parse_mode='Markdown')
    if message.text == "Famas":
        bot.reply_to(message, "вот скин", reply_markup=Rifles)
        text = """
Famas Механо-пушка
цена 830-1975
                """
        bot.send_photo(chat_id=message.chat.id,
                       photo='https://blackbox.style/wp-content/uploads/c6cf63f7-81a1-4413-8d05-ff7940e8c109.jpg',
                       caption=text, parse_mode='Markdown')
    if message.text == "AWP":
        bot.reply_to(message, "вот скин", reply_markup=Rifles)
        text = """
AWP Гунгнир
цена 1115420-2636980
                """
        bot.send_photo(chat_id=message.chat.id,
                       photo='https://blackbox.style/wp-content/uploads/35002215-7b95-4a5f-a904-73cf3b0905da.jpg',
                       caption=text, parse_mode='Markdown')
    if message.text == "MAG-7":
        bot.reply_to(message, "вот скин", reply_markup=Heavy)
        text = """
MAG-7 ПОНТ-7
цена 126-541
                """
        bot.send_photo(chat_id=message.chat.id,
                       photo='https://blackbox.style/wp-content/uploads/7d54cb95-5235-4ce2-a082-e6a33d9edb78.jpg',
                       caption=text, parse_mode='Markdown')
    if message.text == "XM1014":
        bot.reply_to(message, "вот скин", reply_markup=Heavy)
        text = """
XM1014 Времена года
цена 214-465
                """
        bot.send_photo(chat_id=message.chat.id,
                       photo='https://blackbox.style/wp-content/uploads/7b80bac5-5174-4048-9bad-0398a8a95c62.jpg',
                       caption=text, parse_mode='Markdown')
    if message.text == "M249":
        bot.reply_to(message, "вот скин", reply_markup=Heavy)
        text = """
M249 Укус изумрудного яда
цена 210-500
                """
        bot.send_photo(chat_id=message.chat.id,
                       photo='https://blackbox.style/wp-content/uploads/37c0aa8e-8ead-4a98-a780-a7698d4d09ad.jpg',
                       caption=text, parse_mode='Markdown')
    if message.text == "Negev":
        bot.reply_to(message, "вот скин", reply_markup=Heavy)
        text = """
Negev Мьёлнир
цена 196430-266000
                """
        bot.send_photo(chat_id=message.chat.id,
                       photo='https://blackbox.style/wp-content/uploads/051e9a72-d3a7-417e-841d-d048237dbf5d.jpg',
                       caption=text, parse_mode='Markdown')


bot.polling()