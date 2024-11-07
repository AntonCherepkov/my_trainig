from class_man import Man 

class Home:
    def __init__(self):
        self.addres = self.geolocation_home()
        self.fridge = 50
        self.monay_storage = 0
        self.lst_residents = []

    def show_info(self):
        print('Адрес дома:\n   Город: {}\n   Улица: {}\n   Номер дома: {}'.format(
                self.addres['city'], self.addres['street'], self.addres['num_house']))
        print('Запасы еды в доме: {}\nЗапасы денег в доме: {}\nКоличество проживающих в доме: {}'.format(
                self.fridge, self.monay_storage, len(self.lst_residents)))        
        print('В доме проживают:', end=' ')
        for man in self.lst_residents:
            print(man.name, end=' ')

    @classmethod
    def geolocation_home(self):
        out_dict = dict()
        out_dict['city'] = 'Екатеринбург'   #input('Введите город: ')
        out_dict['street'] = 'Петрова'      #input('Введте улицу: ')
        out_dict['num_house'] = '10'        #input('Введите номер дома: ')

        return out_dict
