#!/usr/bin/python
#  -*- coding: UTF-8 -*-

import random
from datetime import date

def generateuser(USER_COUNT):
    data = []
    # мастер пользователь, он не может удовлетворить запоросы=)
    name_list = ['Никита', 'Кирилл', 'Даниил', 'Максим', 'Артем', 'Матвей', 'Булат', 'Ярослав', 'Егор', 'Марк', 'Тимофей', 'Дмитрий', 'Арсений', 'Глеб', 'Александр', 'Роман', 'Тимур', 'Иван', 'Михаил', 'Макар', 'Константин', 'Владислав', 'Богдан', 'Денис', 'Алексей', 'Давид', 'Андрей', 'Святослав', 'Лев', 'Назар', 'Алиса', 'Вероника', 'Мелена', 'Дарья', 'Анастасия', 'Мария', 'Ангелина', 'Каролина', 'Камилла']
    surname_list = ['Смирнов', 'Иванов', 'Кузнецов', 'Соколов', 'Попов', 'Лебедев', 'Козлов', 'Новиков', 'Морозов', 'Петров', 'Волков', 'Соловьёв', 'Васильев', 'Зайцев', 'Павлов', 'Семёнов', 'Голубев', 'Виноградов', 'Богданов', 'Воробьёв', 'Фёдоров', 'Михайлов', 'Беляев', 'Тарасов', 'Белов', 'Комаров', 'Орлов', 'Киселёв', 'Макаров', 'Андреев', 'Ковалёв', 'Ильин', 'Гусев', 'Титов', 'Кузьмин', 'Кудрявцев', 'Баранов', 'Куликов', 'Алексеев', 'Степанов', 'Яковлев', 'Сорокин', 'Сергеев', 'Романов', 'Захаров', 'Борисов', 'Королёв', 'Герасимов', 'Пономарёв', 'Григорьев', 'Лазарев', 'Медведев', 'Ершов', 'Никитин', 'Соболев', 'Рябов', 'Поляков', 'Цветков', 'Данилов', 'Жуков', 'Фролов', 'Журавлёв', 'Николаев', 'Крылов', 'Максимов', 'Сидоров', 'Осипов', 'Белоусов', 'Федотов', 'Дорофеев', 'Егоров', 'Матвеев', 'Бобров', 'Дмитриев', 'Калинин', 'Анисимов', 'Петухов', 'Антонов', 'Тимофеев', 'Никифоров', 'Веселов', 'Филиппов', 'Марков', 'Большаков', 'Суханов', 'Миронов', 'Ширяев', 'Александров', 'Коновалов', 'Шестаков', 'Казаков', 'Ефимов', 'Денисов', 'Громов', 'Фомин', 'Давыдов', 'Мельников', 'Щербаков', 'Блинов', 'Колесников', 'Карпов', 'Афанасьев', 'Власов', 'Маслов', 'Исаков', 'Тихонов', 'Аксёнов', 'Гаврилов', 'Родионов', 'Котов', 'Горбунов', 'Кудряшов', 'Быков', 'Зуев', 'Третьяков', 'Савельев', 'Панов', 'Рыбаков', 'Суворов', 'Абрамов', 'Воронов', 'Мухин', 'Архипов', 'Трофимов', 'Мартынов', 'Емельянов', 'Горшков', 'Чернов', 'Овчинников', 'Селезнёв', 'Панфилов', 'Копылов', 'Михеев', 'Галкин', 'Назаров', 'Лобанов', 'Лукин', 'Беляков', 'Потапов', 'Некрасов', 'Хохлов', 'Жданов', 'Наумов', 'Шилов', 'Воронцов', 'Ермаков', 'Дроздов', 'Игнатьев', 'Савин', 'Логинов', 'Сафонов', 'Капустин', 'Кириллов', 'Моисеев', 'Елисеев', 'Кошелев', 'Костин', 'Горбачёв', 'Орехов', 'Ефремов', 'Исаев', 'Евдокимов', 'Калашников', 'Кабанов', 'Носков', 'Юдин', 'Кулагин', 'Лапин', 'Прохоров', 'Нестеров', 'Харитонов', 'Агафонов', 'Муравьёв', 'Ларионов', 'Федосеев', 'Зимин', 'Пахомов', 'Шубин', 'Игнатов', 'Филатов', 'Крюков', 'Рогов', 'Кулаков', 'Терентьев', 'Молчанов', 'Владимиров', 'Артемьев', 'Гурьев', 'Зиновьев', 'Гришин', 'Кононов', 'Дементьев', 'Ситников', 'Симонов', 'Мишин', 'Фадеев', 'Комиссаров', 'Мамонтов', 'Носов', 'Гуляев', 'Шаров', 'Устинов', 'Вишняков', 'Евсеев', 'Лаврентьев', 'Брагин', 'Константинов', 'Корнилов', 'Авдеев', 'Зыков', 'Бирюков', 'Шарапов', 'Никонов', 'Щукин', 'Дьячков', 'Одинцов', 'Сазонов', 'Якушев', 'Красильников', 'Гордеев', 'Самойлов', 'Князев', 'Беспалов', 'Уваров', 'Шашков', 'Бобылёв', 'Доронин', 'Белозёров', 'Рожков', 'Самсонов', 'Мясников', 'Лихачёв', 'Буров', 'Сысоев', 'Фомичёв', 'Русаков', 'Стрелков', 'Гущин', 'Тетерин', 'Колобов', 'Субботин', 'Фокин', 'Блохин', 'Селиверстов', 'Пестов', 'Кондратьев', 'Силин', 'Меркушев', 'Лыткин', 'Туров']
    secondname_list = ['Никитович', 'Кирилловчи', 'Даниилович', 'Максимович', 'Артемович', 'Матвеевич', 'Булатович', 'Ярославович', 'Егорович', 'Маркович', 'Тимофеевич', 'Дмитриевич', 'Арсениевич', 'Глебович', 'Александрович', 'Романович', 'Тимурович', 'Иванович', 'Михаилович', 'Макарович', 'Константинович', 'Владиславович', 'Богданович', 'Денисович', 'Алексеквич', 'Давидович', 'Андреевич', 'Святославович', 'Львович', 'Назарович']
    depertment_list = ['ФРТК', 'ФОПФ', 'ФАКИ', 'ФМХФ', 'ФФКЭ', 'ФУПМ', 'ФПФЭ', 'ФИВТ', 'ФНБИК']
    count_i = 0
    g = open('info.sql','a')
    while (count_i < USER_COUNT):
        temp = []
        temp2 = []
        temp2.append(name_list[random.randint(0,len(name_list) - 1)]) # имя
        temp2.append(surname_list[random.randint(0,len(surname_list) - 1)]) # фамилия
        temp2.append(secondname_list[random.randint(0,len(secondname_list) - 1)]) # отчество
        temp.append(temp2)
        temp.append(depertment_list[random.randint(0,len(depertment_list) - 1)])  # факультиет
        temp.append(str(random.randint(0,9))+str(random.randint(1,8))+str(random.randint(1,8))) # группа
        temp.append('vk.com/'+str(random.randint(10000000, 90000000))) # вк
        temp.append('') # фб
        temp.append('') # скайп
        temp.append(str(random.randint(10000000, 90000000)) + '@phystech.edu') # физтех почта
        temp.append('') # доп почта
        temp.append('') # телефон
        temp.append(random.randint(1, 11)) # общага
        temp.append(random.randint(100, 400)) # номер комнаты
        g.write('INSERT INTO Person (user, department, group, vkLink, fblink, skype, physMail, mainMail, phone, dormNumber, roomNumber) VALUES ('+str(temp[0])+', "'+temp[1]+'", "'+temp[2]+'", "'+temp[3]+'", "'+temp[4]+'", "'+temp[5]+'", "'+temp[6]+'", "'+temp[7]+'", "'+temp[8]+'", '+str(temp[9])+', '+str(temp[10])+');\n')
        data.append(temp)
        count_i += 1
    g.close()
    return data


