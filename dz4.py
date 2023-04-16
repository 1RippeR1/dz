class travel:

    def hello(self,name):
        print(f'Здравствуйте {name}')
        self.name = name

    def first_part(self,pleace):
        if pleace in ['Italia','Brazilia','USA']:
            self.way = True
        else:
            print(f'{self.name} у нас нет  путевки в {pleace}')
    def second_part(self):
        if self.way:
            print(f'''Price 
1-Italia = 10000
2-Brazilia = 20000
3-USA = 15000''')
        else: print('Всего хорошего')
    def thert_part(self,ready):
        ready = int(input())
        if ready == 1 :
            print('ваш рейс завтра')
        elif ready == 2:
            print('Ваш рейс после завтра')
        elif ready == 3:
            print("Ваш рейс сегодня")

g = travel()
g.hello(input('Введите имя '))
g.first_part(input('Куда вы хотите поехать'))
g.second_part()
g.thert_part()