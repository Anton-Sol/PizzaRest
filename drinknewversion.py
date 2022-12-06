class Drink:
    def __init__(self, name, size, price):
        self.name = name
        self.size = size
        self.price = price
    def __str__(self):
        return f'Напиток - {self.name},объем - {self.size} мл, '   f'цена - {self.price} рублей'

    def add_sugar(self):
        sugar = int(input('Сколько кусков сахара вы хотите положить(1 кусок - 5 рублей) '))
        self.price += (5 * sugar)
        return self.price

    def add_cream(self):

        r = input('Хотите ли положить сливки(стоимость 20 рублей): yes/no')

        if r == 'yes':
            self.price += 20
            return self.price
        elif r == 'no':
            return self.price
    def poor_drink(self):
        e = int(input('С собой или в кафе: 1 - с собой, 2 - в кафе'))
        if e == 1:             return f'{self.name} с собой'
        elif e == 2:
             return f'{self.name} наливаем в бокал'
class BlackTea250ml(Drink):
    def __init__(self, name='черный чай', size=250, price=150):
        Drink.__init__(self, name, size, price)
        return
class BlackTea500ml(Drink):
    def __init__(self, name='черный чай', size=500, price=300):
        Drink.__init__(self, name, size, price)
        return
class BlackTea750ml(Drink):
    def __init__(self, name='черный чай', size=750, price=500):
        Drink.__init__(self, name, size, price)
        return
class GreenTea250ml(Drink):
    def __init__(self, name='зеленый чай', size=250, price=150):
        Drink.__init__(self, name, size, price)
        return
class GreenTea500ml(Drink):
    def __init__(self, name='зеленый чай', size=500, price=300):
        Drink.__init__(self, name, size, price)
        return
class GreenTea750ml(Drink):
    def __init__(self, name='зеленый чай', size=750, price=500):
        Drink.__init__(self, name, size, price)
        return
class OolongTea250ml(Drink):
    def __init__(self, name='улун', size=250, price=150):
        Drink.__init__(self, name, size, price)
        return
class OolongTea500ml(Drink):
    def __init__(self, name='улун', size=500, price=300):
        Drink.__init__(self, name, size, price)
        return
class OolongTea750ml(Drink):
    def __init__(self, name='улун', size=750, price=500):
        Drink.__init__(self, name, size, price)
        return
class Cola250ml(Drink):
    def __init__(self, name='cola', size=250, price=100):
        Drink.__init__(self, name, size, price)
        return
class Cola500ml(Drink):
    def __init__(self, name='cola', size=500, price=200):
        Drink.__init__(self, name, size, price)
        return
class Cola750ml(Drink):
    def __init__(self, name='cola', size=750, price=300):
        Drink.__init__(self, name, size, price)
        return
class Latte250ml(Drink):
    def __init__(self, name='латте', size=250, price=200):
        Drink.__init__(self, name, size, price)
        return
class Latte500ml(Drink):
    def __init__(self, name='латте', size=500, price=350):
        Drink.__init__(self, name, size, price)
        return
class Latte750ml(Drink):
    def __init__(self, name='латте', size=750, price=600):
        Drink.__init__(self, name, size, price)
        return
class Cappuccino250ml(Drink):
    def __init__(self, name='капучино', size=250, price=200):
        Drink.__init__(self, name, size, price)
        return
class Cappuccino500ml(Drink):
    def __init__(self, name='капучино', size=500, price=350):
        Drink.__init__(self, name, size, price)
        return
class Cappuccino750ml(Drink):
    def __init__(self, name='капучино', size=750, price=600):
        Drink.__init__(self, name, size, price)
        return
class Espresso250ml(Drink):
    def __init__(self, name='эспрессо', size=250, price=200):
        Drink.__init__(self, name, size, price)
        return
class Espresso500ml(Drink):
    def __init__(self, name='эспрессо', size=500, price=350):
        Drink.__init__(self, name, size, price)
        return
class Espresso750ml(Drink):
    def __init__(self, name='эспрессо', size=750, price=600):
        Drink.__init__(self, name, size, price)
        return
