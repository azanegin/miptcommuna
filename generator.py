#!/usr/bin/python
#  -*- coding: UTF-8 -*-

import random


'''
Firtst_name
surname
second_name
birthday
mipt_departure
mipt_group
vk
facebook
skype
phystech_mail
main_mail
phone
campus_number
campus_room
'''
def generateuser(USER_COUNT):
    data = []
    # мастер пользователь, он не может удовлетворить запоросы=)
    data.append(['Админ','Админенко','Админович','04.04.1984','ФУПМ','000','vk.com/admin','facebook.com/admin','admin','admin@phystech.mail','admin@gmail.com','(666)-666-66-66','7','501'])
    name_list = ['Никита', 'Кирилл', 'Даниил', 'Максим', 'Артем', 'Матвей', 'Булат', 'Ярослав', 'Егор', 'Марк', 'Тимофей', 'Дмитрий', 'Арсений', 'Глеб', 'Александр', 'Роман', 'Тимур', 'Иван', 'Михаил', 'Макар', 'Константин', 'Владислав', 'Богдан', 'Денис', 'Алексей', 'Давид', 'Андрей', 'Святослав', 'Лев', 'Назар', 'Алиса', 'Вероника', 'Мелена', 'Дарья', 'Анастасия', 'Мария', 'Ангелина', 'Каролина', 'Камилла']
    surname_list = ['Смирнов', 'Иванов', 'Кузнецов', 'Соколов', 'Попов', 'Лебедев', 'Козлов', 'Новиков', 'Морозов', 'Петров', 'Волков', 'Соловьёв', 'Васильев', 'Зайцев', 'Павлов', 'Семёнов', 'Голубев', 'Виноградов', 'Богданов', 'Воробьёв', 'Фёдоров', 'Михайлов', 'Беляев', 'Тарасов', 'Белов', 'Комаров', 'Орлов', 'Киселёв', 'Макаров', 'Андреев', 'Ковалёв', 'Ильин', 'Гусев', 'Титов', 'Кузьмин', 'Кудрявцев', 'Баранов', 'Куликов', 'Алексеев', 'Степанов', 'Яковлев', 'Сорокин', 'Сергеев', 'Романов', 'Захаров', 'Борисов', 'Королёв', 'Герасимов', 'Пономарёв', 'Григорьев', 'Лазарев', 'Медведев', 'Ершов', 'Никитин', 'Соболев', 'Рябов', 'Поляков', 'Цветков', 'Данилов', 'Жуков', 'Фролов', 'Журавлёв', 'Николаев', 'Крылов', 'Максимов', 'Сидоров', 'Осипов', 'Белоусов', 'Федотов', 'Дорофеев', 'Егоров', 'Матвеев', 'Бобров', 'Дмитриев', 'Калинин', 'Анисимов', 'Петухов', 'Антонов', 'Тимофеев', 'Никифоров', 'Веселов', 'Филиппов', 'Марков', 'Большаков', 'Суханов', 'Миронов', 'Ширяев', 'Александров', 'Коновалов', 'Шестаков', 'Казаков', 'Ефимов', 'Денисов', 'Громов', 'Фомин', 'Давыдов', 'Мельников', 'Щербаков', 'Блинов', 'Колесников', 'Карпов', 'Афанасьев', 'Власов', 'Маслов', 'Исаков', 'Тихонов', 'Аксёнов', 'Гаврилов', 'Родионов', 'Котов', 'Горбунов', 'Кудряшов', 'Быков', 'Зуев', 'Третьяков', 'Савельев', 'Панов', 'Рыбаков', 'Суворов', 'Абрамов', 'Воронов', 'Мухин', 'Архипов', 'Трофимов', 'Мартынов', 'Емельянов', 'Горшков', 'Чернов', 'Овчинников', 'Селезнёв', 'Панфилов', 'Копылов', 'Михеев', 'Галкин', 'Назаров', 'Лобанов', 'Лукин', 'Беляков', 'Потапов', 'Некрасов', 'Хохлов', 'Жданов', 'Наумов', 'Шилов', 'Воронцов', 'Ермаков', 'Дроздов', 'Игнатьев', 'Савин', 'Логинов', 'Сафонов', 'Капустин', 'Кириллов', 'Моисеев', 'Елисеев', 'Кошелев', 'Костин', 'Горбачёв', 'Орехов', 'Ефремов', 'Исаев', 'Евдокимов', 'Калашников', 'Кабанов', 'Носков', 'Юдин', 'Кулагин', 'Лапин', 'Прохоров', 'Нестеров', 'Харитонов', 'Агафонов', 'Муравьёв', 'Ларионов', 'Федосеев', 'Зимин', 'Пахомов', 'Шубин', 'Игнатов', 'Филатов', 'Крюков', 'Рогов', 'Кулаков', 'Терентьев', 'Молчанов', 'Владимиров', 'Артемьев', 'Гурьев', 'Зиновьев', 'Гришин', 'Кононов', 'Дементьев', 'Ситников', 'Симонов', 'Мишин', 'Фадеев', 'Комиссаров', 'Мамонтов', 'Носов', 'Гуляев', 'Шаров', 'Устинов', 'Вишняков', 'Евсеев', 'Лаврентьев', 'Брагин', 'Константинов', 'Корнилов', 'Авдеев', 'Зыков', 'Бирюков', 'Шарапов', 'Никонов', 'Щукин', 'Дьячков', 'Одинцов', 'Сазонов', 'Якушев', 'Красильников', 'Гордеев', 'Самойлов', 'Князев', 'Беспалов', 'Уваров', 'Шашков', 'Бобылёв', 'Доронин', 'Белозёров', 'Рожков', 'Самсонов', 'Мясников', 'Лихачёв', 'Буров', 'Сысоев', 'Фомичёв', 'Русаков', 'Стрелков', 'Гущин', 'Тетерин', 'Колобов', 'Субботин', 'Фокин', 'Блохин', 'Селиверстов', 'Пестов', 'Кондратьев', 'Силин', 'Меркушев', 'Лыткин', 'Туров']
    secondname_list = ['Никитович', 'Кирилловчи', 'Даниилович', 'Максимович', 'Артемович', 'Матвеевич', 'Булатович', 'Ярославович', 'Егорович', 'Маркович', 'Тимофеевич', 'Дмитриевич', 'Арсениевич', 'Глебович', 'Александрович', 'Романович', 'Тимурович', 'Иванович', 'Михаилович', 'Макарович', 'Константинович', 'Владиславович', 'Богданович', 'Денисович', 'Алексеквич', 'Давидович', 'Андреевич', 'Святославович', 'Львович', 'Назарович']
    depertment_list = ['ФРТК', 'ФОПФ', 'ФАКИ', 'ФМХФ', 'ФФКЭ', 'ФУПМ', 'ФПФЭ', 'ФИВТ', 'ФНБИК']
    count_i = 0
    while (count_i < USER_COUNT):
        temp = []
        temp.append(name_list[random.randint(0,len(name_list) - 1)]) # имя
        temp.append(surname_list[random.randint(0,len(surname_list) - 1)]) # фамилия
        temp.append(surname_list[random.randint(0,len(surname_list) - 1)]) # отчество
        temp.append(str(random.randint(1,28)) + '.' + str(random.randint(1, 12)) + '.' + str(random.randint(1989, 1999))) # дата рождения
        temp.append(depertment_list[random.randint(0,len(depertment_list) - 1)])  # факультиет
        temp.append(str(random.randint(0, 9)) + str(random.randint(1, 8)) + str(random.randint(1, 8))) # группа
        temp.append('vk.com/'+str(random.randint(10000000, 90000000))) # вк
        temp.append('') # фб
        temp.append('') # скайп
        temp.append(str(random.randint(10000000, 90000000)) + '@phystech.edu') # физтех почта
        temp.append('') # доп почта
        temp.append('') # телефон
        temp.append(random.randint(1, 11)) # общага
        temp.append(random.randint(100, 400)) # номер комнаты
        data.append(temp)
        count_i += 1
    return data


