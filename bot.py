import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.utils import get_random_id

admins = {"148376704", "253106080"}
group = "118577465"
turn_off = list()

mens = {
    1: "Модельные - 500 ₽",
    2: "Спортивные - 350 ₽",
    3: "Наголо - 150 ₽",
    4: "Окрашивание(камуфляж седины) - 700 ₽",
    5: "Оформление бороды - 150 ₽",
    6: "Рисунок машинкой - 100 ₽",
    7: "Укладка - 300 ₽"
}

sec_mens = {
    8: "Модельная - 350 ₽",
    9: "Спортивная - 250 ₽"
}

womens = {
1: "Мытье головы и укладка 250 ₽",
2: "Стрижка женская(мытьё головы и укладка):",
21: "Короткие 500 ₽",
22: "Средняя длина волос 600 ₽",
23: "Длинные 700 ₽",
24: "Креативная стрижка 700 ₽",
25: "Подравнивание волос по одной длине 400 ₽",
26: "Оформление чёлки 150 ₽",
3: "Укладка волос, оформление утюжком:",
31: "Короткие 600 ₽",
32: "Удлиненные 700 ₽",
4: "Окрашивание волос",
41: "Короткие 1200 ₽",
42: "Удлиненные 1700 ₽",
5: "Окрашивание волос краской клиента",
51: "Короткие 700 ₽",
52: "Средняя длина волос 1000 ₽",
53: "Длинные 1300 ₽",
54: "Мелирование 1200 ₽",
6: "Сложное окрашивание(\"омбре\", \"балаяж\", \"айр тач\") 4000 ₽",
7: "Химическая завивка 1000 ₽",
8: "Карвинг 1800 ₽",
9: "Плетение кос 300 ₽",
10: "Прическа 1500 ₽",
11: "Прикорневой объем 3000 ₽",
12: "Полировка волос машинкой",
121: "Средняя длина волос 1000 ₽",
122: "Длинные 1500 ₽",
123: "Полировка волос ножницами 2000 ₽",
13: "Спа - процедуры",
131: "Уход(маска, экранирование волос) 300 ₽",
14: "Ламинирование волос",
141: "Короткие, средние 1000 ₽",
142: "Длинные, каждые 15см 500 ₽",
15: "Ботокс 3000 ₽",
16: "Кератиновое выпрямление волос 3500 ₽",
17: "Наращивание волос ",
171: "Ленточное(работа 40 лент) 4000 ₽",
172: "Коррекция 6000 ₽",
173: "Снятие лент 3000 ₽",
174: "Капсульное(работа за капсулу) 50 ₽",
175: "Коррекция(работа за капсулу) 70 ₽",
176: "Снятие(работа за капсулу) 35 ₽",
18: "Макияж 2000 ₽",
19: "Брови и ресницы:",
191: "Оформление бровей 150 ₽",
192: "Окрашивание бровей 150 ₽",
193: "Окрашивание ресниц 150 ₽",
194: "Биозавивка ресниц 1000 ₽",
195: "Долговременная укладка ресниц 1000 ₽"
}

students = {
1: "Мытье головы 20 ₽",
2: "Применение бальзама 20 ₽",
3: "Стрижка женская/мужская 50 ₽",
4: "Хим. завивка на короткие волосы 200 ₽",
5: "Хим. завивка на средние волосы 250 ₽",
6: "Хим. завивка на длинные волосы 300 ₽",
7: "Укладка с использованием фена",
71: "Короткие 50 ₽",
72: "Средняя длина волос 100 ₽",
73: "Длинные 150 ₽",
8: "Карвинг (долговременная укладка)",
81: "Короткие 350 ₽",
82: "Средняя длина волос 450 ₽",
83: "Длинные 550 ₽",
9: "Сушка волос 50 ₽",
10: "Прическа на длинные волосы 200 ₽",
11: "Окрашивание волос краской клиента 150 ₽",
12: "Окрашивание волос красителями ",
121: "Короткие 250 ₽",
122: "Средняя длина волос 300 ₽",
123: "Длинные 350 ₽",
13: "Мелирование ",
131: "Короткие 350 ₽",
132: "Средняя длина волос 400 ₽",
133: "Длинные 450 ₽",
134: "Частичные пряди 100 ₽",
14: "Ламинирование волос",
141: "Короткие 500 ₽",
142: "Длинные 650 ₽",
15: "Прикорневой объем 400 ₽"
}

