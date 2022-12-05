import time


class Seller:
    def __init__(self):
        self.open_time = None
        self.close_time = None
        self.name_seller = input('Введите имя: ')
        self.surname_seller = input('Введите фамилию: ')
        self.patronymic_seller = input('Введите Очество: ')

    def __str__(self):
        self.info_seller = f'Продавец  {self.surname_seller} {self.name_seller} {self.patronymic_seller}'
        return self.info_seller

    def time_open(self):
        # answer_open = input(f'Открыть кассу?; y/n: ')
        # while answer_open != '':
        #     if answer_open == 'y':
       
        self.open_time = time.strftime("%d-%m-%Y %H:%M")
        
        return self.open_time

            # elif answer_open == 'n':
            #     print("Касса не открыта")
            #     return False
            # else:
            #     print("Не удалось открыть кассу")
            #     answer_open = input(f'Открыть кассу?; y/n: ')

    def time_close(self):

        self.close_time = time.strftime("%d-%m-%Y %H:%M")
     
        return self.close_time

        # answer_close = input(f'закрыть кассу?; y/n: ')
        # while answer_close != '':
        #     if answer_close == 'y':
        #         close_time = time.strftime("%d-%m-%Y %H:%M")
        #         self.close_time = (f'Время закрытие кассы, {close_time}')
        #         return True

        #     elif answer_close == 'n':
        #         print("Касса не закрыта")
        #         return False
        #     else:
        #         print("Не удалось закрыть кассу")
        #         answer_close = input(f'Открыть кассу?; y/n: ')

    def print_chek(self):
        print()
        print(self.info_seller, self.open_time, sep='\n')
        print(self.info_seller, self.close_time, sep='\n')