'''
type
owner
quality
location
status
des
campus
'''
def generateitem(ITEM_COUNT, USER_COUNT):
    data = []
    counter_i = 0
    item_type_list = ['Настольные игры', 'Игровые приставки', 'Велики', 'Коньки/ролики', 'Cпорт инвентарь', 'Хоз. предметы', 'Фото/видео техника', 'МФУ', 'Конспекты/задания']
    quality_list = ['Плохое', 'Среднее', 'Хорошее', 'Новое']
    while (counter_i < ITEM_COUNT):
        temp =[]
        temp.append(item_type_list[random.randint(0,len(item_type_list) - 1)]) # тип
        temp.append(random.randint(2, USER_COUNT)) # владелец
        temp.append(quality_list[random.randint(0, len(quality_list) - 1)]) # качество
        temp.append('my room') # где находится
        x = True
        if (random.randint(0,1) == 0):
            x = False
        temp.append(x) # используется сейчяас ли нет
        temp.append('need money, use it') # описание
        x = True
        if (random.randint(0,1) == 0):
            x = False
        temp.append(x) # является ли общественным
        data.append(temp)
        counter_i += 1
    return data

'''
who
need
time
duration
description
complete by
cancel?
'''
def generatequery(QUERY_COUNT, ITEM_COUNT, USER_COUNT):
    data = []
    item_type_list = ['Настольные игры', 'Игровые приставки', 'Велики', 'Коньки/ролики', 'Cпорт инвентарь', 'Хоз. предметы', 'Фото/видео техника', 'МФУ', 'Конспекты/задания']
    time_list=[['сегодня', 'завтра', 'после завтра', 'пятница', 'выходные'], ['утро', 'день', 'вечер', 'ночь']]
    counter_i = 0
    while (counter_i < QUERY_COUNT):
        temp = []
        temp.append(random.randint(2, USER_COUNT)) # кому нужно
        temp.append(item_type_list[random.randint(0, len(item_type_list) -1)]) # что нужно
        temp.append(time_list[0][random.randint(0, len(time_list[0]) - 1)] + ' ' + time_list[1][random.randint(0, len(time_list[1]) - 1)] ) # когда нужно
        x = random.randint(0, 1)
        if (x == 0):
            temp.append(str(random.randint(1,8))+' часов')
        else:
            temp.append(str(random.randint(10,50))+' минут') # время на сколько нужно
        temp.append('Досуг') # зачем
        mode = random.randint(0,2)
        if (mode == 0):
            temp.append(1) # master-user //admin
            temp.append(False)
        elif (mode == 1):
            temp.append(1)
            temp.append(True) # отмена
        else:
            temp.append(random.randint(2, USER_COUNT))
            temp.append(False)
        data.append(temp)
        counter_i += 1
    return data