speech = "Все поражаются тому, как прекрасны и ослепительны актрисы в Голливуде. И это не удивительно," +\
         " ведь делают их красивыми мастера макияжа. Каждая женщина мечтает выглядеть так же превосходно," +\
         " хочет почувствовать себя голливудской дивой, чтобы на нее обращали внимание мужчины. И в этом может" +\
         " помочь макияж. Как часть модной индустрии он насчитывает много разных стилей, из которых самый" +\
         " популярный - так называемый классический голливудский макияж.\n"

vk_session = vk_api.VkApi(token='YourToken')
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()

def set_key(kwargs):
    keyboard = VkKeyboard(one_time=True)
    a = 0
    for i in range(len(kwargs[0])):
        keyboard.add_button(kwargs[0][i], color=VkKeyboardColor.PRIMARY)
        a += 1
        if a >= 2 or i == len(kwargs[0]) - 1:
            keyboard.add_line()
            a = 0
    for i in range(len(kwargs[1])):
        keyboard.add_button(kwargs[1][i], color=VkKeyboardColor.NEGATIVE)
        if i != len(kwargs[1]) - 1:
            keyboard.add_line()
    return keyboard

def send_butt(id, text, keyboard):
    vk.messages.send(
        peer_id=id,
        random_id=get_random_id(),
        keyboard=keyboard.get_keyboard(),
        message=text
    )

def send(id, text):
    vk.messages.send(user_id=id, message=text, random_id=0)

def pricelist(admission):
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.text and event.to_me:
            sex = event.text
            id = event.user_id
            if sex == "Мужские":
                price_list = "Прайс-лист на мужские стрижки:\n"
                for i in mens:
                    price_list += str(i) + " " + mens[i] + "\n"
                send(id, price_list)
                price_list = "Для пенсионеров и детей:\n"
                for i in sec_mens:
                    price_list += str(i) + " " + sec_mens[i] + "\n"
                send_butt(id, price_list, set_key([['Мужские', 'Женские'], ['Выход']]))
                if admission:
                    send(id, "Напишите номер нужной услуги:")
                    select_menu_mens()
                    return
            elif sex == "Женские":
                price_list = "Прайс-лист на женские стрижки:\n"
                for i in womens:
                    if i > 20:
                        price_list += "•" + str(i) + " " + womens[i] + "\n"
                    else:
                        price_list += str(i) + " " + womens[i] + "\n"
                send_butt(event.user_id, price_list, set_key([['Мужские', 'Женские'], ['Выход']]))
                if admission:
                    send(event.user_id, "Напишите номер нужной услуги:")
                    select_menu_womens()
                    return
            elif sex == "Выход":
                send(event.user_id, 'Вы в главном меню')
                menu_msg(id)
                return
            else:
                send_butt(id, "Введите Мужские, Женские или Выход", set_key([['Мужские', 'Женские'], ['Выход']]))

def student_pricelist(id, admission):
    price_list = "Прайс-лист:\n"
    for i in students:
        price_list += str(i) + " " + students[i] + "\n"
    send_butt(id, price_list, set_key([['Запись'], ['Выход в меню']]))
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.text and event.to_me:
            if event.text == "Запись":
                send_butt(event.user_id, "Мастер Анна - 89655790369 \n Мастер Наталья - 89655723692",
                          set_key([[], ['Выход']]))
                for event in longpoll.listen():
                    if event.type == VkEventType.MESSAGE_NEW and event.text and event.to_me:
                        if event.text == "Выход":
                            send(event.user_id, "Bы в меню")
                            return
                        else:
                            send_butt(event.user_id, "Нажмите выход", set_key([[], ['Выход']]))
            elif event.text == "Выход в меню":
                send(event.user_id, "Bы в меню")
                return
            else:
                send_butt(event.user_id, "Выберите запись или выход в меню", set_key([['Запись'], ['Выход в меню']]))

def select_menu_mens():
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.text and event.to_me:
            try:
                if int(event.text) > 9 or int(event.text) < 1:
                    send(event.user_id, "Выберите число из возможных")
                else:
                    send(event.user_id, "Работает!")
                    break
            except BaseException:
                send(event.user_id, "Выберите число!")

def get_atr(id, attr):
    return vk.users.get(user_id=id)[0][attr]

def select_menu_womens():
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.text and event.to_me:
            try:
                send(event.user_id, womens[int(event.text)])
                break
            except Exception:
                send(event.user_id, "Выберите число из возможных!")

