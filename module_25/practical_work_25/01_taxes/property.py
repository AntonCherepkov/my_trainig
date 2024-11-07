class Property:
    def __init__(self, worth):
        self.__worth = self.set_worth(worth)

    def set_worth(self, worth):
        if worth >= 0:
            return worth
        else:
            raise ValueError('Стоимость не может быть отрицательной!')

    def calculate_tax(self, divider=1):
        return round(self.__worth / divider, 3)

    def __str__(self):
        return f'{self.__class__.__name__}', f' имеет стоимость: {self.__worth}'


class Apartment(Property):
    def __init__(self, worth, address):
        super().__init__(worth)
        self.address = address
        self.tax = self.calculate_tax()

    def calculate_tax(self):
        return super().calculate_tax(1000)

    def __str__(self):
        gen_info = super().__str__()[1]
        return f'Квартира на {self.address}' + gen_info + f'\nНалог на квартиру составляет {self.tax}'


class Car(Property):
    def __init__(self, worth, brand):
        super().__init__(worth)
        self.car_brand = brand
        self.tax = self.calculate_tax()

    def calculate_tax(self):
        return super().calculate_tax(200)

    def __str__(self):
        worth_info = super().__str__()[1]
        return f'Автомобиль марки {self.car_brand}' + worth_info + f'\nНалог на автомобиль: {self.tax}'


class CountryHouse(Property):
    def __init__(self, worth, geolocation):
        super().__init__(worth)
        self.village = geolocation
        self.tax = super().calculate_tax(500)

    def __str__(self):
        worth_ino = super().__str__()[1]
        return f'Дом, находящийся в деревне {self.village}' + worth_ino + f'\nНалог на дом: {self.tax}'
