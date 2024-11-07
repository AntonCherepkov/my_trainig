import re


lst_car_numbers = 'А578ВЕ777 ОР233787 К901МН66 СТ46599 СНИ2929П777 666АМР666'

private_car = r'[АВЕКМНОРСНТУХ]\d{3}[АВЕКМНОРСНУХ]{2}\d{2,3}'
taxi_car = r'[АВЕКМНОРСНТУХ]{2}\d{3}\d{2,3}'

lst_private_car = re.findall(private_car, lst_car_numbers)
lst_taxi_car = re.findall(taxi_car, lst_car_numbers)

print(f'Список номеров частных автомобилей: {lst_private_car}')
print(f'Список номеров такси: {lst_taxi_car}')
