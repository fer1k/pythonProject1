import telebot
from telebot import types

answer = ''
city2 = ''
date = ''
city = ''
wait = ''
ans = ''

bot = telebot.TeleBot("1727570238:AAFXwr6xlUZPJ5piGuuYC5a4uNmmgIgTPQI")


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, """
    Добро пожаловать!😊 
Если вы хотите ознакомиться с ближайшим расписанием ЖД Вокзалов,напишите 'Привет'.
Памятка:
1⃣ Пиши названия городов и месяцев с заглавной буквы.
2⃣ На данный момент я представляю билеты с 4 мая 2021 года до 30 мая 2021 года.
3⃣ Ваш билет отправится вам на почту после совершения покупки. """, parse_mode="Markdown")
    bot.register_next_step_handler(message, get_text_messages)


@bot.message_handler(commands=['help'])
def send_welcome(message):
    if message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши привет")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


@bot.message_handler(content_types=['text', 'document', 'audio'])
def get_text_messages(message):
    if message.text == 'Привет' or message.text == 'привет':
        bot.send_message(message.from_user.id, "Привет! Вы хотите найти билеты ЖД вокзалов?")
        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        keyboard.row('Да', 'Нет')
        bot.send_message(message.chat.id, 'Выберите опцию на клавиатуре:',
                         reply_markup=keyboard)
        bot.register_next_step_handler(message, reg_answer)
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


def reg_answer(message):
    global answer
    answer = message.text
    if message.text == 'Нет' or message.text == 'нет':
        bot.reply_to(message, 'Извините, если у вас будет желание купить билеты - пишите /start')
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши привет")
    elif message.text == "/start":
        bot.send_message(message.chat.id, """
            Добро пожаловать!😊 
Если вы хотите ознакомиться с ближайшим расписанием ЖД Вокзалов,напишите 'Привет'.
Памятка:
1⃣ Пиши названия городов и месяцев с заглавной буквы.
2⃣ На данный момент я представляю билеты с 4 мая 2021 года до 30 мая 2021 года.
3⃣ Ваш билет отправится вам на почту после совершения покупки.  """, parse_mode="Markdown")
        bot.register_next_step_handler(message.from_user.id, get_text_messages)
    else:
        bot.send_message(message.from_user.id, "Город в котором вы находитесь?")
    bot.register_next_step_handler(message, reg_month)


def reg_month(message):
    global city
    city = message.text
    if message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши привет")
    elif message.text == "/start":
        bot.send_message(message.chat.id, """
            Добро пожаловать!😊 
Если вы хотите ознакомиться с ближайшим расписанием ЖД Вокзалов,напишите 'Привет'.
Памятка:
1⃣ Пиши названия городов и месяцев с заглавной буквы.
2⃣ На данный момент я представляю билеты с 4 мая 2021 года до 30 мая 2021 года.
3⃣ Ваш билет отправится вам на почту после совершения покупки.  """, parse_mode="Markdown")
        bot.register_next_step_handler(message.from_user.id, get_text_messages)
    else:
        bot.send_message(message.from_user.id, "Куда желаете поехать ?")
    bot.register_next_step_handler(message, reg_year)


def reg_year(message):
    global city2
    city2 = message.text
    if message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши привет")
    elif message.text == "/start":
        bot.send_message(message.chat.id, """
                    Добро пожаловать!😊 
Если вы хотите ознакомиться с ближайшим расписанием ЖД Вокзалов,напишите 'Привет'.
Памятка:
1⃣ Пиши названия городов и месяцев с заглавной буквы.
2⃣ На данный момент я представляю билеты с 4 мая 2021 года до 30 мая 2021 года.
3⃣ Ваш билет отправится вам на почту после совершения покупки.  """, parse_mode="Markdown")
        bot.register_next_step_handler(message.from_user.id, get_text_messages)
    else:
        bot.send_message(message.from_user.id, "Выберите число отправки?")
    bot.register_next_step_handler(message, reg_date)


