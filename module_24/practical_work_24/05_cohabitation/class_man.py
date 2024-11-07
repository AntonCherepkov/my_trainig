from my_error import ThreatLifeError 

class Man:
    def __init__(self, name, age, house=None):
        self.name = name
        self.age = age

        from class_home import Home
        try:
            if isinstance(house, Home):
                self.home = house
            elif house is None:
                self.home = Home()
            else:
                raise TypeError('Не объект класса Home!')
        except TypeError as ve:
            print('Error: ', ve)
            print('Давайте создадим нужный экземпляр!')
            self.home = Home()

        self.home.lst_residents.append(self)
        self.degree_satiety = 50

    def get_eats(self):
        if self.home.fridge <= 0:
            try:
                if self.home.monay_storage == 0:
                    raise ThreatLifeError('Нет еды, и купить не на что!')
            except ThreatLifeError as end_programm:
                print('Error: ', end_programm)
            else:
                self.make_purchase()
        elif self.home.fridge < 30:
            print('      В холодильнике остался один бутерброд!')
            self.degree_satiety += self.home.fridge
            self.home.fridge = 0
        else:
            print(f'      {self.name} плотно ест!')
            self.degree_satiety += 30
            self.home.fridge -= 30

    def get_job_done(self):
        if self.age >= 18:
            if self.degree_satiety < 20:
                print(f'      {self.name} не может работать, слишком мало сил!')
                self.get_eats()
            else:
                print(f'      {self.name} полон сил и идет на работу!')
                self.degree_satiety -= 15
                self.home.monay_storage += 30

    def get_play(self):
        if self.degree_satiety <= 20:
            print(f'      {self.name} не может играть!')
            self.get_eats()
        else:
            self.degree_satiety -= 15

    def shop(self, num=None):
        if self.home.monay_storage <=0:
            print('      Дома нет денег! Необходимо поработать!')
            self.get_job_done()
        elif self.home.monay_storage < 30:
            print('      Дома осталась только мелочь!')
            self.home.fridge -= self.home.monay_storage
            self.home.monay_storage = 0
        else:
            if num:
                print(f'      {self.home.lst_residents[num].name} делает закуп в магазине!')
            else:
                print(f'      {self.name} делает закуп в магазине!')
            self.home.monay_storage -= 30
            self.home.fridge += 30

    def make_purchase(self):
        if self.age >= 18:
            self.shop()
        else:
            print('      Дети не ходят в магазин, поэтому сходил ', end='')
            for man in self.home.lst_residents:
                if man.age >= 18:
                    print(man.name)
                    self.shop(self.home.lst_residents.index(man))
                    break

    def is_check_satiety(self):
        if self.degree_satiety <= 0:
            raise ValueError(f'{self.name}: чувство голода на критической отметке!')
