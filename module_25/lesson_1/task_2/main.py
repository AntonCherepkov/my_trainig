class People:
    __count_man = 0

    def __init__(self, name, age):
        self.set_name(name)
        self.set_age(age)

        People.__count_man += 1

    def get_count(self):
        return self.__count_man

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_name(self, name):
        if all([isinstance(name, str), name.isalpha()]):
            self.__name = name
        else:
            raise TypeError('Имя должно быть строкой и не иметь цифр')

    def set_age(self, age):
        if isinstance(age, int):
            if age in range(1, 99):
                self.__age = age
            else:
                raise ValueError('Значение возраста должно быть в интервале от 1 до 99')
        else:
            raise TypeError('Значение должно быть целочисленным значением')

    def __str__(self):
        return f'Имя человека: {self.__name},\nВозвраст человека: {self.__age},\nКоличество людей: {self.__count_man}'


man_1 = People('Anton', 32)
print(man_1)

man_2 = People('Tatiana', 37)
print(man_2)

man_3 = People('Semen', 23)
print(man_3)
