from random import randint


class Toyota:
    color = 'red'
    price = 1000000
    max_speed = 200
    current_speed = 0


one_car = Toyota()
two_car = Toyota()
three_car = Toyota()

for car in one_car, two_car, three_car:
    car.current_speed = randint(0, 200)

print(one_car.current_speed, ' -> ', one_car.max_speed, ' -> ', one_car.color)
print(two_car.current_speed, ' -> ', two_car.max_speed, ' -> ', one_car.color)
print(three_car.current_speed, ' -> ', three_car.max_speed, ' -> ', one_car.color)

two_car.color = 'green'

print(one_car.current_speed, ' -> ', one_car.max_speed, ' -> ', one_car.color)
print(two_car.current_speed, ' -> ', two_car.max_speed, ' -> ', two_car.color)
print(three_car.current_speed, ' -> ', three_car.max_speed, ' -> ', three_car.color)