def about_us(id):
    send_butt(id, "Представляем Вам наш салон красоты \"Beauty code\".\n" +
              "Мы являемся школой и студией красоты✨\n" +
              "В нашей школе вы сможете обучиться:\n" +
              "✔️Курс Парикмахерского искусства\n" +
              "✔️Курс Визажист\n" +
              "✔️Курс Сам себе визажист\n" +
              "А также сможете получить все виды парикмахерских услуг, макияж, прически☝️😊\n" +
              "Мы с нетерпением ждём вас по адресу : г. Пермь, ул. Челюскинцев, 23\n" +
              "Будем рады видеть у нас в качестве клиентов, учеников и моделей😍😊\n",
              set_key([['Запись'], ['Выход в меню']])
              )
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.text and event.to_me:
            if event.text == "Запись":
                send_butt(event.user_id, "Мастер Анна - 89655790369 \n Мастер Наталья - 89655723692",
                          set_key([[], ['Выход']]))
                for event in longpoll.listen():
                    if event.type == VkEventType.MESSAGE_NEW and event.text and event.to_me:
                        if event.text == "Выход":
                            send(event.user_id, "Bы в меню")
                            return
                        else:
                            send_butt(event.user_id, "Нажмите выход", set_key([[], ['Выход']]))
            elif event.text == "Выход в меню":
                send(event.user_id, "Bы в меню")
                return
            else:
                send_butt(event.user_id, "Выберите запись или выход в меню", set_key([['Запись'], ['Выход в меню']]))

def courses(id):
    send_butt(id, "Вот список курсов, которые мы можем предложить:\n1.\"Парикмахер-универсал\"\n2.\"Визажист\"\n3.\"Сам себе визажист\"", set_key([['Парикмахер-универсал', 'Визажист', 'Сам себе визажист'], ['Выход в меню']]))
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
            if event.text == "Парикмахер-универсал":
                send_butt(event.user_id, "Базовый курс для тех, кто хочет научиться с нуля обучиться парикмахерскому искусству.\n" +
                                    "Программа курса:\n" +
                                    "✔ Лекции по организации рабочего места\n" +
                                    "✔ материаловедению\n" +
                                    "✔ физиологии кожи головы и волос\n" +
                                    "✔инструментам\n" +
                                    "✔ дезинфекции, гигиене\n" +
                                    "✔ Лекции по основам стрижки: геометрия, особенности детских стрижек, мужские и женские стрижки\n" +
                                    "✔ Отработка на моделях всех салонных процедур от мытья головы до завивки\n" +
                                    "✔Отработка на манекен-головах причесок, укладок, накрутки коклюшек.\n" +
                                    "✔Лекции, расходные материалы (все продукты от средств по уходу до оксидов) предоставляются\n" +
                                    "✔ Обучающимися приобретаются инструменты: фен, расчески, брашинг, ножницы (прямой срез, филировка).\n" +
                                    "✔Группа из 5-10 человек\n" +
                                    "✔Цена 15 000 ₽", set_key([['Парикмахер-универсал', 'Визажист', 'Сам себе визажист'], ['Выход в меню']]))
            elif event.text == "Визажист":
                send_butt(event.user_id, "Курс для тех, кто хочет научиться визажированию\n" +
                                    "Программа: \n" +
                                    "✔️1 день - теория, дневной макияж\n" +
                                    "✔️2 день - вечерний макияж\n" +
                                    "✔️3 день - голливудский макияж(стрелки)\n" +
                                    "Цена 15000 ₽\n" +
                                    "Группа 3-5 чел\n" +
                                    "Косметика и кисти предоставляются 😊", set_key([['Парикмахер-универсал', 'Визажист', 'Сам себе визажист'], ['Выход в меню']]))
            elif event.text == "Сам себе визажист":
                send_butt(event.user_id, speech +
                                    "Мы предлагаем для вас курс \"Сам себе визажист\", мы подберём образ для каждой девушки✨\n" +
                                    "в него входят:\n" +
                                    "✔ 1 день- теория, дневной макияж\n" +
                                    "✔ 2 день- вечерний макияж\n" +
                                    "✔ 3 день- голливудский макияж(стрелки)\n" +
                                    "✔ Группа 3-5 чел\n" +
                                    "✔ Цена 5 000 ₽", set_key([['Парикмахер-универсал', 'Визажист', 'Сам себе визажист'], ['Выход в меню']]))
            elif event.text == "Выход в меню":
                send(event.user_id, "Вы в меню")
                return
            else:
                send_butt(event.user_id, "Уточните запрос", set_key([['Парикмахер-универсал', 'Визажист', 'Сам себе визажист'], ['Выход в меню']]))

