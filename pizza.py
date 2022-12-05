import time
class Pizza:
    def __init__(self, title, dough, sauce, filling, price, tm):
        self.title = title
        self.dough = dough
        self.sauce = sauce
        self.filling = filling
        self.price = price
        self.tm = tm

    def __repr__(self):
        return self.title

    def __str__(self):
        return f'Название пиццы: {self.title}\nЦена: {self.price} руб.'

    def timer(self, time_second):
        while time_second > 0:
            t = str('{:02}:{:02}'.format(time_second // 60 % 60, time_second % 60))
            print(f'До готовности пиццы осталось: {t}', end='')
            time.sleep(1)
            print("\r\033[K", end='')
            time_second -= 1
        print('Пицца готова')


class Pepperoni(Pizza):
    def __init__(self, title='Пепперони', dough='Дрожжевое', sauce='Томатный', filling='Сосиски', price=500,
                 tm=900):
        super().__init__(title, dough, sauce, filling, price,tm)



class BBQ(Pizza):
    def __init__(self, title='Барбекю', dough='Дрожжевое', sauce='Шашлычный', filling='Курица', price=550,
                 tm=1200):
        super().__init__(title, dough, sauce, filling, price,tm)



class Seafood(Pizza):
    def __init__(self, title='Дары моря', dough='Cлоёное', sauce='Тирияки', filling='Креветки', price=600,
                 tm=600):
        super().__init__(title, dough, sauce, filling, price,tm)


if __name__!= '__main__':
    Seafood()
    Pepperoni()
    BBQ()