def generateitem(ITEM_COUNT, USER_COUNT):
    data = []
    counter_i = 0
    item_type_list = ['Настольные игры', 'Игровые приставки', 'Велики', 'Коньки/ролики', 'Cпорт инвентарь', 'Хоз. предметы', 'Фото/видео техника', 'МФУ', 'Конспекты/задания']
    quality_list = ['Плохое', 'Среднее', 'Хорошее', 'Новое']
    g = open('info.sql','a')
    while (counter_i < ITEM_COUNT):
        temp =[]
        temp.append('Моя вещь')
        temp.append(item_type_list[random.randint(0,len(item_type_list) - 1)]) # тип
        temp.append(random.randint(1, USER_COUNT - 1)) # владелец
        temp.append(quality_list[random.randint(0, len(quality_list) - 1)]) # качество
        temp.append('my room') # где находится
        x = True
        if (random.randint(0,1) == 0):
            x = False
        temp.append(x) # используется сейчяас ли нет
        x = True
        if (random.randint(0,1) == 0):
            x = False
        temp.append(x) # является ли общественным
        temp.append('need money, use it') # описание
        g.write('INSERT INTO Item (name, itemType, owner, quality, location, status, isCommon, description) VALUES ("'+temp[0]+'", "'+temp[1]+'", '+str(temp[2])+', "'+temp[3]+'", "'+temp[4]+'", '+str(temp[5])+', '+str(temp[6])+', "'+temp[7]+'");\n')
        data.append(temp)
        counter_i += 1
    g.close()
    return data


