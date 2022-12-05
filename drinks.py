class Drink:
    def __init__(self, name, size, price):
        self.name = name
        self.size = size
        self.sugar = 0
        self.cream = 0
        self.price = price + self.sugar + self.cream

    def __str__(self):
        return f'''Напиток: {self.name}\nОбъем: {self.size} мл\nЦена: {self.price}'''

    def add_sugar(self):
        sugar = int(input('''Сколько кусков сахара вы хотите положить(1 кусок - 5 рублей)
        >>> '''))
        self.sugar = 5 * sugar

    def add_cream(self):
        r = input('''Добавить сливки (стоимость 20 рублей): [да/нет]
        >>> ''')

        if r == 'да':
            self.cream = 20
        elif r == 'нет':
            return 




class TeaBlack200(Drink):
    def __init__(self, name = 'Чай черный', size = 200, price = 60):
        Drink.__init__(self, name, size, price)


class TeaBlack300(Drink):
    def __init__(self, name = 'Чай черный', size = 300, price = 70):
        Drink.__init__(self, name, size, price)

class TeaGreen200(Drink):
    def __init__(self, name = 'Чай зеленый', size = 200, price = 60):
        Drink.__init__(self, name, size, price)

class TeaGreen300(Drink):
    def __init__(self, name = 'Чай черный', size = 300, price = 70):
        Drink.__init__(self, name, size, price)
    

class Cola(Drink):
    def __init__(self, name = 'Кола', size = 500, price = 100):
        Drink.__init__(self, name, size, price)

    def add_cream(self):
        return 0
    def add_sugar(self):
        return 0