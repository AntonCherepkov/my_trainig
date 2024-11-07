from property import Apartment
from property import Car
from property import CountryHouse


def count_tax(*args):
    summ = 0
    if all([isinstance(arg, (Apartment, Car, CountryHouse)) for arg in args]):
        for my_property in args:
            summ += my_property.tax
        return summ
    else:
        raise TypeError('Не является объектом требуемого класса!')


money = int(input("Введите количество денег: "))

cost_apartment = int(input("Введите стоимость квартиры: "))
apartment = Apartment(worth=cost_apartment, address='ул. Пушкина')

cost_car = int(input("Введите стоимость автомобиля: "))
car = Car(worth=cost_car, brand='Лада Гранта')

cost_country_house = int(input("Введите стоимость дачного дома: "))
country_house = CountryHouse(worth=cost_country_house, geolocation='Хрустальная')

print(apartment)
print(car)
print(country_house)

sum_tax = count_tax(apartment, car, country_house)

if sum_tax > money:
    print('Вам не хватит денег, что бы заплатить налоги!')
else:
    print('Налог уплачен!')