'''
:type
date
time
where
create by
support
money
description
link
'''
def generatemiting(MEETING_COUNT, USER_COUNT):
    data = []
    type_list =['Кино', 'Клуб/Концерт', 'Вечера настольных игр', 'Выставки/семинары', 'Спортивные игры', 'Транспортные маршруты', 'Поездки в магазин', 'Остальное']
    time_list=[['сегодня', 'завтра', 'после завтра', 'пятница', 'выходные'], ['утро', 'день', 'вечер', 'ночь']]
    location = ['Боталка', 'Роща', 'РИО', 'Конфитюр', 'Новодачная', 'Тимирязевская', 'КПМ']
    counter_i = 0
    while (counter_i < MEETING_COUNT):
        temp = []
        temp.append(type_list[random.randint(0, len(type_list) - 1)]) # тип
        temp.append(time_list[0][random.randint(0, len(time_list[0]) - 1)]) # дата
        temp.append(time_list[1][random.randint(0, len(time_list[1]) - 1)]) # время
        temp.append(location[random.randint(0, len(location) - 1)]) # где
        temp.append(random.randint(0, USER_COUNT)) # кто создал
        temp.append('МКИ, деканат') # кто поддерживает
        temp.append(0) # сколько денег нужно
        temp.append('Неизвестно') # описание
        temp.append('') # ссылуа на событие в вк
        data.append(temp)
        counter_i += 1
    return data

'''
meeting
user
donate
'''
def generatemember(MEMBER_COUNT, MEETING_COUNT, USER_COUNT):
    data = []
    counter_i = 0
    while(counter_i < MEMBER_COUNT):
        temp = []
        temp.append(random.randint(1, MEETING_COUNT - 1)) # встреча
        temp.append(random.randint(2, USER_COUNT)) # учасник
        temp.append(0) # донат
        data.append(temp)
        counter_i += 1
    return data

'''
meet
uploader
gallery_link
'''
def generategallery(GALLERY_COUNT, MEETING_COUNT, USER_COUNT):
    data = []
    counter_i = 0
    while(counter_i < GALLERY_COUNT):
        temp = []
        temp.append(random.randint(1, MEETING_COUNT - 1)) # встреча
        temp.append(random.randint(2, USER_COUNT)) # кто загрузил
        temp.append('vk.com/gallery_233434'+str(random.randint(100,999))) # ссылка на галерею
        data.append(temp)
        counter_i += 1
    return data