def generatequery(QUERY_COUNT, ITEM_COUNT, USER_COUNT):
    data = []
    data2 = []
    item_type_list = ['Настольные игры', 'Игровые приставки', 'Велики', 'Коньки/ролики', 'Cпорт инвентарь', 'Хоз. предметы', 'Фото/видео техника', 'МФУ', 'Конспекты/задания']
    time_list=['утро', 'день', 'вечер', 'ночь']
    counter_i = 0
    g = open('info.sql','a')
    while (counter_i < QUERY_COUNT):
        temp = []
        temp.append(random.randint(1, USER_COUNT - 1)) # кому нужно
        temp.append(item_type_list[random.randint(0, len(item_type_list) -1)]) # что нужно
        temp.append(date.fromordinal(735710+random.randint(0, 15))) # когда нужно
        temp.append(time_list[random.randint(0, len(time_list) - 1)])
        x = random.randint(0, 1)
        if (x == 0):
            temp.append(str(random.randint(1,8))+' часов')
        else:
            temp.append(str(random.randint(10,50))+' минут') # время на сколько нужно
        temp.append('Досуг') # зачем
        x = random.randint(0, 3)
        temp2 = []
        if (x == 0):
            temp.append(False)
            temp.append(False)
        elif (x == 1):
            temp.append(False)
            temp.append(True)
        elif (x == 2):
            temp.append(True)
            temp.append(False)
            temp2.append(counter_i)
            temp2.append(random.randint(1, USER_COUNT - 1))
            g.write('INSERT INTO Squery (query, person) VALUES ('+str(temp2[0])+', '+str(temp2[1])+');\n')
        else:
            temp.append(True)
            temp.append(True)
            temp2.append(counter_i)
            temp2.append(random.randint(1, USER_COUNT - 1))
            g.write('INSERT INTO Squery (query, person) VALUES ('+str(temp2[0])+', '+str(temp2[1])+');\n')
        if (temp2 != []):
            data2.append(temp2)
        g.write('INSERT INTO Query (who, need, time, dayPart, duration, description, compelete, cancel) VALUES ('+str(temp[0])+', "'+temp[1]+'", '+str(temp[2])+', "'+temp[3]+'", "'+temp[4]+'", "'+temp[5]+'", '+str(temp[6])+', '+str(temp[7])+');\n')
        data.append(temp)
        counter_i += 1
    g.close()
    return [data, data2]


def generatemiting(MEETING_COUNT, USER_COUNT):
    data = []
    type_list =['Кино', 'Клуб/Концерт', 'Вечера настольных игр', 'Выставки/семинары', 'Спортивные игры', 'Транспортные маршруты', 'Поездки в магазин', 'Остальное']
    time_list=[['сегодня', 'завтра', 'после завтра', 'пятница', 'выходные'], ['утро', 'день', 'вечер', 'ночь']]
    location = ['Боталка', 'Роща', 'РИО', 'Конфитюр', 'Новодачная', 'Тимирязевская', 'КПМ']
    counter_i = 0
    g = open('info.sql','a')
    while (counter_i < MEETING_COUNT):
        temp = []
        temp.append(type_list[random.randint(0, len(type_list) - 1)]) # тип
        temp.append(date.fromordinal(735710+random.randint(0, 15))) # дата
        temp.append(time_list[1][random.randint(0, len(time_list[1]) - 1)]) # время
        temp.append(location[random.randint(0, len(location) - 1)]) # где
        temp.append(random.randint(1, USER_COUNT - 1)) # кто создал
        temp.append('МКИ, деканат') # кто поддерживает
        temp.append(0) # сколько денег нужно
        temp.append('Неизвестно') # описание
        temp.append('') # ссылуа на событие в вк
        g.write('INSERT INTO Meeting (metType, time, dayPart, location, creator, support, money, description, link) VALUES ("'+temp[0]+'", ' +str(temp[1])+', "'+temp[2]+'", '+', "'+temp[3]+'", '+str(temp[4])+', "'+temp[5]+'", '+str(temp[6])+', "'+temp[7]+'", "'+temp[8]+'");\n')
        data.append(temp)
        counter_i += 1
    g.close()
    return data