def reg_date(message):
    global date
    date = message.text
    if message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши привет")
    elif message.text == "/start":
        bot.send_message(message.chat.id, """
                            Добро пожаловать!😊 
Если вы хотите ознакомиться с ближайшим расписанием ЖД Вокзалов,напишите 'Привет'.
Памятка:
1⃣ Пиши названия городов и месяцев с заглавной буквы.
2⃣ На данный момент я представляю билеты с 4 мая 2021 года до 30 мая 2021 года.
3⃣ Ваш билет отправится вам на почту после совершения покупки.  """, parse_mode="Markdown")
        bot.register_next_step_handler(message.from_user.id, get_text_messages)
    else:
        global wait
        while wait == 0:
            # noinspection PyBroadException
            try:
                wait = int(message.text)
            except Exception:
                bot.send_message(message.from_user.id, "Идет процесс обрабатывания информации.")
        keyboard = types.InlineKeyboardMarkup()
        key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')
        keyboard.add(key_yes)
        key_no = types.InlineKeyboardButton(text='Нет', callback_data='no')
        keyboard.add(key_no)
        question = 'Город в котором вы находитесь ' +city + '. Куда желаете поехать ' + city2 + ' число ' + date + ' мая ?'
        bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "yes":
        bot.send_message(call.message.chat.id, "Подтвердите свой запрос, написав 'Да'.⬇")
        bot.register_next_step_handler(call.message, send_welcome)
    elif call.data == "no":
        bot.send_message(call.message.chat.id, "Попробуем еще раз!")
        bot.send_message(call.message.chat.id, "Привет! вы хотите ознакомиться с ближайшим расписанием ЖД Вокзалов?")
        bot.register_next_step_handler(call.message, reg_answer)

    elif call.data == "second":
        bot.send_message(call.message.chat.id, "Попробуем еще раз!")
        bot.send_message(call.message.chat.id, "Привет! вы хотите ознакомиться с ближайшим расписанием ЖД Вокзалов?")
        bot.register_next_step_handler(call.message, reg_answer)
    elif call.data == 'first':
        key3 = types.InlineKeyboardMarkup()
        key_first = types.InlineKeyboardButton(text='Купе',url="https://aviata.kz/railways/place?from=2700000&to=2708001&number=003%D0%A6&date=2021-05-04%2014%3A35&is_transit=false&car=%D0%9A%D1%83%D0%BF%D0%B5&carId=16078721&fullPath=%2Frailways%2Fsearch%3Fstation_from%3D2700000%26station_to%3D2708001%26departure_date%3D04.05.2021", callback_data='VIP')
        key_second = types.InlineKeyboardButton(text='Плацкарт',url="https://aviata.kz/railways/place?from=2700000&to=2708001&number=003%D0%A6&date=2021-05-04%2014%3A35&is_transit=false&car=%D0%A1%D0%B8%D0%B4%D1%8F%D1%87%D0%B8%D0%B9&carId=16078720&fullPath=%2Frailways%2Fsearch%3Fstation_from%3D2700000%26station_to%3D2708001%26departure_date%3D04.05.2021", callback_data='stan')
        key_third = types.InlineKeyboardButton(text='Завершить покупку', callback_data='end')
        key3.add(key_first)
        key3.add(key_second)
        key3.add(key_third)
        bot.send_message(call.message.chat.id, "Отличный выбор!")
        bot.send_message(call.from_user.id, 'Выберите тип билета:', reply_markup=key3)
    elif call.data == 'first2':
        bot.send_message(call.message.chat.id, "Отличный выбор!")
        key3 = types.InlineKeyboardMarkup()
        key_first = types.InlineKeyboardButton(text='Купе',url="https://aviata.kz/railways/place?from=2700000&to=2708001&number=003%D0%A6&date=2021-05-05%2014%3A35&is_transit=false&car=%D0%9A%D1%83%D0%BF%D0%B5&carId=16104758&fullPath=%2Frailways%2Fsearch%3Fstation_from%3D2700000%26station_to%3D2708001%26departure_date%3D05.05.2021", callback_data='VIP')
        key_second = types.InlineKeyboardButton(text='Плацкарт',url="https://aviata.kz/railways/place?from=2700000&to=2708001&number=003%D0%A6&date=2021-05-05%2014%3A35&is_transit=false&car=%D0%A1%D0%B8%D0%B4%D1%8F%D1%87%D0%B8%D0%B9&carId=16104757&fullPath=%2Frailways%2Fsearch%3Fstation_from%3D2700000%26station_to%3D2708001%26departure_date%3D05.05.2021", callback_data='stan')
        key_third = types.InlineKeyboardButton(text='Завершить покупку', callback_data='end')
        key3.row(key_first)
        key3.row(key_second)
        key3.add(key_third)
        bot.send_message(call.from_user.id, 'Выберите тип билета:', reply_markup=key3)
    elif call.data == 'first3':
        bot.send_message(call.message.chat.id, "Отличный выбор!")
        key3 = types.InlineKeyboardMarkup()
        key_first = types.InlineKeyboardButton(text='Купе',
                                               url="https://aviata.kz/railways/place?from=2700000&to=2708001&number=003%D0%A6&date=2021-05-06%2014%3A35&is_transit=false&car=%D0%9A%D1%83%D0%BF%D0%B5&carId=16128870&fullPath=%2Frailways%2Fsearch%3Fstation_from%3D2700000%26station_to%3D2708001%26departure_date%3D06.05.2021",
                                               callback_data='VIP')
        key_second = types.InlineKeyboardButton(text='Плацкарт',
                                                url="https://aviata.kz/railways/place?from=2700000&to=2708001&number=003%D0%A6&date=2021-05-06%2014%3A35&is_transit=false&car=%D0%A1%D0%B8%D0%B4%D1%8F%D1%87%D0%B8%D0%B9&carId=16128869&fullPath=%2Frailways%2Fsearch%3Fstation_from%3D2700000%26station_to%3D2708001%26departure_date%3D06.05.2021",
                                                callback_data='stan')
        key_third = types.InlineKeyboardButton(text='Завершить покупку', callback_data='end')
        key3.row(key_first)
        key3.row(key_second)
        key3.add(key_third)
        bot.send_message(call.from_user.id, 'Выберите тип билета:', reply_markup=key3)
    elif call.data == 'first4':
        bot.send_message(call.message.chat.id, "Отличный выбор!")
        key3 = types.InlineKeyboardMarkup()
        key_first = types.InlineKeyboardButton(text='Купе',
                                               url="https://aviata.kz/railways/place?from=2700000&to=2708001&number=003%D0%A6&date=2021-05-07%2014%3A35&is_transit=false&car=%D0%9A%D1%83%D0%BF%D0%B5&carId=16161840&fullPath=%2Frailways%2Fsearch%3Fstation_from%3D2700000%26station_to%3D2708001%26departure_date%3D07.05.2021",
                                               callback_data='VIP')
        key_second = types.InlineKeyboardButton(text='Плацкарт',
                                                url="https://aviata.kz/railways/place?from=2700000&to=2708001&number=003%D0%A6&date=2021-05-07%2014%3A35&is_transit=false&car=%D0%A1%D0%B8%D0%B4%D1%8F%D1%87%D0%B8%D0%B9&carId=16161839&fullPath=%2Frailways%2Fsearch%3Fstation_from%3D2700000%26station_to%3D2708001%26departure_date%3D07.05.2021",
                                                callback_data='stan')
        key_third = types.InlineKeyboardButton(text='Завершить покупку', callback_data='end')
        key3.row(key_first)
        key3.row(key_second)
        key3.add(key_third)
        bot.send_message(call.from_user.id, 'Выберите тип билета:', reply_markup=key3)
    elif call.data == 'first5':
        bot.send_message(call.message.chat.id, "Отличный выбор!")
        key3 = types.InlineKeyboardMarkup()
        key_first = types.InlineKeyboardButton(text='Купе',
                                               url="https://aviata.kz/railways/place?from=2700000&to=2708001&number=003%D0%A6&date=2021-05-08%2014%3A35&is_transit=false&car=%D0%9A%D1%83%D0%BF%D0%B5&carId=16179733&fullPath=%2Frailways%2Fsearch%3Fstation_from%3D2700000%26station_to%3D2708001%26departure_date%3D08.05.2021",
                                               callback_data='VIP')
        key_second = types.InlineKeyboardButton(text='Плацкарт',
                                                url="https://aviata.kz/railways/place?from=2700000&to=2708001&number=003%D0%A6&date=2021-05-08%2014%3A35&is_transit=false&car=%D0%A1%D0%B8%D0%B4%D1%8F%D1%87%D0%B8%D0%B9&carId=16179732&fullPath=%2Frailways%2Fsearch%3Fstation_from%3D2700000%26station_to%3D2708001%26departure_date%3D08.05.2021",
                                                callback_data='stan')
        key_third = types.InlineKeyboardButton(text='Завершить покупку', callback_data='end')
        key3.row(key_first)
        key3.row(key_second)
        key3.add(key_third)
        bot.send_message(call.from_user.id, 'Выберите тип билета:', reply_markup=key3)
    elif call.data == 'first6':
        bot.send_message(call.message.chat.id, "Отличный выбор!")
        key3 = types.InlineKeyboardMarkup()
        key_first = types.InlineKeyboardButton(text='Купе',
                                               url="https://aviata.kz/railways/place?from=2700000&to=2708001&number=003%D0%A6&date=2021-05-09%2014%3A35&is_transit=false&car=%D0%9A%D1%83%D0%BF%D0%B5&carId=16206868&fullPath=%2Frailways%2Fsearch%3Fstation_from%3D2700000%26station_to%3D2708001%26departure_date%3D09.05.2021",
                                               callback_data='VIP')
        key_second = types.InlineKeyboardButton(text='Плацкарт',
                                                url="https://aviata.kz/railways/place?from=2700000&to=2708001&number=003%D0%A6&date=2021-05-09%2014%3A35&is_transit=false&car=%D0%A1%D0%B8%D0%B4%D1%8F%D1%87%D0%B8%D0%B9&carId=16206867&fullPath=%2Frailways%2Fsearch%3Fstation_from%3D2700000%26station_to%3D2708001%26departure_date%3D09.05.2021",
                                                callback_data='stan')
        key_third = types.InlineKeyboardButton(text='Завершить покупку', callback_data='end')
        key3.row(key_first)
        key3.row(key_second)
        key3.add(key_third)
        bot.send_message(call.from_user.id, 'Выберите тип билета:', reply_markup=key3)
    elif call.data == 'first7':
        bot.send_message(call.message.chat.id, "Отличный выбор!")
        key3 = types.InlineKeyboardMarkup()
        key_first = types.InlineKeyboardButton(text='Купе',
                                               url="https://aviata.kz/railways/place?from=2700000&to=2708001&number=003%D0%A6&date=2021-05-10%2014%3A35&is_transit=false&car=%D0%9A%D1%83%D0%BF%D0%B5&carId=16234068&fullPath=%2Frailways%2Fsearch%3Fstation_from%3D2700000%26station_to%3D2708001%26departure_date%3D10.05.2021",
                                               callback_data='VIP')
        key_second = types.InlineKeyboardButton(text='Плацкарт',
                                                url="https://aviata.kz/railways/place?from=2700000&to=2708001&number=003%D0%A6&date=2021-05-10%2014%3A35&is_transit=false&car=%D0%A1%D0%B8%D0%B4%D1%8F%D1%87%D0%B8%D0%B9&carId=16234067&fullPath=%2Frailways%2Fsearch%3Fstation_from%3D2700000%26station_to%3D2708001%26departure_date%3D10.05.2021",
                                                callback_data='stan')
        key_third = types.InlineKeyboardButton(text='Завершить покупку', callback_data='end')
        key3.row(key_first)
        key3.row(key_second)
        key3.add(key_third)
        bot.send_message(call.from_user.id, 'Выберите тип билета:', reply_markup=key3)
    elif call.data == 'first8':
        bot.send_message(call.message.chat.id, "Отличный выбор!")
        key3 = types.InlineKeyboardMarkup()
        key_first = types.InlineKeyboardButton(text='Купе',
                                               url="https://aviata.kz/railways/place?from=2700000&to=2708001&number=003%D0%A6&date=2021-05-11%2014%3A35&is_transit=false&car=%D0%9A%D1%83%D0%BF%D0%B5&carId=16262710&fullPath=%2Frailways%2Fsearch%3Fstation_from%3D2700000%26station_to%3D2708001%26departure_date%3D11.05.2021    ",
                                               callback_data='VIP')
        key_second = types.InlineKeyboardButton(text='Плацкарт',
                                                url="https://aviata.kz/railways/place?from=2700000&to=2708001&number=003%D0%A6&date=2021-05-11%2014%3A35&is_transit=false&car=%D0%A1%D0%B8%D0%B4%D1%8F%D1%87%D0%B8%D0%B9&carId=16262709&fullPath=%2Frailways%2Fsearch%3Fstation_from%3D2700000%26station_to%3D2708001%26departure_date%3D11.05.2021",
                                                callback_data='stan')
        key_third = types.InlineKeyboardButton(text='Завершить покупку', callback_data='end')
        key3.row(key_first)
        key3.row(key_second)
        key3.add(key_third)
        bot.send_message(call.from_user.id, 'Выберите тип билета:', reply_markup=key3)
    elif call.data == 'first9':
        bot.send_message(call.message.chat.id, "Отличный выбор!")
        key3 = types.InlineKeyboardMarkup()
        key_first = types.InlineKeyboardButton(text='Купе',
                                               url="https://aviata.kz/railways/place?from=2700000&to=2708001&number=003%D0%A6&date=2021-05-12%2014%3A35&is_transit=false&car=%D0%9A%D1%83%D0%BF%D0%B5&carId=16288720&fullPath=%2Frailways%2Fsearch%3Fstation_from%3D2700000%26station_to%3D2708001%26departure_date%3D12.05.2021",
                                               callback_data='VIP')
        key_second = types.InlineKeyboardButton(text='Плацкарт',
                                                url="https://aviata.kz/railways/place?from=2700000&to=2708001&number=003%D0%A6&date=2021-05-12%2014%3A35&is_transit=false&car=%D0%A1%D0%B8%D0%B4%D1%8F%D1%87%D0%B8%D0%B9&carId=16288719&fullPath=%2Frailways%2Fsearch%3Fstation_from%3D2700000%26station_to%3D2708001%26departure_date%3D12.05.2021",
                                                callback_data='stan')
        key_third = types.InlineKeyboardButton(text='Завершить покупку', callback_data='end')
        key3.row(key_first)
        key3.row(key_second)
        key3.add(key_third)
        bot.send_message(call.from_user.id, 'Выберите тип билета:', reply_markup=key3)
    elif call.data == 'first10':
        bot.send_message(call.message.chat.id, "Отличный выбор!")
        key3 = types.InlineKeyboardMarkup()
        key_first = types.InlineKeyboardButton(text='Купе',
                                               url="https://aviata.kz/railways/place?from=2700000&to=2708001&number=003%D0%A6&date=2021-05-13%2014%3A35&is_transit=false&car=%D0%9A%D1%83%D0%BF%D0%B5&carId=16318742&fullPath=%2Frailways%2Fsearch%3Fstation_from%3D2700000%26station_to%3D2708001%26departure_date%3D13.05.2021",
                                               callback_data='VIP')
        key_second = types.InlineKeyboardButton(text='Плацкарт',
                                                url="https://aviata.kz/railways/place?from=2700000&to=2708001&number=003%D0%A6&date=2021-05-13%2014%3A35&is_transit=false&car=%D0%A1%D0%B8%D0%B4%D1%8F%D1%87%D0%B8%D0%B9&carId=16318741&fullPath=%2Frailways%2Fsearch%3Fstation_from%3D2700000%26station_to%3D2708001%26departure_date%3D13.05.2021",
                                                callback_data='stan')
        key_third = types.InlineKeyboardButton(text='Завершить покупку', callback_data='end')
        key3.row(key_first)
        key3.row(key_second)
        key3.add(key_third)
        bot.send_message(call.from_user.id, 'Выберите тип билета:', reply_markup=key3)
    elif call.data == 'first11':
        bot.send_message(call.message.chat.id, "Отличный выбор!")
        key3 = types.InlineKeyboardMarkup()
        key_first = types.InlineKeyboardButton(text='Купе',
                                               url="https://aviata.kz/railways/place?from=2700000&to=2708001&number=003%D0%A6&date=2021-05-14%2014%3A35&is_transit=false&car=%D0%9A%D1%83%D0%BF%D0%B5&carId=16342241&fullPath=%2Frailways%2Fsearch%3Fstation_from%3D2700000%26station_to%3D2708001%26departure_date%3D14.05.2021",
                                               callback_data='VIP')
        key_second = types.InlineKeyboardButton(text='Плацкарт',
                                                url="https://aviata.kz/railways/place?from=2700000&to=2708001&number=003%D0%A6&date=2021-05-14%2014%3A35&is_transit=false&car=%D0%A1%D0%B8%D0%B4%D1%8F%D1%87%D0%B8%D0%B9&carId=16342240&fullPath=%2Frailways%2Fsearch%3Fstation_from%3D2700000%26station_to%3D2708001%26departure_date%3D14.05.2021",
                                                callback_data='stan')
        key_third = types.InlineKeyboardButton(text='Завершить покупку', callback_data='end')
        key3.row(key_first)
        key3.row(key_second)
        key3.add(key_third)
        bot.send_message(call.from_user.id, 'Выберите тип билета:', reply_markup=key3)
    elif call.data == 'first12':
        bot.send_message(call.message.chat.id, "Отличный выбор!")
        key3 = types.InlineKeyboardMarkup()
        key_first = types.InlineKeyboardButton(text='Купе',
                                               url="https://aviata.kz/railways/place?from=2700000&to=2708001&number=003%D0%A6&date=2021-05-15%2014%3A35&is_transit=false&car=%D0%9A%D1%83%D0%BF%D0%B5&carId=16366879&fullPath=%2Frailways%2Fsearch%3Fstation_from%3D2700000%26station_to%3D2708001%26departure_date%3D15.05.2021",
                                               callback_data='VIP')
        key_second = types.InlineKeyboardButton(text='Плацкарт',
                                                url="https://aviata.kz/railways/place?from=2700000&to=2708001&number=003%D0%A6&date=2021-05-15%2014%3A35&is_transit=false&car=%D0%A1%D0%B8%D0%B4%D1%8F%D1%87%D0%B8%D0%B9&carId=16366878&fullPath=%2Frailways%2Fsearch%3Fstation_from%3D2700000%26station_to%3D2708001%26departure_date%3D15.05.2021",
                                                callback_data='stan')
        key_third = types.InlineKeyboardButton(text='Завершить покупку', callback_data='end')
        key3.row(key_first)
        key3.row(key_second)
        key3.add(key_third)
        bot.send_message(call.from_user.id, 'Выберите тип билета:', reply_markup=key3)
    elif call.data == 'first13':
        bot.send_message(call.message.chat.id, "Отличный выбор!")
        key3 = types.InlineKeyboardMarkup()
        key_first = types.InlineKeyboardButton(text='Купе',
                                               url="https://aviata.kz/railways/place?from=2700000&to=2708001&number=003%D0%A6&date=2021-05-16%2014%3A35&is_transit=false&car=%D0%9A%D1%83%D0%BF%D0%B5&carId=16413231&fullPath=%2Frailways%2Fsearch%3Fstation_from%3D2700000%26station_to%3D2708001%26departure_date%3D16.05.2021",
                                               callback_data='VIP')
        key_second = types.InlineKeyboardButton(text='Плацкарт',
                                                url="https://aviata.kz/railways/place?from=2700000&to=2708001&number=003%D0%A6&date=2021-05-16%2014%3A35&is_transit=false&car=%D0%A1%D0%B8%D0%B4%D1%8F%D1%87%D0%B8%D0%B9&carId=16413230&fullPath=%2Frailways%2Fsearch%3Fstation_from%3D2700000%26station_to%3D2708001%26departure_date%3D16.05.2021",
                                                callback_data='stan')
        key_third = types.InlineKeyboardButton(text='Завершить покупку', callback_data='end')
        key3.row(key_first)
        key3.row(key_second)
        key3.add(key_third)
        bot.send_message(call.from_user.id, 'Выберите тип билета:', reply_markup=key3)
    elif call.data == 'first14':
        bot.send_message(call.message.chat.id, "Отличный выбор!")
        key3 = types.InlineKeyboardMarkup()
        key_first = types.InlineKeyboardButton(text='Купе',
                                               url="https://aviata.kz/railways/place?from=2700000&to=2708001&number=003%D0%A6&date=2021-05-17%2014%3A35&is_transit=false&car=%D0%9A%D1%83%D0%BF%D0%B5&carId=16431139&fullPath=%2Frailways%2Fsearch%3Fstation_from%3D2700000%26station_to%3D2708001%26departure_date%3D17.05.2021",
                                               callback_data='VIP')
        key_second = types.InlineKeyboardButton(text='Плацкарт',
                                                url="https://aviata.kz/railways/place?from=2700000&to=2708001&number=003%D0%A6&date=2021-05-17%2014%3A35&is_transit=false&car=%D0%A1%D0%B8%D0%B4%D1%8F%D1%87%D0%B8%D0%B9&carId=16431138&fullPath=%2Frailways%2Fsearch%3Fstation_from%3D2700000%26station_to%3D2708001%26departure_date%3D17.05.2021",
                                                callback_data='stan')
        key_third = types.InlineKeyboardButton(text='Завершить покупку', callback_data='end')
        key3.row(key_first)
        key3.row(key_second)
        key3.add(key_third)
        bot.send_message(call.from_user.id, 'Выберите тип билета:', reply_markup=key3)
    elif call.data == 'first15':
        bot.send_message(call.message.chat.id, "Отличный выбор!")
        key3 = types.InlineKeyboardMarkup()
        key_first = types.InlineKeyboardButton(text='Купе',
                                               url="https://aviata.kz/railways/place?from=2700000&to=2708001&number=003%D0%A6&date=2021-05-18%2014%3A35&is_transit=false&car=%D0%9A%D1%83%D0%BF%D0%B5&carId=16451637&fullPath=%2Frailways%2Fsearch%3Fstation_from%3D2700000%26station_to%3D2708001%26departure_date%3D18.05.2021",
                                               callback_data='VIP')
        key_second = types.InlineKeyboardButton(text='Плацкарт',
                                                url="https://aviata.kz/railways/place?from=2700000&to=2708001&number=003%D0%A6&date=2021-05-18%2014%3A35&is_transit=false&car=%D0%A1%D0%B8%D0%B4%D1%8F%D1%87%D0%B8%D0%B9&carId=16451636&fullPath=%2Frailways%2Fsearch%3Fstation_from%3D2700000%26station_to%3D2708001%26departure_date%3D18.05.2021",
                                                callback_data='stan')
        key_third = types.InlineKeyboardButton(text='Завершить покупку', callback_data='end')
        key3.row(key_first)
        key3.row(key_second)
        key3.add(key_third)
        bot.send_message(call.from_user.id, 'Выберите тип билета:', reply_markup=key3)
    elif call.data == 'first16':
        bot.send_message(call.message.chat.id, "Отличный выбор!")
        key3 = types.InlineKeyboardMarkup()
        key_first = types.InlineKeyboardButton(text='Купе',
                                               url="https://aviata.kz/railways/place?from=2700000&to=2708001&number=003%D0%A6&date=2021-05-19%2014%3A35&is_transit=false&car=%D0%9A%D1%83%D0%BF%D0%B5&carId=16480693&fullPath=%2Frailways%2Fsearch%3Fstation_from%3D2700000%26station_to%3D2708001%26departure_date%3D19.05.2021",
                                               callback_data='VIP')
        key_second = types.InlineKeyboardButton(text='Плацкарт',
                                                url="https://aviata.kz/railways/place?from=2700000&to=2708001&number=003%D0%A6&date=2021-05-19%2014%3A35&is_transit=false&car=%D0%A1%D0%B8%D0%B4%D1%8F%D1%87%D0%B8%D0%B9&carId=16480692&fullPath=%2Frailways%2Fsearch%3Fstation_from%3D2700000%26station_to%3D2708001%26departure_date%3D19.05.2021",
                                                callback_data='stan')
        key_third = types.InlineKeyboardButton(text='Завершить покупку', callback_data='end')
        key3.row(key_first)
        key3.row(key_second)
        key3.add(key_third)
        bot.send_message(call.from_user.id, 'Выберите тип билета:', reply_markup=key3)

    elif call.data == 'first17':
        bot.send_message(call.message.chat.id, "Отличный выбор!")
        key3 = types.InlineKeyboardMarkup()
        key_first = types.InlineKeyboardButton(text='Купе',
                                               url="https://aviata.kz/railways/place?from=2700000&to=2708001&number=003%D0%A6&date=2021-05-20%2014%3A35&is_transit=false&car=%D0%9A%D1%83%D0%BF%D0%B5&carId=16507350&fullPath=%2Frailways%2Fsearch%3Fstation_from%3D2700000%26station_to%3D2708001%26departure_date%3D20.05.2021",
                                               callback_data='VIP')
        key_second = types.InlineKeyboardButton(text='Плацкарт',
                                                url="https://aviata.kz/railways/place?from=2700000&to=2708001&number=003%D0%A6&date=2021-05-20%2014%3A35&is_transit=false&car=%D0%A1%D0%B8%D0%B4%D1%8F%D1%87%D0%B8%D0%B9&carId=16507349&fullPath=%2Frailways%2Fsearch%3Fstation_from%3D2700000%26station_to%3D2708001%26departure_date%3D20.05.2021",
                                                callback_data='stan')
        key_third = types.InlineKeyboardButton(text='Завершить покупку', callback_data='end')
        key3.row(key_first)
        key3.row(key_second)
        key3.add(key_third)
        bot.send_message(call.from_user.id, 'Выберите тип билета:', reply_markup=key3)

    elif call.data == 'first18':
        bot.send_message(call.message.chat.id, "Отличный выбор!")
        key3 = types.InlineKeyboardMarkup()
        key_first = types.InlineKeyboardButton(text='Купе',
                                               url="https://aviata.kz/railways/place?from=2700000&to=2708001&number=003%D0%A6&date=2021-05-21%2014%3A35&is_transit=false&car=%D0%9A%D1%83%D0%BF%D0%B5&carId=16533029&fullPath=%2Frailways%2Fsearch%3Fstation_from%3D2700000%26station_to%3D2708001%26departure_date%3D21.05.2021",
                                               callback_data='VIP')
        key_second = types.InlineKeyboardButton(text='Плацкарт',
                                                url="https://aviata.kz/railways/place?from=2700000&to=2708001&number=003%D0%A6&date=2021-05-21%2014%3A35&is_transit=false&car=%D0%A1%D0%B8%D0%B4%D1%8F%D1%87%D0%B8%D0%B9&carId=16533028&fullPath=%2Frailways%2Fsearch%3Fstation_from%3D2700000%26station_to%3D2708001%26departure_date%3D21.05.2021",
                                                callback_data='stan')
        key_third = types.InlineKeyboardButton(text='Завершить покупку', callback_data='end')
        key3.row(key_first)
        key3.row(key_second)
        key3.add(key_third)
        bot.send_message(call.from_user.id, 'Выберите тип билета:', reply_markup=key3)

    elif call.data == 'first19':
        bot.send_message(call.message.chat.id, "Отличный выбор!")
        key3 = types.InlineKeyboardMarkup()
        key_first = types.InlineKeyboardButton(text='Купе',
                                               url="https://aviata.kz/railways/place?from=2700000&to=2708001&number=003%D0%A6&date=2021-05-22%2014%3A35&is_transit=false&car=%D0%9A%D1%83%D0%BF%D0%B5&carId=16571881&fullPath=%2Frailways%2Fsearch%3Fstation_from%3D2700000%26station_to%3D2708001%26departure_date%3D22.05.2021",
                                               callback_data='VIP')
        key_second = types.InlineKeyboardButton(text='Плацкарт',
                                                url="https://aviata.kz/railways/place?from=2700000&to=2708001&number=003%D0%A6&date=2021-05-22%2014%3A35&is_transit=false&car=%D0%A1%D0%B8%D0%B4%D1%8F%D1%87%D0%B8%D0%B9&carId=16571880&fullPath=%2Frailways%2Fsearch%3Fstation_from%3D2700000%26station_to%3D2708001%26departure_date%3D22.05.2021",
                                                callback_data='stan')
        key_third = types.InlineKeyboardButton(text='Завершить покупку', callback_data='end')
        key3.row(key_first)
        key3.row(key_second)
        key3.add(key_third)
        bot.send_message(call.from_user.id, 'Выберите тип билета:', reply_markup=key3)
    elif call.data == 'first20':
        bot.send_message(call.message.chat.id, "Отличный выбор!")
        key3 = types.InlineKeyboardMarkup()
        key_first = types.InlineKeyboardButton(text='Купе',
                                               url="https://aviata.kz/railways/place?from=2700000&to=2708001&number=003%D0%A6&date=2021-05-23%2014%3A35&is_transit=false&car=%D0%9A%D1%83%D0%BF%D0%B5&carId=16589288&fullPath=%2Frailways%2Fsearch%3Fstation_from%3D2700000%26station_to%3D2708001%26departure_date%3D23.05.2021",
                                               callback_data='VIP')
        key_second = types.InlineKeyboardButton(text='Плацкарт',
                                                url="https://aviata.kz/railways/place?from=2700000&to=2708001&number=003%D0%A6&date=2021-05-23%2014%3A35&is_transit=false&car=%D0%A1%D0%B8%D0%B4%D1%8F%D1%87%D0%B8%D0%B9&carId=16589287&fullPath=%2Frailways%2Fsearch%3Fstation_from%3D2700000%26station_to%3D2708001%26departure_date%3D23.05.2021",
                                                callback_data='stan')
        key_third = types.InlineKeyboardButton(text='Завершить покупку', callback_data='end')
        key3.row(key_first)
        key3.row(key_second)
        key3.add(key_third)
        bot.send_message(call.from_user.id, 'Выберите тип билета:', reply_markup=key3)
    elif call.data == 'first21':
        bot.send_message(call.message.chat.id, "Отличный выбор!")
        key3 = types.InlineKeyboardMarkup()
        key_first = types.InlineKeyboardButton(text='Купе',
                                               url="https://aviata.kz/railways/place?from=2700000&to=2708001&number=003%D0%A6&date=2021-05-24%2014%3A35&is_transit=false&car=%D0%9A%D1%83%D0%BF%D0%B5&carId=16614045&fullPath=%2Frailways%2Fsearch%3Fstation_from%3D2700000%26station_to%3D2708001%26departure_date%3D24.05.2021",
                                               callback_data='VIP')
        key_second = types.InlineKeyboardButton(text='Плацкарт',
                                                url="https://aviata.kz/railways/place?from=2700000&to=2708001&number=003%D0%A6&date=2021-05-24%2014%3A35&is_transit=false&car=%D0%A1%D0%B8%D0%B4%D1%8F%D1%87%D0%B8%D0%B9&carId=16614044&fullPath=%2Frailways%2Fsearch%3Fstation_from%3D2700000%26station_to%3D2708001%26departure_date%3D24.05.2021",
                                                callback_data='stan')
        key_third = types.InlineKeyboardButton(text='Завершить покупку', callback_data='end')
        key3.row(key_first)
        key3.row(key_second)
        key3.add(key_third)
        bot.send_message(call.from_user.id, 'Выберите тип билета:', reply_markup=key3)
    elif call.data == 'first22':
        bot.send_message(call.message.chat.id, "Отличный выбор!")
        key3 = types.InlineKeyboardMarkup()
        key_first = types.InlineKeyboardButton(text='Купе',
                                               url="https://aviata.kz/railways/place?from=2700000&to=2708001&number=003%D0%A6&date=2021-05-25%2014%3A35&is_transit=false&car=%D0%9A%D1%83%D0%BF%D0%B5&carId=16635727&fullPath=%2Frailways%2Fsearch%3Fstation_from%3D2700000%26station_to%3D2708001%26departure_date%3D25.05.2021",
                                               callback_data='VIP')
        key_second = types.InlineKeyboardButton(text='Плацкарт',
                                                url="https://aviata.kz/railways/place?from=2700000&to=2708001&number=003%D0%A6&date=2021-05-25%2014%3A35&is_transit=false&car=%D0%A1%D0%B8%D0%B4%D1%8F%D1%87%D0%B8%D0%B9&carId=16635726&fullPath=%2Frailways%2Fsearch%3Fstation_from%3D2700000%26station_to%3D2708001%26departure_date%3D25.05.2021 ",
                                                callback_data='stan')
        key_third = types.InlineKeyboardButton(text='Завершить покупку', callback_data='end')
        key3.row(key_first)
        key3.row(key_second)
        key3.add(key_third)
        bot.send_message(call.from_user.id, 'Выберите тип билета:', reply_markup=key3)

    elif call.data == 'first23':
        bot.send_message(call.message.chat.id, "Отличный выбор!")
        key3 = types.InlineKeyboardMarkup()
        key_first = types.InlineKeyboardButton(text='Купе',
                                               url="https://aviata.kz/railways/place?from=2700000&to=2708001&number=015%D0%A2&date=2021-05-26%2015%3A43&is_transit=false&car=%D0%9A%D1%83%D0%BF%D0%B5&carId=16664383&fullPath=%2Frailways%2Fsearch%3Fstation_from%3D2700000%26station_to%3D2708001%26departure_date%3D26.05.2021",
                                               callback_data='VIP')
        key_second = types.InlineKeyboardButton(text='Плацкарт',
                                                url="https://aviata.kz/railways/place?from=2700000&to=2708001&number=003%D0%A6&date=2021-05-26%2014%3A35&is_transit=false&car=%D0%A1%D0%B8%D0%B4%D1%8F%D1%87%D0%B8%D0%B9&carId=16664379&fullPath=%2Frailways%2Fsearch%3Fstation_from%3D2700000%26station_to%3D2708001%26departure_date%3D26.05.2021 ",
                                                callback_data='stan')
        key_third = types.InlineKeyboardButton(text='Завершить покупку', callback_data='end')
        key3.row(key_first)
        key3.row(key_second)
        key3.add(key_third)
        bot.send_message(call.from_user.id, 'Выберите тип билета:', reply_markup=key3)

    elif call.data == 'first24':
        bot.send_message(call.message.chat.id, "Отличный выбор!")
        key3 = types.InlineKeyboardMarkup()
        key_first = types.InlineKeyboardButton(text='Купе',
                                               url="https://aviata.kz/railways/place?from=2700000&to=2708001&number=003%D0%A6&date=2021-05-27%2014%3A35&is_transit=false&car=%D0%9A%D1%83%D0%BF%D0%B5&carId=16691818&fullPath=%2Frailways%2Fsearch%3Fstation_from%3D2700000%26station_to%3D2708001%26departure_date%3D27.05.2021",
                                               callback_data='VIP')
        key_second = types.InlineKeyboardButton(text='Плацкарт',
                                                url="https://aviata.kz/railways/place?from=2700000&to=2708001&number=003%D0%A6&date=2021-05-27%2014%3A35&is_transit=false&car=%D0%A1%D0%B8%D0%B4%D1%8F%D1%87%D0%B8%D0%B9&carId=16691817&fullPath=%2Frailways%2Fsearch%3Fstation_from%3D2700000%26station_to%3D2708001%26departure_date%3D27.05.2021",
                                                callback_data='stan')
        key_third = types.InlineKeyboardButton(text='Завершить покупку', callback_data='end')
        key3.row(key_first)
        key3.row(key_second)
        key3.add(key_third)
        bot.send_message(call.from_user.id, 'Выберите тип билета:', reply_markup=key3)

    elif call.data == 'first25':
        bot.send_message(call.message.chat.id, "Отличный выбор!")
        key3 = types.InlineKeyboardMarkup()
        key_first = types.InlineKeyboardButton(text='Купе',
                                               url="https://aviata.kz/railways/place?from=2700000&to=2708001&number=003%D0%A6&date=2021-05-28%2014%3A35&is_transit=false&car=%D0%9A%D1%83%D0%BF%D0%B5&carId=16709502&fullPath=%2Frailways%2Fsearch%3Fstation_from%3D2700000%26station_to%3D2708001%26departure_date%3D28.05.2021",
                                               callback_data='VIP')
        key_second = types.InlineKeyboardButton(text='Плацкарт',
                                                url="https://aviata.kz/railways/place?from=2700000&to=2708001&number=003%D0%A6&date=2021-05-28%2014%3A35&is_transit=false&car=%D0%A1%D0%B8%D0%B4%D1%8F%D1%87%D0%B8%D0%B9&carId=16709501&fullPath=%2Frailways%2Fsearch%3Fstation_from%3D2700000%26station_to%3D2708001%26departure_date%3D28.05.2021",
                                                callback_data='stan')
        key_third = types.InlineKeyboardButton(text='Завершить покупку', callback_data='end')
        key3.row(key_first)
        key3.row(key_second)
        key3.add(key_third)
        bot.send_message(call.from_user.id, 'Выберите тип билета:', reply_markup=key3)

    elif call.data == 'first26':
        bot.send_message(call.message.chat.id, "Отличный выбор!")
        key3 = types.InlineKeyboardMarkup()
        key_first = types.InlineKeyboardButton(text='Купе',
                                               url="https://aviata.kz/railways/place?from=2700000&to=2708001&number=003%D0%A6&date=2021-05-29%2014%3A35&is_transit=false&car=%D0%9A%D1%83%D0%BF%D0%B5&carId=16737081&fullPath=%2Frailways%2Fsearch%3Fstation_from%3D2700000%26station_to%3D2708001%26departure_date%3D29.05.2021",
                                               callback_data='VIP')
        key_second = types.InlineKeyboardButton(text='Плацкарт',
                                                url="https://aviata.kz/railways/place?from=2700000&to=2708001&number=003%D0%A6&date=2021-05-29%2014%3A35&is_transit=false&car=%D0%A1%D0%B8%D0%B4%D1%8F%D1%87%D0%B8%D0%B9&carId=16737080&fullPath=%2Frailways%2Fsearch%3Fstation_from%3D2700000%26station_to%3D2708001%26departure_date%3D29.05.2021",
                                                callback_data='stan')
        key_third = types.InlineKeyboardButton(text='Завершить покупку', callback_data='end')
        key3.row(key_first)
        key3.row(key_second)
        key3.add(key_third)
        bot.send_message(call.from_user.id, 'Выберите тип билета:', reply_markup=key3)

    elif call.data == 'first27':
        bot.send_message(call.message.chat.id, "Отличный выбор!")
        key3 = types.InlineKeyboardMarkup()
        key_first = types.InlineKeyboardButton(text='Купе',
                                               url="https://aviata.kz/railways/place?from=2700000&to=2708001&number=003%D0%A6&date=2021-05-30%2014%3A35&is_transit=false&car=%D0%9A%D1%83%D0%BF%D0%B5&carId=16781338&fullPath=%2Frailways%2Fsearch%3Fstation_from%3D2700000%26station_to%3D2708001%26departure_date%3D30.05.2021",
                                               callback_data='VIP')
        key_second = types.InlineKeyboardButton(text='Плацкарт',
                                                url="https://aviata.kz/railways/place?from=2700000&to=2708001&number=003%D0%A6&date=2021-05-30%2014%3A35&is_transit=false&car=%D0%A1%D0%B8%D0%B4%D1%8F%D1%87%D0%B8%D0%B9&carId=16781337&fullPath=%2Frailways%2Fsearch%3Fstation_from%3D2700000%26station_to%3D2708001%26departure_date%3D30.05.2021",
                                                callback_data='stan')
        key_third = types.InlineKeyboardButton(text='Завершить покупку', callback_data='end')
        key3.row(key_first)
        key3.row(key_second)
        key3.add(key_third)
        bot.send_message(call.from_user.id, 'Выберите тип билета:', reply_markup=key3)

    elif call.data == 'a4':
        bot.send_message(call.message.chat.id, "Отличный выбор!")
        key3 = types.InlineKeyboardMarkup()
        key_first = types.InlineKeyboardButton(text='Купе',
                                               url="https://aviata.kz/railways/place?from=2708001&to=2700000&number=004%D0%A6&date=2021-05-04%2015%3A33&is_transit=false&car=%D0%9A%D1%83%D0%BF%D0%B5&carId=16078715&fullPath=%2Frailways%2Fsearch%3Fstation_from%3D2708001%26station_to%3D2700000%26departure_date%3D04.05.2021",
                                               callback_data='VIP')
        key_second = types.InlineKeyboardButton(text='Плацкарт',
                                                url="https://aviata.kz/railways/place?from=2708001&to=2700000&number=004%D0%A6&date=2021-05-04%2015%3A33&is_transit=false&car=%D0%A1%D0%B8%D0%B4%D1%8F%D1%87%D0%B8%D0%B9&carId=16078714&fullPath=%2Frailways%2Fsearch%3Fstation_from%3D2708001%26station_to%3D2700000%26departure_date%3D04.05.2021",
                                                callback_data='stan')
        key_third = types.InlineKeyboardButton(text='Завершить покупку', callback_data='end')
        key3.row(key_first)
        key3.row(key_second)
        key3.add(key_third)
        bot.send_message(call.from_user.id, 'Выберите тип билета:', reply_markup=key3)

    elif call.data == 'a5':
        bot.send_message(call.message.chat.id, "Отличный выбор!")
        key3 = types.InlineKeyboardMarkup()
        key_first = types.InlineKeyboardButton(text='Купе',
                                               url="https://aviata.kz/railways/place?from=2708001&to=2700000&number=004%D0%A6&date=2021-05-05%2015%3A33&is_transit=false&car=%D0%9A%D1%83%D0%BF%D0%B5&carId=16103724&fullPath=%2Frailways%2Fsearch%3Fstation_from%3D2708001%26station_to%3D2700000%26departure_date%3D05.05.2021",
                                               callback_data='VIP')
        key_second = types.InlineKeyboardButton(text='Плацкарт',
                                                url="https://aviata.kz/railways/place?from=2708001&to=2700000&number=004%D0%A6&date=2021-05-05%2015%3A33&is_transit=false&car=%D0%A1%D0%B8%D0%B4%D1%8F%D1%87%D0%B8%D0%B9&carId=16103723&fullPath=%2Frailways%2Fsearch%3Fstation_from%3D2708001%26station_to%3D2700000%26departure_date%3D05.05.2021",
                                                callback_data='stan')
        key_third = types.InlineKeyboardButton(text='Завершить покупку', callback_data='end')
        key3.row(key_first)
        key3.row(key_second)
        key3.add(key_third)
        bot.send_message(call.from_user.id, 'Выберите тип билета:', reply_markup=key3)

    elif call.data == 'a6':
        bot.send_message(call.message.chat.id, "Отличный выбор!")
        key3 = types.InlineKeyboardMarkup()
        key_first = types.InlineKeyboardButton(text='Купе',
                                               url="https://aviata.kz/railways/place?from=2708001&to=2700000&number=004%D0%A6&date=2021-05-06%2015%3A33&is_transit=false&car=%D0%9A%D1%83%D0%BF%D0%B5&carId=16128863&fullPath=%2Frailways%2Fsearch%3Fstation_from%3D2708001%26station_to%3D2700000%26departure_date%3D06.05.2021",
                                               callback_data='VIP')
        key_second = types.InlineKeyboardButton(text='Плацкарт',
                                                url="https://aviata.kz/railways/place?from=2708001&to=2700000&number=004%D0%A6&date=2021-05-06%2015%3A33&is_transit=false&car=%D0%A1%D0%B8%D0%B4%D1%8F%D1%87%D0%B8%D0%B9&carId=16128862&fullPath=%2Frailways%2Fsearch%3Fstation_from%3D2708001%26station_to%3D2700000%26departure_date%3D06.05.2021",
                                                callback_data='stan')
        key_third = types.InlineKeyboardButton(text='Завершить покупку', callback_data='end')
        key3.row(key_first)
        key3.row(key_second)
        key3.add(key_third)
        bot.send_message(call.from_user.id, 'Выберите тип билета:', reply_markup=key3)

    elif call.data == 'a7':
        bot.send_message(call.message.chat.id, "Отличный выбор!")
        key3 = types.InlineKeyboardMarkup()
        key_first = types.InlineKeyboardButton(text='Купе',
                                               url="https://aviata.kz/railways/place?from=2708001&to=2700000&number=004%D0%A6&date=2021-05-07%2015%3A33&is_transit=false&car=%D0%9A%D1%83%D0%BF%D0%B5&carId=16157360&fullPath=%2Frailways%2Fsearch%3Fstation_from%3D2708001%26station_to%3D2700000%26departure_date%3D07.05.2021",
                                               callback_data='VIP')
        key_second = types.InlineKeyboardButton(text='Плацкарт',
                                                url="https://aviata.kz/railways/place?from=2708001&to=2700000&number=004%D0%A6&date=2021-05-07%2015%3A33&is_transit=false&car=%D0%A1%D0%B8%D0%B4%D1%8F%D1%87%D0%B8%D0%B9&carId=16157359&fullPath=%2Frailways%2Fsearch%3Fstation_from%3D2708001%26station_to%3D2700000%26departure_date%3D07.05.2021",
                                                callback_data='stan')
        key_third = types.InlineKeyboardButton(text='Завершить покупку', callback_data='end')
        key3.row(key_first)
        key3.row(key_second)
        key3.add(key_third)
        bot.send_message(call.from_user.id, 'Выберите тип билета:', reply_markup=key3)

    elif call.data == 'a8':
        bot.send_message(call.message.chat.id, "Отличный выбор!")
        key3 = types.InlineKeyboardMarkup()
        key_first = types.InlineKeyboardButton(text='Купе',
                                               url="https://aviata.kz/railways/place?from=2708001&to=2700000&number=004%D0%A6&date=2021-05-08%2015%3A33&is_transit=false&car=%D0%9A%D1%83%D0%BF%D0%B5&carId=16179771&fullPath=%2Frailways%2Fsearch%3Fstation_from%3D2708001%26station_to%3D2700000%26departure_date%3D08.05.2021",
                                               callback_data='VIP')
        key_second = types.InlineKeyboardButton(text='Плацкарт',
                                                url="https://aviata.kz/railways/place?from=2708001&to=2700000&number=004%D0%A6&date=2021-05-08%2015%3A33&is_transit=false&car=%D0%A1%D0%B8%D0%B4%D1%8F%D1%87%D0%B8%D0%B9&carId=16179770&fullPath=%2Frailways%2Fsearch%3Fstation_from%3D2708001%26station_to%3D2700000%26departure_date%3D08.05.2021",
                                                callback_data='stan')
        key_third = types.InlineKeyboardButton(text='Завершить покупку', callback_data='end')
        key3.row(key_first)
        key3.row(key_second)
        key3.add(key_third)
        bot.send_message(call.from_user.id, 'Выберите тип билета:', reply_markup=key3)

    elif call.data == 'a9':
        bot.send_message(call.message.chat.id, "Отличный выбор!")
        key3 = types.InlineKeyboardMarkup()
        key_first = types.InlineKeyboardButton(text='Купе',
                                               url="https://aviata.kz/railways/place?from=2708001&to=2700000&number=004%D0%A6&date=2021-05-09%2015%3A33&is_transit=false&car=%D0%9A%D1%83%D0%BF%D0%B5&carId=16208844&fullPath=%2Frailways%2Fsearch%3Fstation_from%3D2708001%26station_to%3D2700000%26departure_date%3D09.05.2021",
                                               callback_data='VIP')
        key_second = types.InlineKeyboardButton(text='Плацкарт',
                                                url="https://aviata.kz/railways/place?from=2708001&to=2700000&number=004%D0%A6&date=2021-05-09%2015%3A33&is_transit=false&car=%D0%A1%D0%B8%D0%B4%D1%8F%D1%87%D0%B8%D0%B9&carId=16208843&fullPath=%2Frailways%2Fsearch%3Fstation_from%3D2708001%26station_to%3D2700000%26departure_date%3D09.05.2021",
                                                callback_data='stan')
        key_third = types.InlineKeyboardButton(text='Завершить покупку', callback_data='end')
        key3.row(key_first)
        key3.row(key_second)
        key3.add(key_third)
        bot.send_message(call.from_user.id, 'Выберите тип билета:', reply_markup=key3)

    elif call.data == 'a10':
        bot.send_message(call.message.chat.id, "Отличный выбор!")
        key3 = types.InlineKeyboardMarkup()
        key_first = types.InlineKeyboardButton(text='Купе',
                                               url="https://aviata.kz/railways/place?from=2708001&to=2700000&number=004%D0%A6&date=2021-05-10%2015%3A33&is_transit=false&car=%D0%9A%D1%83%D0%BF%D0%B5&carId=16234353&fullPath=%2Frailways%2Fsearch%3Fstation_from%3D2708001%26station_to%3D2700000%26departure_date%3D10.05.2021",
                                               callback_data='VIP')
        key_second = types.InlineKeyboardButton(text='Плацкарт',
                                                url="https://aviata.kz/railways/place?from=2708001&to=2700000&number=004%D0%A6&date=2021-05-10%2015%3A33&is_transit=false&car=%D0%A1%D0%B8%D0%B4%D1%8F%D1%87%D0%B8%D0%B9&carId=16234352&fullPath=%2Frailways%2Fsearch%3Fstation_from%3D2708001%26station_to%3D2700000%26departure_date%3D10.05.2021",
                                                callback_data='stan')
        key_third = types.InlineKeyboardButton(text='Завершить покупку', callback_data='end')
        key3.row(key_first)
        key3.row(key_second)
        key3.add(key_third)
        bot.send_message(call.from_user.id, 'Выберите тип билета:', reply_markup=key3)

    elif call.data == 'a11':
        bot.send_message(call.message.chat.id, "Отличный выбор!")
        key3 = types.InlineKeyboardMarkup()
        key_first = types.InlineKeyboardButton(text='Купе',
                                               url="https://aviata.kz/railways/place?from=2708001&to=2700000&number=004%D0%A6&date=2021-05-11%2015%3A33&is_transit=false&car=%D0%9A%D1%83%D0%BF%D0%B5&carId=16261359&fullPath=%2Frailways%2Fsearch%3Fstation_from%3D2708001%26station_to%3D2700000%26departure_date%3D11.05.2021",
                                               callback_data='VIP')
        key_second = types.InlineKeyboardButton(text='Плацкарт',
                                                url="https://aviata.kz/railways/place?from=2708001&to=2700000&number=004%D0%A6&date=2021-05-11%2015%3A33&is_transit=false&car=%D0%A1%D0%B8%D0%B4%D1%8F%D1%87%D0%B8%D0%B9&carId=16261358&fullPath=%2Frailways%2Fsearch%3Fstation_from%3D2708001%26station_to%3D2700000%26departure_date%3D11.05.2021",
                                                callback_data='stan')
        key_third = types.InlineKeyboardButton(text='Завершить покупку', callback_data='end')
        key3.row(key_first)
        key3.row(key_second)
        key3.add(key_third)
        bot.send_message(call.from_user.id, 'Выберите тип билета:', reply_markup=key3)


    elif call.data == 'a12':
        bot.send_message(call.message.chat.id, "Отличный выбор!")
        key3 = types.InlineKeyboardMarkup()
        key_first = types.InlineKeyboardButton(text='Купе',
                                               url="https://aviata.kz/railways/place?from=2708001&to=2700000&number=004%D0%A6&date=2021-05-12%2015%3A33&is_transit=false&car=%D0%9A%D1%83%D0%BF%D0%B5&carId=16288713&fullPath=%2Frailways%2Fsearch%3Fstation_from%3D2708001%26station_to%3D2700000%26departure_date%3D12.05.2021",
                                               callback_data='VIP')
        key_second = types.InlineKeyboardButton(text='Плацкарт',
                                                url="https://aviata.kz/railways/place?from=2708001&to=2700000&number=004%D0%A6&date=2021-05-12%2015%3A33&is_transit=false&car=%D0%A1%D0%B8%D0%B4%D1%8F%D1%87%D0%B8%D0%B9&carId=16288712&fullPath=%2Frailways%2Fsearch%3Fstation_from%3D2708001%26station_to%3D2700000%26departure_date%3D12.05.2021",
                                                callback_data='stan')
        key_third = types.InlineKeyboardButton(text='Завершить покупку', callback_data='end')
        key3.row(key_first)
        key3.row(key_second)
        key3.add(key_third)
        bot.send_message(call.from_user.id, 'Выберите тип билета:', reply_markup=key3)

    elif call.data == 'a13':
        bot.send_message(call.message.chat.id, "Отличный выбор!")
        key3 = types.InlineKeyboardMarkup()
        key_first = types.InlineKeyboardButton(text='Купе',
                                               url="https://aviata.kz/railways/place?from=2708001&to=2700000&number=010%D0%A2&date=2021-05-13%2021%3A30&is_transit=false&car=%D0%9A%D1%83%D0%BF%D0%B5&carId=16318211&fullPath=%2Frailways%2Fsearch%3Fstation_from%3D2708001%26station_to%3D2700000%26departure_date%3D13.05.2021",
                                               callback_data='VIP')
        key_second = types.InlineKeyboardButton(text='Плацкарт',
                                                url="https://aviata.kz/railways/place?from=2708001&to=2700000&number=004%D0%A6&date=2021-05-13%2015%3A33&is_transit=false&car=%D0%A1%D0%B8%D0%B4%D1%8F%D1%87%D0%B8%D0%B9&carId=16318203&fullPath=%2Frailways%2Fsearch%3Fstation_from%3D2708001%26station_to%3D2700000%26departure_date%3D13.05.2021",
                                                callback_data='stan')
        key_third = types.InlineKeyboardButton(text='Завершить покупку', callback_data='end')
        key3.row(key_first)
        key3.row(key_second)
        key3.add(key_third)
        bot.send_message(call.from_user.id, 'Выберите тип билета:', reply_markup=key3)

    elif call.data == 'a14':
        bot.send_message(call.message.chat.id, "Отличный выбор!")
        key3 = types.InlineKeyboardMarkup()
        key_first = types.InlineKeyboardButton(text='Купе',
                                               url="https://aviata.kz/railways/place?from=2708001&to=2700000&number=004%D0%A6&date=2021-05-14%2015%3A33&is_transit=false&car=%D0%9A%D1%83%D0%BF%D0%B5&carId=16343963&fullPath=%2Frailways%2Fsearch%3Fstation_from%3D2708001%26station_to%3D2700000%26departure_date%3D14.05.2021",
                                               callback_data='VIP')
        key_second = types.InlineKeyboardButton(text='Плацкарт',
                                                    url="https://aviata.kz/railways/place?from=2708001&to=2700000&number=004%D0%A6&date=2021-05-14%2015%3A33&is_transit=false&car=%D0%A1%D0%B8%D0%B4%D1%8F%D1%87%D0%B8%D0%B9&carId=16343962&fullPath=%2Frailways%2Fsearch%3Fstation_from%3D2708001%26station_to%3D2700000%26departure_date%3D14.05.2021",
                                                callback_data='stan')
        key_third = types.InlineKeyboardButton(text='Завершить покупку', callback_data='end')
        key3.row(key_first)
        key3.row(key_second)
        key3.add(key_third)
        bot.send_message(call.from_user.id, 'Выберите тип билета:', reply_markup=key3)

    elif call.data == 'a15':
        bot.send_message(call.message.chat.id, "Отличный выбор!")
        key3 = types.InlineKeyboardMarkup()
        key_first = types.InlineKeyboardButton(text='Купе',
                                               url="https://aviata.kz/railways/place?from=2708001&to=2700000&number=004%D0%A6&date=2021-05-15%2015%3A33&is_transit=false&car=%D0%9A%D1%83%D0%BF%D0%B5&carId=16370037&fullPath=%2Frailways%2Fsearch%3Fstation_from%3D2708001%26station_to%3D2700000%26departure_date%3D15.05.2021",
                                               callback_data='VIP')
        key_second = types.InlineKeyboardButton(text='Плацкарт',
                                                    url="https://aviata.kz/railways/place?from=2708001&to=2700000&number=004%D0%A6&date=2021-05-15%2015%3A33&is_transit=false&car=%D0%A1%D0%B8%D0%B4%D1%8F%D1%87%D0%B8%D0%B9&carId=16370036&fullPath=%2Frailways%2Fsearch%3Fstation_from%3D2708001%26station_to%3D2700000%26departure_date%3D15.05.2021",
                                                callback_data='stan')
        key_third = types.InlineKeyboardButton(text='Завершить покупку', callback_data='end')
        key3.row(key_first)
        key3.row(key_second)
        key3.add(key_third)
        bot.send_message(call.from_user.id, 'Выберите тип билета:', reply_markup=key3)

    elif call.data == 'a16':
        bot.send_message(call.message.chat.id, "Отличный выбор!")
        key3 = types.InlineKeyboardMarkup()
        key_first = types.InlineKeyboardButton(text='Купе',
                                               url="https://aviata.kz/railways/place?from=2708001&to=2700000&number=004%D0%A6&date=2021-05-16%2015%3A33&is_transit=false&car=%D0%9A%D1%83%D0%BF%D0%B5&carId=16402020&fullPath=%2Frailways%2Fsearch%3Fstation_from%3D2708001%26station_to%3D2700000%26departure_date%3D16.05.2021",
                                               callback_data='VIP')
        key_second = types.InlineKeyboardButton(text='Плацкарт',
                                                    url="https://aviata.kz/railways/place?from=2708001&to=2700000&number=004%D0%A6&date=2021-05-16%2015%3A33&is_transit=false&car=%D0%A1%D0%B8%D0%B4%D1%8F%D1%87%D0%B8%D0%B9&carId=16402019&fullPath=%2Frailways%2Fsearch%3Fstation_from%3D2708001%26station_to%3D2700000%26departure_date%3D16.05.2021",
                                                callback_data='stan')
        key_third = types.InlineKeyboardButton(text='Завершить покупку', callback_data='end')
        key3.row(key_first)
        key3.row(key_second)
        key3.add(key_third)
        bot.send_message(call.from_user.id, 'Выберите тип билета:', reply_markup=key3)

    elif call.data == 'a17':
        bot.send_message(call.message.chat.id, "Отличный выбор!")
        key3 = types.InlineKeyboardMarkup()
        key_first = types.InlineKeyboardButton(text='Купе',
                                               url="https://aviata.kz/railways/place?from=2708001&to=2700000&number=004%D0%A6&date=2021-05-17%2015%3A33&is_transit=false&car=%D0%9A%D1%83%D0%BF%D0%B5&carId=16426540&fullPath=%2Frailways%2Fsearch%3Fstation_from%3D2708001%26station_to%3D2700000%26departure_date%3D17.05.2021",
                                               callback_data='VIP')
        key_second = types.InlineKeyboardButton(text='Плацкарт',
                                                    url="https://aviata.kz/railways/place?from=2708001&to=2700000&number=004%D0%A6&date=2021-05-17%2015%3A33&is_transit=false&car=%D0%A1%D0%B8%D0%B4%D1%8F%D1%87%D0%B8%D0%B9&carId=16426539&fullPath=%2Frailways%2Fsearch%3Fstation_from%3D2708001%26station_to%3D2700000%26departure_date%3D17.05.2021",
                                                callback_data='stan')
        key_third = types.InlineKeyboardButton(text='Завершить покупку', callback_data='end')
        key3.row(key_first)
        key3.row(key_second)
        key3.add(key_third)
        bot.send_message(call.from_user.id, 'Выберите тип билета:', reply_markup=key3)

    elif call.data == 'a18':
        bot.send_message(call.message.chat.id, "Отличный выбор!")
        key3 = types.InlineKeyboardMarkup()
        key_first = types.InlineKeyboardButton(text='Купе',
                                               url="https://aviata.kz/railways/place?from=2708001&to=2700000&number=004%D0%A6&date=2021-05-18%2015%3A33&is_transit=false&car=%D0%9A%D1%83%D0%BF%D0%B5&carId=16450341&fullPath=%2Frailways%2Fsearch%3Fstation_from%3D2708001%26station_to%3D2700000%26departure_date%3D18.05.2021",
                                               callback_data='VIP')
        key_second = types.InlineKeyboardButton(text='Плацкарт',
                                                    url="https://aviata.kz/railways/place?from=2708001&to=2700000&number=004%D0%A6&date=2021-05-18%2015%3A33&is_transit=false&car=%D0%A1%D0%B8%D0%B4%D1%8F%D1%87%D0%B8%D0%B9&carId=16450340&fullPath=%2Frailways%2Fsearch%3Fstation_from%3D2708001%26station_to%3D2700000%26departure_date%3D18.05.2021",
                                                callback_data='stan')
        key_third = types.InlineKeyboardButton(text='Завершить покупку', callback_data='end')
        key3.row(key_first)
        key3.row(key_second)
        key3.add(key_third)
        bot.send_message(call.from_user.id, 'Выберите тип билета:', reply_markup=key3)

    elif call.data == 'a19':
        bot.send_message(call.message.chat.id, "Отличный выбор!")
        key3 = types.InlineKeyboardMarkup()
        key_first = types.InlineKeyboardButton(text='Купе',
                                               url="https://aviata.kz/railways/place?from=2708001&to=2700000&number=004%D0%A6&date=2021-05-19%2015%3A33&is_transit=false&car=%D0%9A%D1%83%D0%BF%D0%B5&carId=16477860&fullPath=%2Frailways%2Fsearch%3Fstation_from%3D2708001%26station_to%3D2700000%26departure_date%3D19.05.2021",
                                               callback_data='VIP')
        key_second = types.InlineKeyboardButton(text='Плацкарт',
                                                    url="https://aviata.kz/railways/place?from=2708001&to=2700000&number=004%D0%A6&date=2021-05-19%2015%3A33&is_transit=false&car=%D0%A1%D0%B8%D0%B4%D1%8F%D1%87%D0%B8%D0%B9&carId=16477859&fullPath=%2Frailways%2Fsearch%3Fstation_from%3D2708001%26station_to%3D2700000%26departure_date%3D19.05.2021",
                                                callback_data='stan')
        key_third = types.InlineKeyboardButton(text='Завершить покупку', callback_data='end')
        key3.row(key_first)
        key3.row(key_second)
        key3.add(key_third)
        bot.send_message(call.from_user.id, 'Выберите тип билета:', reply_markup=key3)

    elif call.data == 'a20':
        bot.send_message(call.message.chat.id, "Отличный выбор!")
        key3 = types.InlineKeyboardMarkup()
        key_first = types.InlineKeyboardButton(text='Купе',
                                               url="https://aviata.kz/railways/place?from=2708001&to=2700000&number=004%D0%A6&date=2021-05-20%2015%3A33&is_transit=false&car=%D0%9A%D1%83%D0%BF%D0%B5&carId=16508491&fullPath=%2Frailways%2Fsearch%3Fstation_from%3D2708001%26station_to%3D2700000%26departure_date%3D20.05.2021",
                                               callback_data='VIP')
        key_second = types.InlineKeyboardButton(text='Плацкарт',
                                                    url="https://aviata.kz/railways/place?from=2708001&to=2700000&number=004%D0%A6&date=2021-05-20%2015%3A33&is_transit=false&car=%D0%A1%D0%B8%D0%B4%D1%8F%D1%87%D0%B8%D0%B9&carId=16508490&fullPath=%2Frailways%2Fsearch%3Fstation_from%3D2708001%26station_to%3D2700000%26departure_date%3D20.05.2021",
                                                callback_data='stan')
        key_third = types.InlineKeyboardButton(text='Завершить покупку', callback_data='end')
        key3.row(key_first)
        key3.row(key_second)
        key3.add(key_third)
        bot.send_message(call.from_user.id, 'Выберите тип билета:', reply_markup=key3)

    elif call.data == 'a21':
        bot.send_message(call.message.chat.id, "Отличный выбор!")
        key3 = types.InlineKeyboardMarkup()
        key_first = types.InlineKeyboardButton(text='Купе',
                                               url="https://aviata.kz/railways/place?from=2708001&to=2700000&number=004%D0%A6&date=2021-05-21%2015%3A33&is_transit=false&car=%D0%9A%D1%83%D0%BF%D0%B5&carId=16536321&fullPath=%2Frailways%2Fsearch%3Fstation_from%3D2708001%26station_to%3D2700000%26departure_date%3D21.05.2021",
                                               callback_data='VIP')
        key_second = types.InlineKeyboardButton(text='Плацкарт',
                                                    url="https://aviata.kz/railways/place?from=2708001&to=2700000&number=004%D0%A6&date=2021-05-21%2015%3A33&is_transit=false&car=%D0%A1%D0%B8%D0%B4%D1%8F%D1%87%D0%B8%D0%B9&carId=16536320&fullPath=%2Frailways%2Fsearch%3Fstation_from%3D2708001%26station_to%3D2700000%26departure_date%3D21.05.2021",
                                                callback_data='stan')
        key_third = types.InlineKeyboardButton(text='Завершить покупку', callback_data='end')
        key3.row(key_first)
        key3.row(key_second)
        key3.add(key_third)
        bot.send_message(call.from_user.id, 'Выберите тип билета:', reply_markup=key3)

    elif call.data == 'a22':
        bot.send_message(call.message.chat.id, "Отличный выбор!")
        key3 = types.InlineKeyboardMarkup()
        key_first = types.InlineKeyboardButton(text='Купе',
                                               url="https://aviata.kz/railways/place?from=2708001&to=2700000&number=004%D0%A6&date=2021-05-22%2015%3A33&is_transit=false&car=%D0%9A%D1%83%D0%BF%D0%B5&carId=16558571&fullPath=%2Frailways%2Fsearch%3Fstation_from%3D2708001%26station_to%3D2700000%26departure_date%3D22.05.2021",
                                               callback_data='VIP')
        key_second = types.InlineKeyboardButton(text='Плацкарт',
                                                    url="https://aviata.kz/railways/place?from=2708001&to=2700000&number=004%D0%A6&date=2021-05-22%2015%3A33&is_transit=false&car=%D0%A1%D0%B8%D0%B4%D1%8F%D1%87%D0%B8%D0%B9&carId=16558570&fullPath=%2Frailways%2Fsearch%3Fstation_from%3D2708001%26station_to%3D2700000%26departure_date%3D22.05.2021",
                                                callback_data='stan')
        key_third = types.InlineKeyboardButton(text='Завершить покупку', callback_data='end')
        key3.row(key_first)
        key3.row(key_second)
        key3.add(key_third)
        bot.send_message(call.from_user.id, 'Выберите тип билета:', reply_markup=key3)

    elif call.data == 'a23':
        bot.send_message(call.message.chat.id, "Отличный выбор!")
        key3 = types.InlineKeyboardMarkup()
        key_first = types.InlineKeyboardButton(text='Купе',
                                               url="https://aviata.kz/railways/place?from=2708001&to=2700000&number=004%D0%A6&date=2021-05-22%2015%3A33&is_transit=false&car=%D0%9A%D1%83%D0%BF%D0%B5&carId=16558571&fullPath=%2Frailways%2Fsearch%3Fstation_from%3D2708001%26station_to%3D2700000%26departure_date%3D22.05.2021",
                                               callback_data='VIP')
        key_second = types.InlineKeyboardButton(text='Плацкарт',
                                                    url="https://aviata.kz/railways/place?from=2708001&to=2700000&number=004%D0%A6&date=2021-05-22%2015%3A33&is_transit=false&car=%D0%A1%D0%B8%D0%B4%D1%8F%D1%87%D0%B8%D0%B9&carId=16558570&fullPath=%2Frailways%2Fsearch%3Fstation_from%3D2708001%26station_to%3D2700000%26departure_date%3D22.05.2021",
                                                callback_data='stan')
        key_third = types.InlineKeyboardButton(text='Завершить покупку', callback_data='end')
        key3.row(key_first)
        key3.row(key_second)
        key3.add(key_third)
        bot.send_message(call.from_user.id, 'Выберите тип билета:', reply_markup=key3)


    elif call.data == 'a24':
        bot.send_message(call.message.chat.id, "Отличный выбор!")
        key3 = types.InlineKeyboardMarkup()
        key_first = types.InlineKeyboardButton(text='Купе',
                                               url="https://aviata.kz/railways/place?from=2708001&to=2700000&number=004%D0%A6&date=2021-05-24%2015%3A33&is_transit=false&car=%D0%9A%D1%83%D0%BF%D0%B5&carId=16613358&fullPath=%2Frailways%2Fsearch%3Fstation_from%3D2708001%26station_to%3D2700000%26departure_date%3D24.05.2021",
                                               callback_data='VIP')
        key_second = types.InlineKeyboardButton(text='Плацкарт',
                                                    url="https://aviata.kz/railways/place?from=2708001&to=2700000&number=004%D0%A6&date=2021-05-24%2015%3A33&is_transit=false&car=%D0%A1%D0%B8%D0%B4%D1%8F%D1%87%D0%B8%D0%B9&carId=16613357&fullPath=%2Frailways%2Fsearch%3Fstation_from%3D2708001%26station_to%3D2700000%26departure_date%3D24.05.2021",
                                                callback_data='stan')
        key_third = types.InlineKeyboardButton(text='Завершить покупку', callback_data='end')
        key3.row(key_first)
        key3.row(key_second)
        key3.add(key_third)
        bot.send_message(call.from_user.id, 'Выберите тип билета:', reply_markup=key3)

    elif call.data == 'a25':
        bot.send_message(call.message.chat.id, "Отличный выбор!")
        key3 = types.InlineKeyboardMarkup()
        key_first = types.InlineKeyboardButton(text='Купе',
                                               url="https://aviata.kz/railways/place?from=2708001&to=2700000&number=010%D0%A2&date=2021-05-25%2021%3A30&is_transit=false&car=%D0%9A%D1%83%D0%BF%D0%B5&carId=16647164&fullPath=%2Frailways%2Fsearch%3Fstation_from%3D2708001%26station_to%3D2700000%26departure_date%3D25.05.2021",
                                               callback_data='VIP')
        key_second = types.InlineKeyboardButton(text='Плацкарт',
                                                    url="https://aviata.kz/railways/place?from=2708001&to=2700000&number=004%D0%A6&date=2021-05-25%2015%3A33&is_transit=false&car=%D0%A1%D0%B8%D0%B4%D1%8F%D1%87%D0%B8%D0%B9&carId=16647156&fullPath=%2Frailways%2Fsearch%3Fstation_from%3D2708001%26station_to%3D2700000%26departure_date%3D25.05.2021",
                                                callback_data='stan')
        key_third = types.InlineKeyboardButton(text='Завершить покупку', callback_data='end')
        key3.row(key_first)
        key3.row(key_second)
        key3.add(key_third)
        bot.send_message(call.from_user.id, 'Выберите тип билета:', reply_markup=key3)

    elif call.data == 'a26':
        bot.send_message(call.message.chat.id, "Отличный выбор!")
        key3 = types.InlineKeyboardMarkup()
        key_first = types.InlineKeyboardButton(text='Купе',
                                               url="https://aviata.kz/railways/place?from=2708001&to=2700000&number=004%D0%A6&date=2021-05-26%2015%3A33&is_transit=false&car=%D0%9A%D1%83%D0%BF%D0%B5&carId=16665242&fullPath=%2Frailways%2Fsearch%3Fstation_from%3D2708001%26station_to%3D2700000%26departure_date%3D26.05.2021",
                                               callback_data='VIP')
        key_second = types.InlineKeyboardButton(text='Плацкарт',
                                                    url="https://aviata.kz/railways/place?from=2708001&to=2700000&number=004%D0%A6&date=2021-05-26%2015%3A33&is_transit=false&car=%D0%A1%D0%B8%D0%B4%D1%8F%D1%87%D0%B8%D0%B9&carId=16665241&fullPath=%2Frailways%2Fsearch%3Fstation_from%3D2708001%26station_to%3D2700000%26departure_date%3D26.05.2021",
                                                callback_data='stan')
        key_third = types.InlineKeyboardButton(text='Завершить покупку', callback_data='end')
        key3.row(key_first)
        key3.row(key_second)
        key3.add(key_third)
        bot.send_message(call.from_user.id, 'Выберите тип билета:', reply_markup=key3)

    elif call.data == 'a27':
        bot.send_message(call.message.chat.id, "Отличный выбор!")
        key3 = types.InlineKeyboardMarkup()
        key_first = types.InlineKeyboardButton(text='Купе',
                                               url="https://aviata.kz/railways/place?from=2708001&to=2700000&number=004%D0%A6&date=2021-05-27%2015%3A33&is_transit=false&car=%D0%9A%D1%83%D0%BF%D0%B5&carId=16691835&fullPath=%2Frailways%2Fsearch%3Fstation_from%3D2708001%26station_to%3D2700000%26departure_date%3D27.05.2021",
                                               callback_data='VIP')
        key_second = types.InlineKeyboardButton(text='Плацкарт',
                                                    url="https://aviata.kz/railways/place?from=2708001&to=2700000&number=004%D0%A6&date=2021-05-27%2015%3A33&is_transit=false&car=%D0%A1%D0%B8%D0%B4%D1%8F%D1%87%D0%B8%D0%B9&carId=16691834&fullPath=%2Frailways%2Fsearch%3Fstation_from%3D2708001%26station_to%3D2700000%26departure_date%3D27.05.2021",
                                                callback_data='stan')
        key_third = types.InlineKeyboardButton(text='Завершить покупку', callback_data='end')
        key3.row(key_first)
        key3.row(key_second)
        key3.add(key_third)
        bot.send_message(call.from_user.id, 'Выберите тип билета:', reply_markup=key3)

    elif call.data == 'a28':
        bot.send_message(call.message.chat.id, "Отличный выбор!")
        key3 = types.InlineKeyboardMarkup()
        key_first = types.InlineKeyboardButton(text='Купе',
                                               url="https://aviata.kz/railways/place?from=2708001&to=2700000&number=004%D0%A6&date=2021-05-28%2015%3A33&is_transit=false&car=%D0%9A%D1%83%D0%BF%D0%B5&carId=16710937&fullPath=%2Frailways%2Fsearch%3Fstation_from%3D2708001%26station_to%3D2700000%26departure_date%3D28.05.2021",
                                               callback_data='VIP')
        key_second = types.InlineKeyboardButton(text='Плацкарт',
                                                    url="https://aviata.kz/railways/place?from=2708001&to=2700000&number=004%D0%A6&date=2021-05-28%2015%3A33&is_transit=false&car=%D0%A1%D0%B8%D0%B4%D1%8F%D1%87%D0%B8%D0%B9&carId=16710936&fullPath=%2Frailways%2Fsearch%3Fstation_from%3D2708001%26station_to%3D2700000%26departure_date%3D28.05.2021",
                                                callback_data='stan')
        key_third = types.InlineKeyboardButton(text='Завершить покупку', callback_data='end')
        key3.row(key_first)
        key3.row(key_second)
        key3.add(key_third)
        bot.send_message(call.from_user.id, 'Выберите тип билета:', reply_markup=key3)

    elif call.data == 'a29':
        bot.send_message(call.message.chat.id, "Отличный выбор!")
        key3 = types.InlineKeyboardMarkup()
        key_first = types.InlineKeyboardButton(text='Купе',
                                               url="https://aviata.kz/railways/place?from=2708001&to=2700000&number=004%D0%A6&date=2021-05-29%2015%3A33&is_transit=false&car=%D0%9A%D1%83%D0%BF%D0%B5&carId=16737943&fullPath=%2Frailways%2Fsearch%3Fstation_from%3D2708001%26station_to%3D2700000%26departure_date%3D29.05.2021",
                                               callback_data='VIP')
        key_second = types.InlineKeyboardButton(text='Плацкарт',
                                                    url="https://aviata.kz/railways/place?from=2708001&to=2700000&number=004%D0%A6&date=2021-05-29%2015%3A33&is_transit=false&car=%D0%A1%D0%B8%D0%B4%D1%8F%D1%87%D0%B8%D0%B9&carId=16737942&fullPath=%2Frailways%2Fsearch%3Fstation_from%3D2708001%26station_to%3D2700000%26departure_date%3D29.05.2021",
                                                callback_data='stan')
        key_third = types.InlineKeyboardButton(text='Завершить покупку', callback_data='end')
        key3.row(key_first)
        key3.row(key_second)
        key3.add(key_third)
        bot.send_message(call.from_user.id, 'Выберите тип билета:', reply_markup=key3)

    elif call.data == 'a30':
        bot.send_message(call.message.chat.id, "Отличный выбор!")
        key3 = types.InlineKeyboardMarkup()
        key_first = types.InlineKeyboardButton(text='Купе',
                                               url="https://aviata.kz/railways/place?from=2708001&to=2700000&number=004%D0%A6&date=2021-05-30%2015%3A33&is_transit=false&car=%D0%9A%D1%83%D0%BF%D0%B5&carId=16770654&fullPath=%2Frailways%2Fsearch%3Fstation_from%3D2708001%26station_to%3D2700000%26departure_date%3D30.05.2021",
                                               callback_data='VIP')
        key_second = types.InlineKeyboardButton(text='Плацкарт',
                                                    url="https://aviata.kz/railways/place?from=2708001&to=2700000&number=004%D0%A6&date=2021-05-29%2015%3A33&is_transit=false&car=%D0%A1%D0%B8%D0%B4%D1%8F%D1%87%D0%B8%D0%B9&carId=16737942&fullPath=%2Frailways%2Fsearch%3Fstation_from%3D2708001%26station_to%3D2700000%26departure_date%3D29.05.2021",
                                                callback_data='stan')
        key_third = types.InlineKeyboardButton(text='Завершить покупку', callback_data='end')
        key3.row(key_first)
        key3.row(key_second)
        key3.add(key_third)
        bot.send_message(call.from_user.id, 'Выберите тип билета:', reply_markup=key3)

    elif call.data == 'end':
        key68 = types.InlineKeyboardMarkup()
        key_first = types.InlineKeyboardButton(text="О компании", url="https://aviata.kz/about", callback_data='yees')
        key_second = types.InlineKeyboardButton(text='Отмена ❌', callback_data='no')
        key68.row(key_first)
        key68.row(key_second)
        bot.edit_message_text(
            "Данные сайта: https://aviata.kz/railways "
            "Cпасибо, что пользуетесь нашим сервисом!😊",
            call.message.chat.id, call.message.message_id, reply_markup=key68)
    elif call.data == 'yees':
        bot.send_message(call.message.chat.id, "Спасибо за выбор!☺")
        bot.send_message(call.message.chat.id, "Если хотите еще раз посмотреть список поездов, напишите /start")
    elif call.data == 'nope':
        bot.send_message(call.message.chat.id, "Спасибо! Хорошего дня!🌟")


