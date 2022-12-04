from order import Order
from pizza import * 
from seller import Seller


seller = Seller()

class Terminal:
    def __init__(self):
        self.menu = []
        self.order = []
        self.ini = False

    def print_menu(self):
        for i in range(len(self.menu)):
            print(f'{i+1}. {self.menu[i]}')
    
    def check_menu(self,order):
        while True:
            self.print_menu()
            us_inp = input('''
            [Комманды y - подтвердить заказ, n - отменить заказ]
            Введите код пиццы >>>>''').lower()
            if us_inp == 'y':
                if self.give_money() == True:
                    order.perform()
                break

            if us_inp == 'n':    
                pass
            try:
                order.add_pizza(terminal.menu[int(us_inp)-1])
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
        

    def give_money(self):
        ter_mes = input('Оплатить заказ [да/нет]')
        if ter_mes == 'да':
            print('Оплата')
            return True
        elif ter_mes=='нет':
            raise Exception('Выход из оплаты')
     
    def print_client_check(self, order):
        order.suma()

    def print_check(self, seller):
        print(seller)
        print(f'Время открытия {seller.open_time}')
        print(f'Время закрытия {seller.close_time}')
        proceeds = 0
        print(f'Кол-во заказов {len(self.order)}')
        for i in range(len(self.order)):
            proceeds += self.order[i].price
        print(f'Сумма за день {proceeds}')

            
    def open(self, seller):
        if seller.open_time:
            self.ini = True
            print(f'''Касса открыта
            Время открытия {seller.open_time}''')
            while self.ini:
                order = Order()
                self.check_menu()
            
        

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

terminal = Terminal()
seller.time_open()
terminal.open(seller)
seller.time_close()
terminal.close(seller)
printpsdfds