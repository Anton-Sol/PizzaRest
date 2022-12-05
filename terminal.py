from order import Order
from pizza import *
from seller import Seller
from drinks import *
import time

seller = Seller()

sea = Seafood()
bbq = BBQ()
pep = Pepperoni()
cola = Cola()
tea_1 = TeaBlack200()
tea_2 = TeaBlack300()
tea_3 = TeaGreen200()
tea_4 = TeaGreen300()

menu = [sea, bbq, pep,cola, tea_1,tea_2,tea_3,tea_4]

class Terminal:
    def __init__(self,menu):
        self.menu = menu
        self.order = []
        self.ini = False

    def print_menu(self):
            print('\n'*1)
            for i in range(len(self.menu)):
                
                print(f'{i+1}. {self.menu[i]}')
            print('\n'*1)

    def check_menu(self,order):
        while True:
            self.print_menu()
            us_inp = input('''
            [Комманды да - подтвердить заказ, нет - отменить заказ,состав - состав заказа ]
            [стоп - остановить]
            Введите код пиццы 
            >>>>''').lower()
            if us_inp == 'да':
                if self.give_money(order) == True:
                    self.order.append(order)
                    order.perform(len(self.order))
                    return
                else:
                    print('Продожить составлять заказ', "\n")

            elif us_inp == 'нет':
                return
            elif  us_inp == 'состав':
                order.suma()
            elif  us_inp == 'стоп':
                seller.time_close()
                self.close(seller)
                return    
            else:
                try:
                    order.add_meal(terminal.menu[int(us_inp)-1])
                except:
                    print('Введен неверный код')




    def check_order(self, order):
        try:
            us_inp = input('Введите номер заказа\n>>>')
            for order in self.order:
                if order.order_num == int(us_inp):
                    print('..')
        except:
            print('Такой код отсутствует')
        

    def give_money(self,order):
        order.suma()
        ter_mes = input('Оплатить заказ [да/нет]').lower()
        if ter_mes == 'да':
            print('Оплата')
            return True
        elif ter_mes=='нет':
            print('Выход из оплаты')
            return False
     

    def print_check(self, seller):
        print(seller)
        print(f'Время открытия {seller.open_time}')
        print(f'Время закрытия {seller.close_time}')
        proceeds = 0
        print(f'Кол-во заказов {len(self.order)}')
        for i in range(len(self.order)):
            proceeds += self.order[i].sum_of_check
        print(f'Сумма за день {proceeds}')

            
    def open(self, seller):
        if seller.open_time:
            self.ini = True
            print(f'''Касса открыта
            Время открытия {seller.open_time}''')
            while self.ini:
                order = Order()
                self.check_menu(order)
        else:
            print('Смена закрыта , для начала зарегистрируйтесь в системе и откройте кассу')
        

    def close(self,seller):
        if seller.close_time:
            self.ini = False
            print('Касса закрыта')
            self.print_check(seller)
            self.menu = []
            self.order = []
            self.ini = False
        else:
            print('Кассир не закрыл кассу')



terminal = Terminal(menu)
seller.time_open()
terminal.open(seller)