@bot.message_handler(content_types=['text', 'document', 'audio'])
def send_welcome(message):
    if city == "Алматы" and city2 == "Нурсултан" and date == "4":
        bot.send_message(message.from_user.id, """\r
      Поезд № 043Ц , Алматы 2 → Нур-Султан-Нурлы Жол
Отправление
Алматы
04.05.2021, 14:35
Прибытие
Нур-Султан
05.05.2021, 05:35
Вагон Плацкартный
Общее время в пути - 22 ч. 53 мин.
Билеты от 5 087 ₸

       
       
       """, parse_mode="Markdown")

        key = types.InlineKeyboardMarkup()
        key_first = types.InlineKeyboardButton("Да", callback_data='first')
        key_second = types.InlineKeyboardButton("Нет", callback_data='second')
        key_third = types.InlineKeyboardButton("Другие поезда ",url="https://aviata.kz/railways/search?station_from=2700000&station_to=2708001&departure_date=04.05.2021", callback_data='third')
        key.row(key_first)
        key.row(key_second)
        key.row(key_third)

        bot.send_message(message.chat.id, 'Желаете выбрать данный поезд?:', reply_markup=key)

    elif city == "Алматы" and city2 == "Нурсултан" and date == "5":
        bot.send_message(message.from_user.id, """\r
        Поезд № 003Ц , Алматы 2 → Нур-Султан-Нурлы Жол
Отправление
Алматы
05.05.2021, 14:35
Прибытие
Нур-Султан
06.05.2021, 05:35
Вагон Плацкартный
Общее время в пути - 15 ч. 00 мин.
Билеты от 6313 ₸


        """, parse_mode="Markdown")
        key = types.InlineKeyboardMarkup()
        key_first2 = types.InlineKeyboardButton("Да", callback_data='first2')
        key_second = types.InlineKeyboardButton("Нет", callback_data='second')
        key_third = types.InlineKeyboardButton("Другие поезда ",
                                               url="https://aviata.kz/railways/search?station_from=2700000&station_to=2708001&departure_date=05.05.2021",
                                               callback_data='third')
        key.row(key_first2)
        key.row(key_second)
        key.row(key_third)
        bot.send_message(message.chat.id, 'Желаете выбрать данный поезд?', reply_markup=key)

    elif city == "Алматы" and city2 == "Нурсултан" and date == "6":
        bot.send_message(message.from_user.id, """\r
        Поезд № 003Ц , Алматы 2 → Нур-Султан-Нурлы Жол
Отправление
Алматы
06.05.2021, 14:35
Прибытие
Нур-Султан
07.05.2021, 05:35
Вагон Плацкартный
Общее время в пути - 15 ч. 00 мин.
Билеты от 6313 ₸


        """, parse_mode="Markdown")
        key = types.InlineKeyboardMarkup()
        key_first3 = types.InlineKeyboardButton("Да", callback_data='first3')
        key_second = types.InlineKeyboardButton("Нет", callback_data='second')
        key_third = types.InlineKeyboardButton("Другие поезда ",
                                               url="https://aviata.kz/railways/search?station_from=2700000&station_to=2708001&departure_date=06.05.2021",
                                               callback_data='third')
        key.row(key_first3)
        key.row(key_second)
        key.row(key_third)
        bot.send_message(message.chat.id, 'Желаете выбрать данный поезд?', reply_markup=key)

    elif city == "Алматы" and city2 == "Нурсултан" and date == "7":
        bot.send_message(message.from_user.id, """\r
                Поезд № 003Ц , Алматы 2 → Нур-Султан-Нурлы Жол
Отправление
Алматы
07.05.2021, 14:35
Прибытие
Нур-Султан
08.05.2021, 05:35
Вагон Плацкартный
Общее время в пути - 15 ч. 00 мин.
Билеты от 6313 ₸


                """, parse_mode="Markdown")
        key = types.InlineKeyboardMarkup()
        key_first4 = types.InlineKeyboardButton("Да", callback_data='first4')
        key_second = types.InlineKeyboardButton("Нет", callback_data='second')
        key_third = types.InlineKeyboardButton("Другие поезда ",
                                               url="https://aviata.kz/railways/search?station_from=2700000&station_to=2708001&departure_date=07.05.2021",
                                               callback_data='third')
        key.row(key_first4)
        key.row(key_second)
        key.row(key_third)
        bot.send_message(message.chat.id, 'Желаете выбрать данный поезд?', reply_markup=key)

    elif city == "Алматы" and city2 == "Нурсултан" and date == "8":
        bot.send_message(message.from_user.id, """\r
                    Поезд № 003Ц , Алматы 2 → Нур-Султан-Нурлы Жол
Отправление
Алматы
08.05.2021, 14:35
Прибытие
Нур-Султан
09.05.2021, 05:35
Вагон Плацкартный
Общее время в пути - 15 ч. 00 мин.
Билеты от 6313 ₸


                    """, parse_mode="Markdown")
        key = types.InlineKeyboardMarkup()
        key_first5 = types.InlineKeyboardButton("Да", callback_data='first5')
        key_second = types.InlineKeyboardButton("Нет", callback_data='second')
        key_third = types.InlineKeyboardButton("Другие поезда ",
                                               url="https://aviata.kz/railways/search?station_from=2700000&station_to=2708001&departure_date=08.05.2021",
                                               callback_data='third')
        key.row(key_first5)
        key.row(key_second)
        key.row(key_third)
        bot.send_message(message.chat.id, 'Желаете выбрать данный поезд?', reply_markup=key)

    elif city == "Алматы" and city2 == "Нурсултан" and date == "9":
        bot.send_message(message.from_user.id, """\r
                        Поезд № 003Ц , Алматы 2 → Нур-Султан-Нурлы Жол
Отправление
Алматы
09.05.2021, 14:35
Прибытие
Нур-Султан
10.05.2021, 05:35
Вагон Плацкартный
Общее время в пути - 15 ч. 00 мин.
Билеты от 6313 ₸


                        """, parse_mode="Markdown")
        key = types.InlineKeyboardMarkup()
        key_first6 = types.InlineKeyboardButton("Да", callback_data='first6')
        key_second = types.InlineKeyboardButton("Нет", callback_data='second')
        key_third = types.InlineKeyboardButton("Другие поезда ",
                                               url="https://aviata.kz/railways/search?station_from=2700000&station_to=2708001&departure_date=09.05.2021",
                                               callback_data='third')
        key.row(key_first6)
        key.row(key_second)
        key.row(key_third)
        bot.send_message(message.chat.id, 'Желаете выбрать данный поезд?', reply_markup=key)

    elif city == "Алматы" and city2 == "Нурсултан" and date == "10":
        bot.send_message(message.from_user.id, """\r
                                Поезд № 003Ц , Алматы 2 → Нур-Султан-Нурлы Жол
Отправление
Алматы
10.05.2021, 14:35
Прибытие
Нур-Султан
11.05.2021, 05:35
Вагон Плацкартный
Общее время в пути - 15 ч. 00 мин.
Билеты от 6313 ₸


                                """, parse_mode="Markdown")
        key = types.InlineKeyboardMarkup()
        key_first6 = types.InlineKeyboardButton("Да", callback_data='first7')
        key_second = types.InlineKeyboardButton("Нет", callback_data='second')
        key_third = types.InlineKeyboardButton("Другие поезда ",
                                               url="https://aviata.kz/railways/search?station_from=2700000&station_to=2708001&departure_date=10.05.2021",
                                               callback_data='third')
        key.row(key_first6)
        key.row(key_second)
        key.row(key_third)
        bot.send_message(message.chat.id, 'Желаете выбрать данный поезд?', reply_markup=key)

    elif city == "Алматы" and city2 == "Нурсултан" and date == "11":
        bot.send_message(message.from_user.id, """\r
                                Поезд № 003Ц , Алматы 2 → Нур-Султан-Нурлы Жол
Отправление
Алматы
11.05.2021, 14:35
Прибытие
Нур-Султан
12.05.2021, 05:35
Вагон Плацкартный
Общее время в пути - 15 ч. 00 мин.
Билеты от 6313 ₸


                                """, parse_mode="Markdown")
        key = types.InlineKeyboardMarkup()
        key_first6 = types.InlineKeyboardButton("Да", callback_data='first8')
        key_second = types.InlineKeyboardButton("Нет", callback_data='second')
        key_third = types.InlineKeyboardButton("Другие поезда ",
                                               url="https://aviata.kz/railways/search?station_from=2700000&station_to=2708001&departure_date=11.05.2021",
                                               callback_data='third')
        key.row(key_first6)
        key.row(key_second)
        key.row(key_third)
        bot.send_message(message.chat.id, 'Желаете выбрать данный поезд?', reply_markup=key)

    elif city == "Алматы" and city2 == "Нурсултан" and date == "12":
        bot.send_message(message.from_user.id, """\r
                                Поезд № 003Ц , Алматы 2 → Нур-Султан-Нурлы Жол
Отправление
Алматы
12.05.2021, 14:35
Прибытие
Нур-Султан
13.05.2021, 05:35
Вагон Плацкартный
Общее время в пути - 15 ч. 00 мин.
Билеты от 6313 ₸


                                """, parse_mode="Markdown")
        key = types.InlineKeyboardMarkup()
        key_first6 = types.InlineKeyboardButton("Да", callback_data='first9')
        key_second = types.InlineKeyboardButton("Нет", callback_data='second')
        key_third = types.InlineKeyboardButton("Другие поезда ",
                                               url="https://aviata.kz/railways/search?station_from=2700000&station_to=2708001&departure_date=12.05.2021",
                                               callback_data='third')
        key.row(key_first6)
        key.row(key_second)
        key.row(key_third)
        bot.send_message(message.chat.id, 'Желаете выбрать данный поезд?', reply_markup=key)

    elif city == "Алматы" and city2 == "Нурсултан" and date == "13":
        bot.send_message(message.from_user.id, """\r
                                Поезд № 003Ц , Алматы 2 → Нур-Султан-Нурлы Жол
Отправление
Алматы
13.05.2021, 14:35
Прибытие
Нур-Султан
14.05.2021, 05:35
Вагон Плацкартный
Общее время в пути - 15 ч. 00 мин.
Билеты от 6313 ₸


                                """, parse_mode="Markdown")
        key = types.InlineKeyboardMarkup()
        key_first6 = types.InlineKeyboardButton("Да", callback_data='first10')
        key_second = types.InlineKeyboardButton("Нет", callback_data='second')
        key_third = types.InlineKeyboardButton("Другие поезда ",
                                               url="https://aviata.kz/railways/search?station_from=2700000&station_to=2708001&departure_date=13.05.2021",
                                               callback_data='third')
        key.row(key_first6)
        key.row(key_second)
        key.row(key_third)
        bot.send_message(message.chat.id, 'Желаете выбрать данный поезд?', reply_markup=key)

    elif city == "Алматы" and city2 == "Нурсултан" and date == "14":
        bot.send_message(message.from_user.id, """\r
                                Поезд № 003Ц , Алматы 2 → Нур-Султан-Нурлы Жол
Отправление
Алматы
14.05.2021, 14:35
Прибытие
Нур-Султан
15.05.2021, 05:35
Вагон Плацкартный
Общее время в пути - 15 ч. 00 мин.
Билеты от 6313 ₸


                                """, parse_mode="Markdown")
        key = types.InlineKeyboardMarkup()
        key_first6 = types.InlineKeyboardButton("Да", callback_data='first14')
        key_second = types.InlineKeyboardButton("Нет", callback_data='second')
        key_third = types.InlineKeyboardButton("Другие поезда ",
                                               url="https://aviata.kz/railways/search?station_from=2700000&station_to=2708001&departure_date=14.05.2021",
                                               callback_data='third')
        key.row(key_first6)
        key.row(key_second)
        key.row(key_third)
        bot.send_message(message.chat.id, 'Желаете выбрать данный поезд?', reply_markup=key)

    elif city == "Алматы" and city2 == "Нурсултан" and date == "15":
        bot.send_message(message.from_user.id, """\r
                                    Поезд № 003Ц , Алматы 2 → Нур-Султан-Нурлы Жол
Отправление
Алматы
15.05.2021, 14:35
Прибытие
Нур-Султан
16.05.2021, 05:35
Вагон Плацкартный
Общее время в пути - 15 ч. 00 мин.
Билеты от 6313 ₸


                                    """, parse_mode="Markdown")
        key = types.InlineKeyboardMarkup()
        key_first6 = types.InlineKeyboardButton("Да", callback_data='first15')
        key_second = types.InlineKeyboardButton("Нет", callback_data='second')
        key_third = types.InlineKeyboardButton("Другие поезда ",
                                               url="https://aviata.kz/railways/search?station_from=2700000&station_to=2708001&departure_date=15.05.2021",
                                               callback_data='third')
        key.row(key_first6)
        key.row(key_second)
        key.row(key_third)
        bot.send_message(message.chat.id, 'Желаете выбрать данный поезд?', reply_markup=key)

    elif city == "Алматы" and city2 == "Нурсултан" and date == "16":
        bot.send_message(message.from_user.id, """\r
                                        Поезд № 003Ц , Алматы 2 → Нур-Султан-Нурлы Жол
Отправление
Алматы
16.05.2021, 14:35
Прибытие
Нур-Султан
17.05.2021, 05:35
Вагон Плацкартный
Общее время в пути - 15 ч. 00 мин.
Билеты от 6313 ₸


                                        """, parse_mode="Markdown")
        key = types.InlineKeyboardMarkup()
        key_first6 = types.InlineKeyboardButton("Да", callback_data='first16')
        key_second = types.InlineKeyboardButton("Нет", callback_data='second')
        key_third = types.InlineKeyboardButton("Другие поезда ",
                                               url="https://aviata.kz/railways/search?station_from=2700000&station_to=2708001&departure_date=16.05.2021",
                                               callback_data='third')
        key.row(key_first6)
        key.row(key_second)
        key.row(key_third)
        bot.send_message(message.chat.id, 'Желаете выбрать данный поезд?', reply_markup=key)

    elif city == "Алматы" and city2 == "Нурсултан" and date == "17":
        bot.send_message(message.from_user.id, """\r
                                            Поезд № 003Ц , Алматы 2 → Нур-Султан-Нурлы Жол
Отправление
Алматы
17.05.2021, 14:35
Прибытие
Нур-Султан
18.05.2021, 05:35
Вагон Плацкартный
Общее время в пути - 15 ч. 00 мин.
Билеты от 6313 ₸


                                            """, parse_mode="Markdown")
        key = types.InlineKeyboardMarkup()
        key_first6 = types.InlineKeyboardButton("Да", callback_data='first17')
        key_second = types.InlineKeyboardButton("Нет", callback_data='second')
        key_third = types.InlineKeyboardButton("Другие поезда ",
                                               url="https://aviata.kz/railways/search?station_from=2700000&station_to=2708001&departure_date=17.05.2021",
                                               callback_data='third')
        key.row(key_first6)
        key.row(key_second)
        key.row(key_third)
        bot.send_message(message.chat.id, 'Желаете выбрать данный поезд?', reply_markup=key)

    elif city == "Алматы" and city2 == "Нурсултан" and date == "18":
        bot.send_message(message.from_user.id, """\r
                                                    Поезд № 003Ц , Алматы 2 → Нур-Султан-Нурлы Жол
Отправление
Алматы
18.05.2021, 14:35
Прибытие
Нур-Султан
19.05.2021, 05:35
Вагон Плацкартный
Общее время в пути - 15 ч. 00 мин.
Билеты от 6313 ₸


                                                    """, parse_mode="Markdown")
        key = types.InlineKeyboardMarkup()
        key_first6 = types.InlineKeyboardButton("Да", callback_data='first18')
        key_second = types.InlineKeyboardButton("Нет", callback_data='second')
        key_third = types.InlineKeyboardButton("Другие поезда ",
                                               url="https://aviata.kz/railways/search?station_from=2700000&station_to=2708001&departure_date=18.05.2021",
                                               callback_data='third')
        key.row(key_first6)
        key.row(key_second)
        key.row(key_third)
        bot.send_message(message.chat.id, 'Желаете выбрать данный поезд?', reply_markup=key)

    elif city == "Алматы" and city2 == "Нурсултан" and date == "19":
        bot.send_message(message.from_user.id, """\r
                                                            Поезд № 003Ц , Алматы 2 → Нур-Султан-Нурлы Жол
Отправление
Алматы
19.05.2021, 14:35
Прибытие
Нур-Султан
20.05.2021, 05:35
Вагон Плацкартный
Общее время в пути - 15 ч. 00 мин.
Билеты от 6313 ₸


                                                            """, parse_mode="Markdown")
        key = types.InlineKeyboardMarkup()
        key_first6 = types.InlineKeyboardButton("Да", callback_data='first19')
        key_second = types.InlineKeyboardButton("Нет", callback_data='second')
        key_third = types.InlineKeyboardButton("Другие поезда ",
                                               url="https://aviata.kz/railways/search?station_from=2700000&station_to=2708001&departure_date=19.05.2021",
                                               callback_data='third')
        key.row(key_first6)
        key.row(key_second)
        key.row(key_third)
        bot.send_message(message.chat.id, 'Желаете выбрать данный поезд?', reply_markup=key)

    elif city == "Алматы" and city2 == "Нурсултан" and date == "20":
        bot.send_message(message.from_user.id, """\r
                                                                    Поезд № 003Ц , Алматы 2 → Нур-Султан-Нурлы Жол
Отправление
Алматы
20.05.2021, 14:35
Прибытие
Нур-Султан
21.05.2021, 05:35
Вагон Плацкартный
Общее время в пути - 15 ч. 00 мин.
Билеты от 6313 ₸


                                                                    """, parse_mode="Markdown")
        key = types.InlineKeyboardMarkup()
        key_first6 = types.InlineKeyboardButton("Да", callback_data='first20')
        key_second = types.InlineKeyboardButton("Нет", callback_data='second')
        key_third = types.InlineKeyboardButton("Другие поезда ",
                                               url="https://aviata.kz/railways/search?station_from=2700000&station_to=2708001&departure_date=20.05.2021",
                                               callback_data='third')
        key.row(key_first6)
        key.row(key_second)
        key.row(key_third)
        bot.send_message(message.chat.id, 'Желаете выбрать данный поезд?', reply_markup=key)

    elif city == "Алматы" and city2 == "Нурсултан" and date == "21":
        bot.send_message(message.from_user.id, """\r
                                                                        Поезд № 003Ц , Алматы 2 → Нур-Султан-Нурлы Жол
Отправление
Алматы
21.05.2021, 14:35
Прибытие
Нур-Султан
22.05.2021, 05:35
Вагон Плацкартный
Общее время в пути - 15 ч. 00 мин.
Билеты от 6313 ₸


                                                                        """, parse_mode="Markdown")
        key = types.InlineKeyboardMarkup()
        key_first6 = types.InlineKeyboardButton("Да", callback_data='first21')
        key_second = types.InlineKeyboardButton("Нет", callback_data='second')
        key_third = types.InlineKeyboardButton("Другие поезда ",
                                               url="https://aviata.kz/railways/search?station_from=2700000&station_to=2708001&departure_date=21.05.2021",
                                               callback_data='third')
        key.row(key_first6)
        key.row(key_second)
        key.row(key_third)
        bot.send_message(message.chat.id, 'Желаете выбрать данный поезд?', reply_markup=key)

    elif city == "Алматы" and city2 == "Нурсултан" and date == "22":
        bot.send_message(message.from_user.id, """\r
                                                                                Поезд № 003Ц , Алматы 2 → Нур-Султан-Нурлы Жол
Отправление
Алматы
21.05.2021, 14:35
Прибытие
Нур-Султан
22.05.2021, 05:35
Вагон Плацкартный
Общее время в пути - 15 ч. 00 мин.
Билеты от 6313 ₸


                                                                                """, parse_mode="Markdown")
        key = types.InlineKeyboardMarkup()
        key_first6 = types.InlineKeyboardButton("Да", callback_data='first22')
        key_second = types.InlineKeyboardButton("Нет", callback_data='second')
        key_third = types.InlineKeyboardButton("Другие поезда ",
                                               url="https://aviata.kz/railways/search?station_from=2700000&station_to=2708001&departure_date=22.05.2021",
                                               callback_data='third')
        key.row(key_first6)
        key.row(key_second)
        key.row(key_third)
        bot.send_message(message.chat.id, 'Желаете выбрать данный поезд?', reply_markup=key)

    elif city == "Алматы" and city2 == "Нурсултан" and date == "23":
        bot.send_message(message.from_user.id, """\r
                                                                                Поезд № 003Ц , Алматы 2 → Нур-Султан-Нурлы Жол
Отправление
Алматы
23.05.2021, 14:35
Прибытие
Нур-Султан
24.05.2021, 05:35
Вагон Плацкартный
Общее время в пути - 15 ч. 00 мин.
Билеты от 6313 ₸


                                                                                """, parse_mode="Markdown")
        key = types.InlineKeyboardMarkup()
        key_first6 = types.InlineKeyboardButton("Да", callback_data='first23')
        key_second = types.InlineKeyboardButton("Нет", callback_data='second')
        key_third = types.InlineKeyboardButton("Другие поезда ",
                                               url="https://aviata.kz/railways/search?station_from=2700000&station_to=2708001&departure_date=23.05.2021",
                                               callback_data='third')
        key.row(key_first6)
        key.row(key_second)
        key.row(key_third)
        bot.send_message(message.chat.id, 'Желаете выбрать данный поезд?', reply_markup=key)

    elif city == "Алматы" and city2 == "Нурсултан" and date == "24":
        bot.send_message(message.from_user.id, """\r
                                                                                Поезд № 003Ц , Алматы 2 → Нур-Султан-Нурлы Жол
Отправление
Алматы
24.05.2021, 14:35
Прибытие
Нур-Султан
25.05.2021, 05:35
Вагон Плацкартный
Общее время в пути - 15 ч. 00 мин.
Билеты от 6313 ₸


                                                                                """, parse_mode="Markdown")
        key = types.InlineKeyboardMarkup()
        key_first6 = types.InlineKeyboardButton("Да", callback_data='first24')
        key_second = types.InlineKeyboardButton("Нет", callback_data='second')
        key_third = types.InlineKeyboardButton("Другие поезда ",
                                               url="https://aviata.kz/railways/search?station_from=2700000&station_to=2708001&departure_date=24.05.2021",
                                               callback_data='third')
        key.row(key_first6)
        key.row(key_second)
        key.row(key_third)
        bot.send_message(message.chat.id, 'Желаете выбрать данный поезд?', reply_markup=key)

    elif city == "Алматы" and city2 == "Нурсултан" and date == "25":
        bot.send_message(message.from_user.id, """\r
                                                                                Поезд № 003Ц , Алматы 2 → Нур-Султан-Нурлы Жол
Отправление
Алматы
25.05.2021, 14:35
Прибытие
Нур-Султан
26.05.2021, 05:35
Вагон Плацкартный
Общее время в пути - 15 ч. 00 мин.
Билеты от 6313 ₸


                                                                                """, parse_mode="Markdown")
        key = types.InlineKeyboardMarkup()
        key_first6 = types.InlineKeyboardButton("Да", callback_data='first25')
        key_second = types.InlineKeyboardButton("Нет", callback_data='second')
        key_third = types.InlineKeyboardButton("Другие поезда ",
                                               url="https://aviata.kz/railways/search?station_from=2700000&station_to=2708001&departure_date=25.05.2021",
                                               callback_data='third')
        key.row(key_first6)
        key.row(key_second)
        key.row(key_third)
        bot.send_message(message.chat.id, 'Желаете выбрать данный поезд?', reply_markup=key)

    elif city == "Алматы" and city2 == "Нурсултан" and date == "26":
        bot.send_message(message.from_user.id, """\r
                                                                                Поезд № 003Ц , Алматы 2 → Нур-Султан-Нурлы Жол
Отправление
Алматы
26.05.2021, 14:35
Прибытие
Нур-Султан
27.05.2021, 05:35
Вагон Плацкартный
Общее время в пути - 15 ч. 00 мин.
Билеты от 6313 ₸


                                                                                """, parse_mode="Markdown")
        key = types.InlineKeyboardMarkup()
        key_first6 = types.InlineKeyboardButton("Да", callback_data='first26')
        key_second = types.InlineKeyboardButton("Нет", callback_data='second')
        key_third = types.InlineKeyboardButton("Другие поезда ",
                                               url="https://aviata.kz/railways/search?station_from=2700000&station_to=2708001&departure_date=26.05.2021",
                                               callback_data='third')
        key.row(key_first6)
        key.row(key_second)
        key.row(key_third)
        bot.send_message(message.chat.id, 'Желаете выбрать данный поезд?', reply_markup=key)

    elif city == "Алматы" and city2 == "Нурсултан" and date == "27":
        bot.send_message(message.from_user.id, """\r
                                                                                        Поезд № 003Ц , Алматы 2 → Нур-Султан-Нурлы Жол
Отправление
Алматы
27.05.2021, 14:35
Прибытие
Нур-Султан
28.05.2021, 05:35
Вагон Плацкартный
Общее время в пути - 15 ч. 00 мин.
Билеты от 6313 ₸


                                                                                        """, parse_mode="Markdown")
        key = types.InlineKeyboardMarkup()
        key_first6 = types.InlineKeyboardButton("Да", callback_data='first27')
        key_second = types.InlineKeyboardButton("Нет", callback_data='second')
        key_third = types.InlineKeyboardButton("Другие поезда ",
                                               url="https://aviata.kz/railways/search?station_from=2700000&station_to=2708001&departure_date=27.05.2021",
                                               callback_data='third')
        key.row(key_first6)
        key.row(key_second)
        key.row(key_third)
        bot.send_message(message.chat.id, 'Желаете выбрать данный поезд?', reply_markup=key)

    elif city == "Алматы" and city2 == "Нурсултан" and date == "28":
        bot.send_message(message.from_user.id, """\r
                                                                                        Поезд № 003Ц , Алматы 2 → Нур-Султан-Нурлы Жол
Отправление
Алматы
28.05.2021, 14:35
Прибытие
Нур-Султан
28.05.2021, 05:35
Вагон Плацкартный
Общее время в пути - 15 ч. 00 мин.
Билеты от 6313 ₸


                                                                                        """, parse_mode="Markdown")
        key = types.InlineKeyboardMarkup()
        key_first6 = types.InlineKeyboardButton("Да", callback_data='first28')
        key_second = types.InlineKeyboardButton("Нет", callback_data='second')
        key_third = types.InlineKeyboardButton("Другие поезда ",
                                               url="https://aviata.kz/railways/search?station_from=2700000&station_to=2708001&departure_date=28.05.2021",
                                               callback_data='third')
        key.row(key_first6)
        key.row(key_second)
        key.row(key_third)
        bot.send_message(message.chat.id, 'Желаете выбрать данный поезд?', reply_markup=key)

    elif city == "Алматы" and city2 == "Нурсултан" and date == "29":
        bot.send_message(message.from_user.id, """\r
                                                                                                Поезд № 003Ц , Алматы 2 → Нур-Султан-Нурлы Жол
Отправление
Алматы
29.05.2021, 14:35
Прибытие
Нур-Султан
29.05.2021, 05:35
Вагон Плацкартный
Общее время в пути - 15 ч. 00 мин.
Билеты от 6313 ₸


                                                                                                """,
                         parse_mode="Markdown")
        key = types.InlineKeyboardMarkup()
        key_first6 = types.InlineKeyboardButton("Да", callback_data='first29')
        key_second = types.InlineKeyboardButton("Нет", callback_data='second')
        key_third = types.InlineKeyboardButton("Другие поезда ",
                                               url="https://aviata.kz/railways/search?station_from=2700000&station_to=2708001&departure_date=29.05.2021",
                                               callback_data='third')
        key.row(key_first6)
        key.row(key_second)
        key.row(key_third)
        bot.send_message(message.chat.id, 'Желаете выбрать данный поезд?', reply_markup=key)

    elif city == "Алматы" and city2 == "Нурсултан" and date == "30":
        bot.send_message(message.from_user.id, """\r
                                                                                                Поезд № 003Ц , Алматы 2 → Нур-Султан-Нурлы Жол
        Отправление
        Алматы
        30.05.2021, 14:35
        Прибытие
        Нур-Султан
        1.06.2021, 05:35
        Вагон Плацкартный
        Общее время в пути - 15 ч. 00 мин.
        Билеты от 6313 ₸


                                                                                                """,
                         parse_mode="Markdown")
        key = types.InlineKeyboardMarkup()
        key_first6 = types.InlineKeyboardButton("Да", callback_data='first30')
        key_second = types.InlineKeyboardButton("Нет", callback_data='second')
        key_third = types.InlineKeyboardButton("Другие поезда ",
                                               url="https://aviata.kz/railways/search?station_from=2700000&station_to=2708001&departure_date=30.05.2021",
                                               callback_data='third')
        key.row(key_first6)
        key.row(key_second)
        key.row(key_third)
        bot.send_message(message.chat.id, 'Желаете выбрать данный поезд?', reply_markup=key)

    elif city == "Нурсултан" and city2 == "Алматы" and date == "4":
        bot.send_message(message.from_user.id, """\r
                                                                                                Поезд № 004Ц ,Нур-Султан-Нурлы Жол →  Алматы 2
Отправление
Нурсултан
04.05.2021, 15:33
Прибытие
Алматы
05.05.2021, 06:43
Вагон Плацкартный
Общее время в пути - 15 ч. 10 мин.
Билеты от 6313 ₸


                                                                                                """,
                         parse_mode="Markdown")
        key = types.InlineKeyboardMarkup()
        key_first6 = types.InlineKeyboardButton("Да", callback_data='a4')
        key_second = types.InlineKeyboardButton("Нет", callback_data='second')
        key_third = types.InlineKeyboardButton("Другие поезда ",
                                               url="https://aviata.kz/railways/search?station_from=2708001&station_to=2700000&departure_date=04.05.2021",
                                               callback_data='third')
        key.row(key_first6)
        key.row(key_second)
        key.row(key_third)
        bot.send_message(message.chat.id, 'Желаете выбрать данный поезд?', reply_markup=key)

    elif city == "Нурсултан" and city2 == "Алматы" and date == "5":
        bot.send_message(message.from_user.id, """\r
                                                                                                      Поезд № 004Ц ,Нур-Султан-Нурлы Жол →  Алматы 2
Отправление
Нурсултан
05.05.2021, 15:33
Прибытие
Алматы
06.05.2021, 06:43
Вагон Плацкартный
Общее время в пути - 15 ч. 10 мин.
Билеты от 6313 ₸


                                                                                                      """,
                         parse_mode="Markdown")
        key = types.InlineKeyboardMarkup()
        key_first6 = types.InlineKeyboardButton("Да", callback_data='a5')
        key_second = types.InlineKeyboardButton("Нет", callback_data='second')
        key_third = types.InlineKeyboardButton("Другие поезда ",
                                               url="https://aviata.kz/railways/search?station_from=2708001&station_to=2700000&departure_date=05.05.2021",
                                               callback_data='third')
        key.row(key_first6)
        key.row(key_second)
        key.row(key_third)
        bot.send_message(message.chat.id, 'Желаете выбрать данный поезд?', reply_markup=key)

    elif city == "Нурсултан" and city2 == "Алматы" and date == "6":
        bot.send_message(message.from_user.id, """\r
                                                                                                         Поезд № 004Ц ,Нур-Султан-Нурлы Жол →  Алматы 2
Отправление
Нурсултан
06.05.2021, 15:33
Прибытие
Алматы
07.05.2021, 06:43
Вагон Плацкартный
Общее время в пути - 15 ч. 10 мин.
Билеты от 6313 ₸


                                                                                                         """,
                         parse_mode="Markdown")
        key = types.InlineKeyboardMarkup()
        key_first6 = types.InlineKeyboardButton("Да", callback_data='a6')
        key_second = types.InlineKeyboardButton("Нет", callback_data='second')
        key_third = types.InlineKeyboardButton("Другие поезда ",
                                               url="https://aviata.kz/railways/search?station_from=2708001&station_to=2700000&departure_date=06.05.2021",
                                               callback_data='third')
        key.row(key_first6)
        key.row(key_second)
        key.row(key_third)
        bot.send_message(message.chat.id, 'Желаете выбрать данный поезд?', reply_markup=key)

    elif city == "Нурсултан" and city2 == "Алматы" and date == "7":
        bot.send_message(message.from_user.id, """\r
                                                                                                             Поезд № 004Ц ,Нур-Султан-Нурлы Жол →  Алматы 2
Отправление
Нурсултан
07.05.2021, 15:33
Прибытие
Алматы
08.05.2021, 06:43
Вагон Плацкартный
Общее время в пути - 15 ч. 10 мин.
Билеты от 6313 ₸


                                                                                                             """,
                         parse_mode="Markdown")
        key = types.InlineKeyboardMarkup()
        key_first6 = types.InlineKeyboardButton("Да", callback_data='a7')
        key_second = types.InlineKeyboardButton("Нет", callback_data='second')
        key_third = types.InlineKeyboardButton("Другие поезда ",
                                               url="https://aviata.kz/railways/search?station_from=2708001&station_to=2700000&departure_date=07.05.2021",
                                               callback_data='third')
        key.row(key_first6)
        key.row(key_second)
        key.row(key_third)
        bot.send_message(message.chat.id, 'Желаете выбрать данный поезд?', reply_markup=key)

    elif city == "Нурсултан" and city2 == "Алматы" and date == "8":
        bot.send_message(message.from_user.id, """\r
                                                                                                                 Поезд № 004Ц ,Нур-Султан-Нурлы Жол →  Алматы 2
Отправление
Нурсултан
08.05.2021, 15:33
Прибытие
Алматы
09.05.2021, 06:43
Вагон Плацкартный
Общее время в пути - 15 ч. 10 мин.
Билеты от 6313 ₸


                                                                                                                 """,
                         parse_mode="Markdown")
        key = types.InlineKeyboardMarkup()
        key_first6 = types.InlineKeyboardButton("Да", callback_data='a8')
        key_second = types.InlineKeyboardButton("Нет", callback_data='second')
        key_third = types.InlineKeyboardButton("Другие поезда ",
                                               url="https://aviata.kz/railways/search?station_from=2708001&station_to=2700000&departure_date=08.05.2021",
                                               callback_data='third')
        key.row(key_first6)
        key.row(key_second)
        key.row(key_third)
        bot.send_message(message.chat.id, 'Желаете выбрать данный поезд?', reply_markup=key)

    elif city == "Нурсултан" and city2 == "Алматы" and date == "9":
        bot.send_message(message.from_user.id, """\r
                                                                                                                     Поезд № 004Ц ,Нур-Султан-Нурлы Жол →  Алматы 2
Отправление
Нурсултан
09.05.2021, 15:33
Прибытие
Алматы
10.05.2021, 06:43
Вагон Плацкартный
Общее время в пути - 15 ч. 10 мин.
Билеты от 6313 ₸


                                                                                                                     """,
                         parse_mode="Markdown")
        key = types.InlineKeyboardMarkup()
        key_first6 = types.InlineKeyboardButton("Да", callback_data='a9')
        key_second = types.InlineKeyboardButton("Нет", callback_data='second')
        key_third = types.InlineKeyboardButton("Другие поезда ",
                                               url="https://aviata.kz/railways/search?station_from=2708001&station_to=2700000&departure_date=09.05.2021",
                                               callback_data='third')
        key.row(key_first6)
        key.row(key_second)
        key.row(key_third)
        bot.send_message(message.chat.id, 'Желаете выбрать данный поезд?', reply_markup=key)

    elif city == "Нурсултан" and city2 == "Алматы" and date == "10":
        bot.send_message(message.from_user.id, """\r
                                                                                                                         Поезд № 004Ц ,Нур-Султан-Нурлы Жол →  Алматы 2
Отправление
Нурсултан
10.05.2021, 15:33
Прибытие
Алматы
11.05.2021, 06:43
Вагон Плацкартный
Общее время в пути - 15 ч. 10 мин.
Билеты от 6313 ₸


                                                                                                                         """,
                         parse_mode="Markdown")
        key = types.InlineKeyboardMarkup()
        key_first6 = types.InlineKeyboardButton("Да", callback_data='a10')
        key_second = types.InlineKeyboardButton("Нет", callback_data='second')
        key_third = types.InlineKeyboardButton("Другие поезда ",
                                               url="https://aviata.kz/railways/search?station_from=2708001&station_to=2700000&departure_date=10.05.2021",
                                               callback_data='third')
        key.row(key_first6)
        key.row(key_second)
        key.row(key_third)
        bot.send_message(message.chat.id, 'Желаете выбрать данный поезд?', reply_markup=key)

    elif city == "Нурсултан" and city2 == "Алматы" and date == "11":
        bot.send_message(message.from_user.id, """\r
                                                                                                                             Поезд № 004Ц ,Нур-Султан-Нурлы Жол →  Алматы 2
Отправление
Нурсултан
11.05.2021, 15:33
Прибытие
Алматы
12.05.2021, 06:43
Вагон Плацкартный
Общее время в пути - 15 ч. 10 мин.
Билеты от 6313 ₸


                                                                                                                             """,
                         parse_mode="Markdown")
        key = types.InlineKeyboardMarkup()
        key_first6 = types.InlineKeyboardButton("Да", callback_data='a11')
        key_second = types.InlineKeyboardButton("Нет", callback_data='second')
        key_third = types.InlineKeyboardButton("Другие поезда ",
                                               url="https://aviata.kz/railways/search?station_from=2708001&station_to=2700000&departure_date=11.05.2021",
                                               callback_data='third')
        key.row(key_first6)
        key.row(key_second)
        key.row(key_third)
        bot.send_message(message.chat.id, 'Желаете выбрать данный поезд?', reply_markup=key)

    elif city == "Нурсултан" and city2 == "Алматы" and date == "12":
        bot.send_message(message.from_user.id, """\r
                                                                                                                                     Поезд № 004Ц ,Нур-Султан-Нурлы Жол →  Алматы 2
Отправление
Нурсултан
12.05.2021, 15:33
Прибытие
Алматы
13.05.2021, 06:43
Вагон Плацкартный
Общее время в пути - 15 ч. 10 мин.
Билеты от 6313 ₸


                                                                                                                                     """,
                         parse_mode="Markdown")
        key = types.InlineKeyboardMarkup()
        key_first6 = types.InlineKeyboardButton("Да", callback_data='a12')
        key_second = types.InlineKeyboardButton("Нет", callback_data='second')
        key_third = types.InlineKeyboardButton("Другие поезда ",
                                               url="https://aviata.kz/railways/search?station_from=2708001&station_to=2700000&departure_date=12.05.2021",
                                               callback_data='third')
        key.row(key_first6)
        key.row(key_second)
        key.row(key_third)
        bot.send_message(message.chat.id, 'Желаете выбрать данный поезд?', reply_markup=key)

    elif city == "Нурсултан" and city2 == "Алматы" and date == "13":
        bot.send_message(message.from_user.id, """\r
                                                                                                                                         Поезд № 004Ц ,Нур-Султан-Нурлы Жол →  Алматы 2
Отправление
Нурсултан
13.05.2021, 15:33
Прибытие
Алматы
14.05.2021, 06:43
Вагон Плацкартный
Общее время в пути - 15 ч. 10 мин.
Билеты от 6313 ₸


                                                                                                                                         """,
                         parse_mode="Markdown")
        key = types.InlineKeyboardMarkup()
        key_first6 = types.InlineKeyboardButton("Да", callback_data='a13')
        key_second = types.InlineKeyboardButton("Нет", callback_data='second')
        key_third = types.InlineKeyboardButton("Другие поезда ",
                                               url="https://aviata.kz/railways/search?station_from=2708001&station_to=2700000&departure_date=13.05.2021",
                                               callback_data='third')
        key.row(key_first6)
        key.row(key_second)
        key.row(key_third)
        bot.send_message(message.chat.id, 'Желаете выбрать данный поезд?', reply_markup=key)

    elif city == "Нурсултан" and city2 == "Алматы" and date == "14":
        bot.send_message(message.from_user.id, """\r
                                                                                                                                              Поезд № 004Ц ,Нур-Султан-Нурлы Жол →  Алматы 2
Отправление
Нурсултан
14.05.2021, 15:33
Прибытие
Алматы
15.05.2021, 06:43
Вагон Плацкартный
Общее время в пути - 15 ч. 10 мин.
Билеты от 6313 ₸


                                                                                                                                              """,
                         parse_mode="Markdown")
        key = types.InlineKeyboardMarkup()
        key_first6 = types.InlineKeyboardButton("Да", callback_data='a14')
        key_second = types.InlineKeyboardButton("Нет", callback_data='second')
        key_third = types.InlineKeyboardButton("Другие поезда ",
                                               url="https://aviata.kz/railways/search?station_from=2708001&station_to=2700000&departure_date=14.05.2021",
                                               callback_data='third')
        key.row(key_first6)
        key.row(key_second)
        key.row(key_third)
        bot.send_message(message.chat.id, 'Желаете выбрать данный поезд?', reply_markup=key)

    elif city == "Нурсултан" and city2 == "Алматы" and date == "15":
        bot.send_message(message.from_user.id, """\r
                                                                                                                                                      Поезд № 004Ц ,Нур-Султан-Нурлы Жол →  Алматы 2
Отправление
Нурсултан
15.05.2021, 15:33
Прибытие
Алматы
16.05.2021, 06:43
Вагон Плацкартный
Общее время в пути - 15 ч. 10 мин.
Билеты от 6313 ₸


                                                                                                                                                      """,
                         parse_mode="Markdown")
        key = types.InlineKeyboardMarkup()
        key_first6 = types.InlineKeyboardButton("Да", callback_data='a15')
        key_second = types.InlineKeyboardButton("Нет", callback_data='second')
        key_third = types.InlineKeyboardButton("Другие поезда ",
                                               url="https://aviata.kz/railways/search?station_from=2708001&station_to=2700000&departure_date=15.05.2021",
                                               callback_data='third')
        key.row(key_first6)
        key.row(key_second)
        key.row(key_third)
        bot.send_message(message.chat.id, 'Желаете выбрать данный поезд?', reply_markup=key)

    elif city == "Нурсултан" and city2 == "Алматы" and date == "16":
        bot.send_message(message.from_user.id, """\r
                                                                                                                                                  Поезд № 004Ц ,Нур-Султан-Нурлы Жол →  Алматы 2
Отправление
Нурсултан
16.05.2021, 15:33
Прибытие
Алматы
17.05.2021, 06:43
Вагон Плацкартный
Общее время в пути - 15 ч. 10 мин.
Билеты от 6313 ₸


                                                                                                                                                  """,
                         parse_mode="Markdown")
        key = types.InlineKeyboardMarkup()
        key_first6 = types.InlineKeyboardButton("Да", callback_data='a16')
        key_second = types.InlineKeyboardButton("Нет", callback_data='second')
        key_third = types.InlineKeyboardButton("Другие поезда ",
                                               url="https://aviata.kz/railways/search?station_from=2708001&station_to=2700000&departure_date=16.05.2021",
                                               callback_data='third')
        key.row(key_first6)
        key.row(key_second)
        key.row(key_third)
        bot.send_message(message.chat.id, 'Желаете выбрать данный поезд?', reply_markup=key)

    elif city == "Нурсултан" and city2 == "Алматы" and date == "17":
        bot.send_message(message.from_user.id, """\r
                                                                                                                                                      Поезд № 004Ц ,Нур-Султан-Нурлы Жол →  Алматы 2
Отправление
Нурсултан
17.05.2021, 15:33
Прибытие
Алматы
18.05.2021, 06:43
Вагон Плацкартный
Общее время в пути - 15 ч. 10 мин.
Билеты от 6313 ₸


                                                                                                                                                      """,
                         parse_mode="Markdown")
        key = types.InlineKeyboardMarkup()
        key_first6 = types.InlineKeyboardButton("Да", callback_data='a17')
        key_second = types.InlineKeyboardButton("Нет", callback_data='second')
        key_third = types.InlineKeyboardButton("Другие поезда ",
                                               url="https://aviata.kz/railways/search?station_from=2708001&station_to=2700000&departure_date=17.05.2021",
                                               callback_data='third')
        key.row(key_first6)
        key.row(key_second)
        key.row(key_third)
        bot.send_message(message.chat.id, 'Желаете выбрать данный поезд?', reply_markup=key)

    elif city == "Нурсултан" and city2 == "Алматы" and date == "18":
        bot.send_message(message.from_user.id, """\r
                                                                                                                                                          Поезд № 004Ц ,Нур-Султан-Нурлы Жол →  Алматы 2
Отправление
Нурсултан
18.05.2021, 15:33
Прибытие
Алматы
19.05.2021, 06:43
Вагон Плацкартный
Общее время в пути - 15 ч. 10 мин.
Билеты от 6313 ₸


                                                                                                                                                          """,
                         parse_mode="Markdown")
        key = types.InlineKeyboardMarkup()
        key_first6 = types.InlineKeyboardButton("Да", callback_data='a18')
        key_second = types.InlineKeyboardButton("Нет", callback_data='second')
        key_third = types.InlineKeyboardButton("Другие поезда ",
                                               url="https://aviata.kz/railways/search?station_from=2708001&station_to=2700000&departure_date=18.05.2021",
                                               callback_data='third')
        key.row(key_first6)
        key.row(key_second)
        key.row(key_third)
        bot.send_message(message.chat.id, 'Желаете выбрать данный поезд?', reply_markup=key)

    elif city == "Нурсултан" and city2 == "Алматы" and date == "19":
        bot.send_message(message.from_user.id, """\r
                                                                                                                                                                  Поезд № 004Ц ,Нур-Султан-Нурлы Жол →  Алматы 2
Отправление
Нурсултан
19.05.2021, 15:33
Прибытие
Алматы
20.05.2021, 06:43
Вагон Плацкартный
Общее время в пути - 15 ч. 10 мин.
Билеты от 6313 ₸


                                                                                                                                                                  """,
                         parse_mode="Markdown")
        key = types.InlineKeyboardMarkup()
        key_first6 = types.InlineKeyboardButton("Да", callback_data='a19')
        key_second = types.InlineKeyboardButton("Нет", callback_data='second')
        key_third = types.InlineKeyboardButton("Другие поезда ",
                                               url="https://aviata.kz/railways/search?station_from=2708001&station_to=2700000&departure_date=19.05.2021",
                                               callback_data='third')
        key.row(key_first6)
        key.row(key_second)
        key.row(key_third)
        bot.send_message(message.chat.id, 'Желаете выбрать данный поезд?', reply_markup=key)

    elif city == "Нурсултан" and city2 == "Алматы" and date == "20":
        bot.send_message(message.from_user.id, """\r
                                                                                                                                                              Поезд № 004Ц ,Нур-Султан-Нурлы Жол →  Алматы 2
Отправление
Нурсултан
20.05.2021, 15:33
Прибытие
Алматы
21.05.2021, 06:43
Вагон Плацкартный
Общее время в пути - 15 ч. 10 мин.
Билеты от 6313 ₸


                                                                                                                                                              """,
                         parse_mode="Markdown")
        key = types.InlineKeyboardMarkup()
        key_first6 = types.InlineKeyboardButton("Да", callback_data='a20')
        key_second = types.InlineKeyboardButton("Нет", callback_data='second')
        key_third = types.InlineKeyboardButton("Другие поезда ",
                                               url="https://aviata.kz/railways/search?station_from=2708001&station_to=2700000&departure_date=20.05.2021",
                                               callback_data='third')
        key.row(key_first6)
        key.row(key_second)
        key.row(key_third)
        bot.send_message(message.chat.id, 'Желаете выбрать данный поезд?', reply_markup=key)

    elif city == "Нурсултан" and city2 == "Алматы" and date == "21":
        bot.send_message(message.from_user.id, """\r
                                                                                                                                                                      Поезд № 004Ц ,Нур-Султан-Нурлы Жол →  Алматы 2
Отправление
Нурсултан
21.05.2021, 15:33
Прибытие
Алматы
22.05.2021, 06:43
Вагон Плацкартный
Общее время в пути - 15 ч. 10 мин.
Билеты от 6313 ₸


                                                                                                                                                                      """,
                         parse_mode="Markdown")
        key = types.InlineKeyboardMarkup()
        key_first6 = types.InlineKeyboardButton("Да", callback_data='a21')
        key_second = types.InlineKeyboardButton("Нет", callback_data='second')
        key_third = types.InlineKeyboardButton("Другие поезда ",
                                               url="https://aviata.kz/railways/search?station_from=2708001&station_to=2700000&departure_date=21.05.2021",
                                               callback_data='third')
        key.row(key_first6)
        key.row(key_second)
        key.row(key_third)
        bot.send_message(message.chat.id, 'Желаете выбрать данный поезд?', reply_markup=key)

    elif city == "Нурсултан" and city2 == "Алматы" and date == "22":
        bot.send_message(message.from_user.id, """\r
                                                                                                                                                                            Поезд № 004Ц ,Нур-Султан-Нурлы Жол →  Алматы 2
Отправление
Нурсултан
22.05.2021, 15:33
Прибытие
Алматы
23.05.2021, 06:43
Вагон Плацкартный
Общее время в пути - 15 ч. 10 мин.
Билеты от 6313 ₸


                                                                                                                                                                            """,
                         parse_mode="Markdown")
        key = types.InlineKeyboardMarkup()
        key_first6 = types.InlineKeyboardButton("Да", callback_data='a22')
        key_second = types.InlineKeyboardButton("Нет", callback_data='second')
        key_third = types.InlineKeyboardButton("Другие поезда ",
                                               url="https://aviata.kz/railways/search?station_from=2708001&station_to=2700000&departure_date=22.05.2021",
                                               callback_data='third')
        key.row(key_first6)
        key.row(key_second)
        key.row(key_third)
        bot.send_message(message.chat.id, 'Желаете выбрать данный поезд?', reply_markup=key)

    elif city == "Нурсултан" and city2 == "Алматы" and date == "23":
        bot.send_message(message.from_user.id, """\r
                                                                                                                                                                              Поезд № 004Ц ,Нур-Султан-Нурлы Жол →  Алматы 2
Отправление
Нурсултан
23.05.2021, 15:33
Прибытие
Алматы
24.05.2021, 06:43
Вагон Плацкартный
Общее время в пути - 15 ч. 10 мин.
Билеты от 6313 ₸


                                                                                                                                                                              """,
                         parse_mode="Markdown")
        key = types.InlineKeyboardMarkup()
        key_first6 = types.InlineKeyboardButton("Да", callback_data='a23')
        key_second = types.InlineKeyboardButton("Нет", callback_data='second')
        key_third = types.InlineKeyboardButton("Другие поезда ",
                                               url="https://aviata.kz/railways/search?station_from=2708001&station_to=2700000&departure_date=23.05.2021",
                                               callback_data='third')
        key.row(key_first6)
        key.row(key_second)
        key.row(key_third)
        bot.send_message(message.chat.id, 'Желаете выбрать данный поезд?', reply_markup=key)

    elif city == "Нурсултан" and city2 == "Алматы" and date == "24":
        bot.send_message(message.from_user.id, """\r
                                                                                                                                                                                      Поезд № 004Ц ,Нур-Султан-Нурлы Жол →  Алматы 2
Отправление
Нурсултан
24.05.2021, 15:33
Прибытие
Алматы
25.05.2021, 06:43
Вагон Плацкартный
Общее время в пути - 15 ч. 10 мин.
Билеты от 6313 ₸


                                                                                                                                                                                      """,
                         parse_mode="Markdown")
        key = types.InlineKeyboardMarkup()
        key_first6 = types.InlineKeyboardButton("Да", callback_data='a24')
        key_second = types.InlineKeyboardButton("Нет", callback_data='second')
        key_third = types.InlineKeyboardButton("Другие поезда ",
                                               url="https://aviata.kz/railways/search?station_from=2708001&station_to=2700000&departure_date=24.05.2021",
                                               callback_data='third')
        key.row(key_first6)
        key.row(key_second)
        key.row(key_third)
        bot.send_message(message.chat.id, 'Желаете выбрать данный поезд?', reply_markup=key)

    elif city == "Нурсултан" and city2 == "Алматы" and date == "25":
        bot.send_message(message.from_user.id, """\r
                                                                                                                                                                                          Поезд № 004Ц ,Нур-Султан-Нурлы Жол →  Алматы 2
Отправление
Нурсултан
25.05.2021, 15:33
Прибытие
Алматы
26.05.2021, 06:43
Вагон Плацкартный
Общее время в пути - 15 ч. 10 мин.
Билеты от 6313 ₸


                                                                                                                                                                                          """,
                         parse_mode="Markdown")
        key = types.InlineKeyboardMarkup()
        key_first6 = types.InlineKeyboardButton("Да", callback_data='a25')
        key_second = types.InlineKeyboardButton("Нет", callback_data='second')
        key_third = types.InlineKeyboardButton("Другие поезда ",
                                               url="https://aviata.kz/railways/search?station_from=2708001&station_to=2700000&departure_date=25.05.2021",
                                               callback_data='third')
        key.row(key_first6)
        key.row(key_second)
        key.row(key_third)
        bot.send_message(message.chat.id, 'Желаете выбрать данный поезд?', reply_markup=key)

    elif city == "Нурсултан" and city2 == "Алматы" and date == "26":
        bot.send_message(message.from_user.id, """\r
                                                                                                                                                                                              Поезд № 004Ц ,Нур-Султан-Нурлы Жол →  Алматы 2
Отправление
26.05.2021, 15:33
Прибытие
Алматы
27.05.2021, 06:43
Вагон Плацкартный
Общее время в пути - 15 ч. 10 мин.
Билеты от 6313 ₸


                                                                                                                                                                                              """,
                         parse_mode="Markdown")
        key = types.InlineKeyboardMarkup()
        key_first6 = types.InlineKeyboardButton("Да", callback_data='a26')
        key_second = types.InlineKeyboardButton("Нет", callback_data='second')
        key_third = types.InlineKeyboardButton("Другие поезда ",
                                               url="https://aviata.kz/railways/search?station_from=2708001&station_to=2700000&departure_date=26.05.2021",
                                               callback_data='third')
        key.row(key_first6)
        key.row(key_second)
        key.row(key_third)
        bot.send_message(message.chat.id, 'Желаете выбрать данный поезд?', reply_markup=key)

    elif city == "Нурсултан" and city2 == "Алматы" and date == "27":
        bot.send_message(message.from_user.id, """\r
                                                                                                                                                                                              Поезд № 004Ц ,Нур-Султан-Нурлы Жол →  Алматы 2
Отправление
Нурсултан
27.05.2021, 15:33
Прибытие
Алматы
28.05.2021, 06:43
Вагон Плацкартный
Общее время в пути - 15 ч. 10 мин.
Билеты от 6313 ₸


                                                                                                                                                                                              """,
                         parse_mode="Markdown")
        key = types.InlineKeyboardMarkup()
        key_first6 = types.InlineKeyboardButton("Да", callback_data='a27')
        key_second = types.InlineKeyboardButton("Нет", callback_data='second')
        key_third = types.InlineKeyboardButton("Другие поезда ",
                                               url="https://aviata.kz/railways/search?station_from=2708001&station_to=2700000&departure_date=27.05.2021",
                                               callback_data='third')
        key.row(key_first6)
        key.row(key_second)
        key.row(key_third)
        bot.send_message(message.chat.id, 'Желаете выбрать данный поезд?', reply_markup=key)

    elif city == "Нурсултан" and city2 == "Алматы" and date == "28":
        bot.send_message(message.from_user.id, """\r
                                                                                                                                                                                                  Поезд № 004Ц ,Нур-Султан-Нурлы Жол →  Алматы 2
Отправление
Нурсултан
28.05.2021, 15:33
Прибытие
Алматы
29.05.2021, 06:43
Вагон Плацкартный
Общее время в пути - 15 ч. 10 мин.
Билеты от 6313 ₸


                                                                                                                                                                                                  """,
                         parse_mode="Markdown")
        key = types.InlineKeyboardMarkup()
        key_first6 = types.InlineKeyboardButton("Да", callback_data='a28')
        key_second = types.InlineKeyboardButton("Нет", callback_data='second')
        key_third = types.InlineKeyboardButton("Другие поезда ",
                                               url="https://aviata.kz/railways/search?station_from=2708001&station_to=2700000&departure_date=28.05.2021",
                                               callback_data='third')
        key.row(key_first6)
        key.row(key_second)
        key.row(key_third)
        bot.send_message(message.chat.id, 'Желаете выбрать данный поезд?', reply_markup=key)

    elif city == "Нурсултан" and city2 == "Алматы" and date == "29":
        bot.send_message(message.from_user.id, """\r
                                                                                                                                                                                                      Поезд № 004Ц ,Нур-Султан-Нурлы Жол →  Алматы 2
Отправление
Нурсултан
29.05.2021, 15:33
Прибытие
Алматы
30.05.2021, 06:43
Вагон Плацкартный
Общее время в пути - 15 ч. 10 мин.
Билеты от 6313 ₸


                                                                                                                                                                                                      """,
                         parse_mode="Markdown")
        key = types.InlineKeyboardMarkup()
        key_first6 = types.InlineKeyboardButton("Да", callback_data='a29')
        key_second = types.InlineKeyboardButton("Нет", callback_data='second')
        key_third = types.InlineKeyboardButton("Другие поезда ",
                                               url="https://aviata.kz/railways/search?station_from=2708001&station_to=2700000&departure_date=29.05.2021",
                                               callback_data='third')
        key.row(key_first6)
        key.row(key_second)
        key.row(key_third)
        bot.send_message(message.chat.id, 'Желаете выбрать данный поезд?', reply_markup=key)

    elif city == "Нурсултан" and city2 == "Алматы" and date == "30":
        bot.send_message(message.from_user.id, """\r
                                                                                                                                                                                                      Поезд № 004Ц ,Нур-Султан-Нурлы Жол →  Алматы 2
Отправление
Нурсултан
30.05.2021, 15:33
Прибытие
Алматы
1.06.2021, 06:43
Вагон Плацкартный
Общее время в пути - 15 ч. 10 мин.
Билеты от 6313 ₸


                                                                                                                                                                                                      """,
                         parse_mode="Markdown")
        key = types.InlineKeyboardMarkup()
        key_first6 = types.InlineKeyboardButton("Да", callback_data='a30')
        key_second = types.InlineKeyboardButton("Нет", callback_data='second')
        key_third = types.InlineKeyboardButton("Другие поезда ",
                                               url="https://aviata.kz/railways/search?station_from=2708001&station_to=2700000&departure_date=30.05.2021",
                                               callback_data='third')
        key.row(key_first6)
        key.row(key_second)
        key.row(key_third)
        bot.send_message(message.chat.id, 'Желаете выбрать данный поезд?', reply_markup=key)


    else:
        bot.send_message(message.from_user.id, "По вашему запросу ничего не найдено.")
        bot.send_message(message.chat.id, "Попробуем еще раз!")
        bot.send_message(message.chat.id, "Привет! Вы хотите ознакомиться с ближайшим расписанием ЖД Вокзалов?")
        bot.register_next_step_handler(message, reg_answer)


bot.polling(none_stop=True)

