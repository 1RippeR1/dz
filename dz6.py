class transport():
    def start(self):
        self.engine_on = True
class ground_transport(transport):
        def have_road(self):
            print('имеется ли дорога до точки вашего назначения   Да/Нет ? ')
            quastion = input()
            self.quastion = quastion

        def Yes_No(self):
            if  self.quastion == 'Да':
                print('Выбирайте транспорт')
            else:
                print('Выберите другой вид транспорта')
                self.negation_road = False
                self.engine_on = False
class fly_transport(transport):
    def good_weather_for_fly(self):
        weather = input()
        if weather != 'storm':
            print('в даный момент палет запрещен')
            self.engine_on = False
            self.negation_fly = False
        else:
            print('погода благоприятная ')
            self.negation_fly = True
class sea_transport(transport):
    def good_weather(self):
        weather = input()
        if weather != 'storm':
            print('в даный момент плавание запрещено')
            self.engine_on = False
            self.negation_sea = False
        else:
            print('погла благоприятная ')
            self.negation_sea = True
class avto(ground_transport):
    def choice_transport(self):
        if self.engine_on:
            print('для гор джип')
            print('для дороги легковой автомобиль')
class ship(sea_transport):
    def choice_transport_sea(self):
        if self.engine_on:
            print('Возьмите катер')

class plane(fly_transport):
    def choice_transport_fly(self):
        if self.engine_on:
            print('возьмите самолет')
