class Drink:
    def __init__(self, nameDrink, sizeDrink, priceDrink):
        self.nameDrink = nameDrink
        self.sizeDrink = sizeDrink
        self.priceDrink = priceDrink

    def __str__(self):
        return f'Напиток - {self.nameDrink},объем - {self.sizeDrink} мл, ' \
               f'цена - {self.priceDrink} рублей'

    def add_sugar(self):
        sugar = int(input('Сколько кусков сахара вы хотите положить(1 кусок - 5 рублей) '))
        costSugar = 5 * sugar
        return costSugar

    def add_cream(self):
        costCream = 0
        r = input('Хотите ли положить сливки(стоимость 20 рублей): yes/no')

        if r == 'yes':
            costCream += 20
            return costCream
        elif r == 'no':
            return costCream

    def poor_drink(self):
        e = int(input('С собой или в кафе: 1 - с собой, 2 - в кафе'))
        if e == 1:
            return f'{self.nameDrink} с собой'
        elif e == 2:
            return f'{self.nameDrink} наливаем в бокал'


class Tee(Drink):
    def __init__(self, nameDrink, sizeDrink, priceDrink, degreeTee):
        Drink.__init__(self, nameDrink, sizeDrink, priceDrink)
        self.degreeTee = degreeTee

    def __str__(self):
        return f'Напиток - {self.nameDrink},(для чая {self.degreeTee} градусов, объем - {self.sizeDrink} мл, ' \
               f'цена - {self.priceDrink} рублей'


class Coffe(Drink):
    def __init__(self, nameDrink, sizeDrink, priceDrink, degreeCoffe):
        Drink.__init__(self, nameDrink, sizeDrink, priceDrink)
        self.degreeCoffe = degreeCoffe


class Cola(Drink):
    def __init__(self, nameDrink, sizeDrink, priceDrink):
        Drink.__init__(self, nameDrink, sizeDrink, priceDrink)


n = int(input('Какой напиток вы желаете(введите нужную цифру): 1 - чай, 2 - кофе, 3- cola '))
if n == 1:
    w = int(input('Какой чай вы желаете(введите нужную цифру): 1 - черный, 2 - зеленый, 3- молочный улун'))
    listTee = ['черный чай ', 'зеленый чай', 'молочный улун']
    nameDrink = listTee[w - 1]
    sizeDrink = input('Введите объем емкости(мл): 250/500/750')
    listTeePrice = {'250': 150, '500': 300, '750': 500}
    priceDrink = listTeePrice[sizeDrink]
    degreeTee = int(input('Введите температуру заваривания чая '))
    orderDrink = Tee(nameDrink, sizeDrink, priceDrink, degreeTee)
    print(orderDrink.poor_drink())
    print(orderDrink)
    costSugar = orderDrink.add_sugar()
    costCream = orderDrink.add_cream()
    totalPrice = priceDrink + costSugar + costCream
    print(f'Итоговая цена напитка {nameDrink}: {totalPrice} рублей')
elif n == 2:
    w = int(input('Какой кофе вы желаете(введите нужную цифру): 1 - эспрессо, 2 - капучино, 3- латте'))
    listCoffe = ['эспрессо ', 'капучино', 'латте']
    nameDrink = listCoffe[w - 1]
    sizeDrink = input('Введите объем емкости(мл): 250/500/750')
    listCoffePrice = {'250': 200, '500': 350, '750': 600}
    priceDrink = listCoffePrice[sizeDrink]
    degreeCoffe = int(input('Введите температуру кипячения '))
    orderDrink = Coffe(nameDrink, sizeDrink, priceDrink, degreeCoffe)
    print(orderDrink.poor_drink())
    print(orderDrink)
    costSugar = orderDrink.add_sugar()
    costCream = orderDrink.add_cream()
    totalPrice = priceDrink + costSugar + costCream
    print(f'Итоговая цена напитка {nameDrink}: {totalPrice} рублей')
elif n == 3:
    sizeDrink = input('Введите объем емкости(мл): 250/500/750')
    listCola = {'250': 100, '500': 200, '750': 300}
    priceDrink = listCola[sizeDrink]
    orderDrink = Cola('Cola', sizeDrink, priceDrink)
    print(orderDrink.poor_drink())
    print(orderDrink)
    costSugar = orderDrink.add_sugar()
    costCream = orderDrink.add_cream()
    totalPrice = priceDrink + costSugar + costCream
    print(f'Итоговая цена {nameDrink}: {totalPrice} рублей')


#
# n=(input('Какой напиток желаете: 1 - лате, 2 - капучино, 3 - мокко'))
#
#
# listCof={'1':100,'2':120,'3':150}
# price=listCof[n]
# print(price)