def generatemember(MEMBER_COUNT, MEETING_COUNT, USER_COUNT):
    data = []
    counter_i = 0
    g = open('info.sql','a')
    while(counter_i < MEMBER_COUNT):
        temp = []
        temp.append(random.randint(1, MEETING_COUNT - 1)) # встреча
        temp.append(random.randint(1, USER_COUNT - 1)) # учасник
        temp.append(0) # донат
        g.write('INSERT INTO Member (meeting, user, donate) VALUES ('+str(temp[0])+', '+str(temp[1])+', '+str(temp[2]) + ');\n')
        data.append(temp)
        counter_i += 1
    g.close()
    return data


def generategallery(GALLERY_COUNT, MEETING_COUNT, USER_COUNT):
    data = []
    counter_i = 0
    g = open('info.sql','a')
    while(counter_i < GALLERY_COUNT):
        temp = []
        temp.append(random.randint(1, MEETING_COUNT - 1)) # встреча
        temp.append(random.randint(1, USER_COUNT - 1)) # кто загрузил
        temp.append('vk.com/gallery_233434'+str(random.randint(100,999))) # ссылка на галерею
        g.write('INSERT INTO Gallery (meet, uploader, link) VALUES (' + str(temp[0]) +', '+str(temp[1])+', "'+temp[2]+'");\n')
        data.append(temp)
        counter_i += 1
    g.close()
    return data

'''
name
'''
def generateshop(SHOP_COUNT):
    data = []
    counter_i = 0
    l1_list = ['Святой ','Зеленый ','Стальной ','Чудесный ','Современный ','Совершенный ','']
    l2_list = ['Техно','Сити','Московский','Гипер','Мега',' Мульти','']
    l3_list = ['маркет','рынок','магазин','лавка','ларек','бар','сад'] # Святой Мегаларек, лол
    g = open('info.sql','a')
    while (counter_i < SHOP_COUNT):
        temp = []
        temp = l1_list[random.randint(0, len(l1_list) - 1)] + l2_list[random.randint(0, len(l2_list) - 1)] + l3_list[random.randint(0, len(l3_list) - 1)]
        data.append(temp)
        g.write('INSERT INTO Shop (shopName) VALUES ("' + temp + '");\n')
        counter_i += 1
    g.close()
    return data
'''
shop
tag
'''
def generatetagshop(TAG_SHOP_COUNT, SHOP_COUNT):
    data = []
    counter_i = 0
    tag_list = ['Техника', 'Одежда', 'Автомобили', 'Билеты', 'Еда', 'Растения', 'Мебель']
    g = open('info.sql','a')
    while (counter_i < TAG_SHOP_COUNT):
        temp = []
        temp.append(random.randint(1, SHOP_COUNT - 1))
        temp.append(tag_list[random.randint(0, len(tag_list) - 1)])
        data.append(temp)
        g.write('INSERT INTO ShopTag (shop, tag) VALUES (' + str(temp[0]) + ', "' + temp[1] + '");\n')
        counter_i += 1
    g.close()
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
    g = open('info.sql','a')
    while (counter_i < DISCOUNT_COUNT):
        temp = []
        temp.append(random.randint(1, USER_COUNT - 1))
        temp.append(random.randint(1, SHOP_COUNT - 1))
        temp.append(discount_list[random.randint(0, len(discount_list) - 1)])
        temp.append(random.randint(3, 50))
        temp.append(date.fromordinal(734777+random.randint(100, 5000)))
        temp.append('скидка')
        data.append(temp)
        g.write('INSERT INTO Discount (owner, shop, discountType, discount, expTime, description) VALUES (' +str(temp[0])+', '+str(temp[1])+', "'+temp[2]+'", '+str(temp[3])+', '+str(temp[4])+', "'+str(temp[5])+'");\n')
        counter_i += 1
    g.close()
    return data

USER_COUNT = 3
ITEM_COUNT = 100
QUERY_COUNT = 50
MEETING_COUNT = 20
MEMBER_COUNT = 200
GALLERY_COUNT = 3
SHOP_COUNT = 10
TAG_SHOP_COUNT = 20
DISCOUNT_COUNT = 20

user = generateuser(USER_COUNT) # создание пользователей#print(user)
print(user)
items = generateitem(ITEM_COUNT, USER_COUNT) # создание вещей
print(items)
query = generatequery(QUERY_COUNT, ITEM_COUNT, USER_COUNT) # создание запросов
print(query[0])
print(query[1])
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