def menu_msg(id):
    send_butt(event.user_id,
              'Выберите: Курсы, Прайс-лист, Ученический прайс-лист, О парикмахерской и мастерах, Выход',
              set_key([['Прайс-лист', 'Курсы', 'Ученический прайс-лист', 'О нас'], ['Выход']]))

def defoult_msg(id):
    send_butt(id, "Я не понимаю, извините, попробуйте написать запрос точнее!\n Если вам надоел бот, напишите Выключить\nЕсли не знаете что делать, напишите Помощь", set_key([['Помощь'], ['Выключить']]))

def help_msg(id):
    send_butt(id, "Для того чтобы получить информацию по нашему салону введите \"Меню\" \nДля того чтобы получить номера для записи к мастеру введите \"Запись\" \nДля связи с администратором введите \"Администратор\"", set_key([['Меню', 'Администратор', 'Запись'], ['Выключить']]))

while 1 == 1:
    try:
        for event in longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
                if str(event.user_id) not in turn_off:
                    if event.text == 'Меню':
                        menu_msg(event.user_id)
                        for event in longpoll.listen():
                            if event.type == VkEventType.MESSAGE_NEW and event.text and event.to_me:
                                if event.text == "Курсы":
                                    courses(event.user_id)
                                    menu_msg(event.user_id)
                                elif event.text == "Прайс-лист":
                                    send_butt(event.user_id, "Выберите тип стрижки:", set_key([['Мужские', 'Женские'], ['Выход']]))
                                    pricelist(False)
                                elif event.text == "Ученический прайс-лист":
                                    student_pricelist(event.user_id, False)
                                    menu_msg(event.user_id)
                                elif event.text == "О нас":
                                    about_us(event.user_id)
                                    menu_msg(event.user_id)
                                elif event.text == "Выход":
                                    send(event.user_id, "Вы вышли из меню")
                                    help_msg(event.user_id)
                                    break
                                else:
                                    menu_msg(event.user_id)
                    elif event.text == "Запись онлайн":
                        send(event.user_id, "Выберите тип стрижки (М/Ж):")
                        for event in longpoll.listen():
                            if event.type == VkEventType.MESSAGE_NEW and event.text and event.to_me:
                                pricelist(True)
                    elif event.text == "Администратор":
                        send(event.user_id, "Сейчас обратимся к админам, подождите немного вам обязательно ответят😊")
                        turn_off.append(str(event.user_id))
                        send(event.user_id, "Бот выключен, для того чтобы включить его нажмите Включить")
                        for admin in admins:
                            send(admin, "Пользователь {} {} требует внимания, ссылка на диалог - {}".format(get_atr(event.user_id, 'first_name'), get_atr(event.user_id, 'last_name'), "https://vk.com/gim" + group + "?sel=" + str(event.user_id)))
                    elif event.text == "Запись":
                        send_butt(event.user_id, "Мастер Анна - 89655790369 \n Мастер Наталья - 89655723692", set_key([['Меню', 'Администратор', 'Запись'], ['Выключить']]))
                    elif event.text == "Помощь":
                        help_msg(event.user_id)
                    elif event.text == "Привет":
                        send(event.user_id, "Здравствуйте, {}!\nДля того чтобы получить информацию по нашему салону введите \"Меню\"\nДля того чтобы получить номера для записи к мастеру введите \"Запись\"\nДля связи с администратором введите \"Администратор\"".format(get_atr(event.user_id, 'first_name')))
                    elif event.text == "Спасибо":
                        send(event.user_id, "Рады вам помочь!")
                    elif event.text == "Пока":
                        send(event.user_id, "Всего доброго!")
                    elif event.text == "Выключить":
                        if str(event.user_id) is not turn_off:
                            turn_off.append(str(event.user_id))
                        send(event.user_id, "Бот выключен, для того чтобы включить его напишите \"Включить\"")
                    else:
                        defoult_msg(event.user_id)
                else:
                    if event.text == "Включить":
                        turn_off.remove(str(event.user_id))
                        send(event.user_id, "Бот включён, для того чтобы выключить его напишите Выключить")
                        help_msg(event.user_id)
    except:
        print("Error")
