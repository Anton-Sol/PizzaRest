import time

# class Order():
#     def __init__(self):
#         self.list_pizza = []

#     def __str__(self):
#         return f'Пицца {self.list_pizza}'

#     def add_pizza(self, obj):
#         self.obj = obj
#         self.list_pizza.append(self.obj)
#         count += 1

#     def suma(self, sum_of_check):
#         self.sum_of_check += self.price
#         print(f'Заказ {self.list_pizza} Сумма {self.sum_of_check}')


#     def perform(self):
#         print(f'{self.list_pizza} {self.sum_of_check}')

#     def TimeOfOrder(self, time_order):
#         self.time_order = time_order
#         while time_order != 'N':
#             if time_order == 'Y':
#                 time_of_order = time.localtime()
#                 timeOrder = time.strftime('%m/%d/%y, %H:%M:%S', time_of_order)
#                 self.list_pizza.append(timeOrder)
#             else:
#                 print('Пицца не добавлена')
#                 time_order = input('Добавить пиццу? Y/N')

class Order:

    def __init__(self):
        self.list_of_goods= []

        
        self.sum_of_check = 0
        self.order_num = 0

    def __str__(self) -> str:
        for i in range(len(self.list_of_goods)):
            print(f'{i+1}. {self.list_of_goods[i]}  {self.list_of_goods[i].price} руб.')
        
    def add_meal(self, meal):
        self.list_of_goods.append(meal)

    


    def suma(self):
        for i in range(len(self.list_of_goods)):
            print(f'{i+1}. {self.list_of_goods[i]}')
            self.sum_of_check += self.list_of_goods[i].price
        print(f'''
        Сумма заказа: {self.sum_of_check} руб.
        ''')
        return self.sum_of_check

    def perform(self, pos):
        print('Заказ передан кухне')
        self.time_order_start = time.strftime('%H:%M:%S')
        status = 'Готовится'
        count = 0
        for pizza in self.list_of_goods:
            count += pizza.tm
        self.time_order_fin = time.strftime('%H:%M:%S')
        self.order_num = pos
        print(f'Номер заказа {self.order_num}')
