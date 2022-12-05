class Order():
    def __init__(self, list_pizza=[]):
        self.list_pizza = list_pizza
    def __str__(self):
        return f'Пицца {self.list_pizza}'
    def add_pizza(self, obj):
        self.obj = obj
        list_pizza.append(self.obj)
        count += 1

    def suma(self, sum_of_check):
        self.sum_of_check += self.price
        print(f'Заказ {self.list_pizza} Сумма {self.sum_of_check}')


    def perform(self):
        print(f'{list_pizza} {sum_of_check}')

    def TimeOfOrder(self, time_order):
        self.time_order = time_order
        while time_order != 'N':
            if time_order == 'Y':
                time_of_order = time.localtime()
                timeOrder = time.strftime('%m/%d/%y, %H:%M:%S', time_of_order)
                list_pizza.append(timeOrder)
            else:
                print('Пицца не добавлена')
                time_order = input('Добавить пиццу? Y/N')

list_pizza = []
count = 0
time_order = input('Добавить пиццу? Y/N')
sum_of_check = 0