'''
name
'''
def generateshop(SHOP_COUNT):
    data = []
    counter_i = 0
    l1_list = ['Святой ','Зеленый ','Стальной ','Чудесный ','Современный ','Совершенный','']
    l2_list = ['Техно','Сити','Московский','Гипер','Мега',' Мульти','']
    l3_list = ['маркет','рынок','магазин','лавка','ларек','бар','сад'] # Святой Мегаларек, лол
    while (counter_i < SHOP_COUNT):
        temp = []
        temp = l1_list[random.randint(0, len(l1_list) - 1)] + l2_list[random.randint(0, len(l2_list) - 1)] + l3_list[random.randint(0, len(l3_list) - 1)]
        data.append(temp)
        counter_i += 1
    return data
'''
shop
tag
'''
def generatetagshop(TAG_SHOP_COUNT, SHOP_COUNT):
    data = []
    counter_i = 0
    tag_list = ['Техника', 'Одежда', 'Автомобили', 'Билеты', 'Еда', 'Растения', 'Мебель']
    while (counter_i < TAG_SHOP_COUNT):
        temp = []
        temp.append(random.randint(0, SHOP_COUNT - 1))
        temp.append(tag_list[random.randint(0, len(tag_list) - 1)])
        data.append(temp)
        counter_i += 1
    return data
'''
owner
shop
type
discount
exp_time
description
'''
def generatediscount(DISCOUNT_COUNT, SHOP_COUNT, USER_COUNT):
    data = []
    discount_list = ['Скидочная карта', 'Накопительная карта', 'Одноразовый купон', 'Разовая скидка']
    counter_i = 0
    while (counter_i < DISCOUNT_COUNT):
        temp = []
        temp.append(random.randint(2, USER_COUNT))
        temp.append(random.randint(0, SHOP_COUNT - 1))
        temp.append(discount_list[random.randint(0, len(discount_list) - 1)])
        temp.append(random.randint(3, 50))
        temp.append('никогда')
        temp.append('скидка')
        data.append(temp)
        counter_i += 1
    return data

USER_COUNT = 100
ITEM_COUNT = 100
QUERY_COUNT = 50
MEETING_COUNT = 20
MEMBER_COUNT = 200
GALLERY_COUNT = 3
SHOP_COUNT = 10
TAG_SHOP_COUNT = 20
DISCOUNT_COUNT = 20
user = generateuser(USER_COUNT) # создание пользователей
print(user)
items = generateitem(ITEM_COUNT, USER_COUNT) # создание вещей
print(items)
query = generatequery(QUERY_COUNT, ITEM_COUNT, USER_COUNT) # создание запросов
print(query)
meeting = generatemiting(MEETING_COUNT, USER_COUNT) # создание встреч
print(meeting)
member = generatemember(MEMBER_COUNT, MEETING_COUNT, USER_COUNT) # создание учасников
print(member)
galery = generategallery(GALLERY_COUNT, MEETING_COUNT, USER_COUNT) # создание галерей
print(galery)
shop = generateshop(SHOP_COUNT)
print(shop)
shop_tag = generatetagshop(TAG_SHOP_COUNT, SHOP_COUNT)
print(shop_tag)
discount = generatediscount(DISCOUNT_COUNT, SHOP_COUNT, USER_COUNT)
print(discount)



"""
# создание файлов
counter_i = 0
g = open("user.txt", "w")
g.write("\n")
while (counter_i < len(user)):



    counter_i += 1
g.close()

g = open("items.txt", "w")
g.write("\n")
counter_i = 0
while (counter_i < len(items)):

    counter_i += 1
g.close()


g = open("query.txt", "w")
g.write("\n")
counter_i = 0
while (counter_i < len(query)):

    counter_i += 1
g.close()

g = open("meet.txt", "w")
g.write("\n")
counter_i = 0
while (counter_i < len(meeting)):

    counter_i += 1
g.close()

g = open("meember.txt", "w")
g.write("\n")
counter_i = 0
while (counter_i < len(member)):

    counter_i += 1
g.close()

g = open("galery.txt", "w")
g.write("\n")
counter_i = 0
while (counter_i < len(galery)):

    counter_i += 1
g.close()

g = open("shop.txt", "w")
g.write("\n")
counter_i = 0
while (counter_i < len(shop)):

    counter_i += 1
g.close()

g = open("shop_tag.txt", "a")
g.write("\n")
counter_i = 0
while (counter_i < len(shop_tag)):

    counter_i += 1
g.close()

g = open("discount.txt", "w")
g.write("\n")
counter_i = 0
while (counter_i < len(discount)):

    counter_i += 1
g.close()
"""
