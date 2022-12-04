import time

# Новая версия..

# Комментарий Антона:
# По идее, как только заказ отправляется на кухню ->
# т.е. в хранилище терминала, то должен запускаться метод time,
# который будет возвращать время приготовления каждой пиццы


class Pizza:
    def __init__(self, title, dough, sauce, filling, price, tm):
        self.title = title
        self.dough = dough
        self.sauce = sauce
        self.filling = filling
        self.price = price
        self.tm = tm

    def __str__(self):
        return f'Название пиццы: {self.title}\nТесто: {self.dough}\nСоус: {self.sauce}\nНачинка: {self.filling}\nЦена: {self.price} руб.'

    def timePizza(self):
        time_start = time.strftime("%d-%m-%Y %H:%M")
        print('Пицца начала готовиться : ', time_start)
        for i in range(self.tm, 0, -1):
            time.sleep(1)
        time_out = time.strftime("%d-%m-%Y %H:%M")
        print('Пицца приготовлена: ', time_out)


class Pepperoni(Pizza):
    def __init__(self, title='Пепперони', dough='Дрожжевое', sauce='Томатный', filling='Сосиски', price=500, tm=900):
        super().__init__(title, dough, sauce, filling, price, tm)

        return


class BBQ(Pizza):
    def __init__(self, title='Барбекю', dough='Дрожжевое', sauce='Шашлычный', filling='Курица', price=550, tm=1200):
        super().__init__(title, dough, sauce, filling, price, tm)
        return


class Seafood(Pizza):
    def __init__(self, title='Дары моря', dough='Cлоёное', sauce='Тирияки', filling='Креветки', price=600, tm=600):
        super().__init__(title, dough, sauce, filling, price, tm)
        return


p1 = Pepperoni()
print(p1)
print(p1.timePizza())

# Старая версия с таймером.
#
# Т.е. нужно просто через return вернуть значение времени приготовления(СДЕЛАЛ)
# Нооо, на всякий придержи код таймера, он возможно пригодится.
# Только нужно, чтобы он запускался не через консоль(СДЕЛАЛ) и не блокировал ввод  с клавиатуры (НЕ СДЕЛАЛ, не могу додуматься)
#
#
# class Pizza:
#     def __init__(self, title, dough, sauce, filling, price, tm=None):
#         self.title = title
#         self.dough = dough
#         self.sauce = sauce
#         self.filling = filling
#         self.price = price
#         self.tm = tm
#
#     def __str__(self):
#         return f'Название пиццы: {self.title}\nТесто: {self.dough}\nСоус: {self.sauce}\nНачинка: {self.filling}\nЦена: {self.price} руб.'
#
#     def timer(self, tme):
#         while self.tm > 0:
#             t = str('{:02}:{:02}'.format(self.tm // 60 % 60, self.tm % 60))
#             print(f'До готовности пиццы осталось: {t}', end='')
#             time.sleep(1)
#             print("\r\033[K", end='')  # данная строчка удерживает курсор на месте и блокирует ввод с клавиатуры
#             self.tm -= 1
#         print('Пицца готова')
#
#
# class Pepperoni(Pizza):
#     def __init__(self, title='Пепперони', dough='Дрожжевое', sauce='Томатный', filling='Сосиски', price=500, tm=900):
#         super().__init__(title, dough, sauce, filling, price, tm)
#         return
#
#
# class BBQ(Pizza):
#     def __init__(self, title='Барбекю', dough='Дрожжевое', sauce='Шашлычный', filling='Курица', price=550, tm=1200):
#         super().__init__(title, dough, sauce, filling, price, tm)
#         return
#
#
# class Seafood(Pizza):
#     def __init__(self, title='Дары моря', dough='Cлоёное', sauce='Тирияки', filling='Креветки', price=600, tm=600):
#         super().__init__(title, dough, sauce, filling, price, tm)
#         return
#
#
# def choice_user():
#     user = input('''1 - пицца "Пепперони", тесто дрожжевое, соус томатный, начинка сосиски, цена 500 рублей
# 2 - пицца "Барбекю", тесто дрожжевое, соус шашлычный, начинка курица, цена 550 рублей
# 3 - пицца "Дары моря", тесто слоёное, соус тирияки, начинка креветки, цена 600 рублей
# Выберите пиццу (нажмите 1/2/3): ''')
#
#     if user == '1':
#         user_pep = Pepperoni()
#         print(user_pep)
#         user_pep.timer(1)
#
#     elif user == '2':
#         user_bbq = BBQ()
#         print(user_bbq)
#         user_bbq.timer(1)
#
#     elif user == '3':
#         user_sf = Seafood()
#         print(user_sf)
#         user_sf.timer(1)
#
#
# choice_user()
