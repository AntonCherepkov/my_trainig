from itertools import groupby

# Это просто экперимент с функцией groupby модуля itertools

vehicles = [('Ford', 'Taurus'), ('Dodge', 'Durango'),
            ('Chevrolet', 'Cobalt'), ('Ford', 'F150'),
            ('Dodge', 'Charger'), ('Ford', 'GT')]

sorted_vehicles = sorted(vehicles, key=lambda make: make[0])

for key, group in groupby(sorted_vehicles, key=lambda make: make[0]):
    print(f'Мой вывод -> {key}:{group}')
    for make, model in group:
        print(f'{model} is made by {make}')
    print ("**** END OF GROUP ***\n")
