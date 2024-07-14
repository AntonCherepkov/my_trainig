class UnitNPC:
    def __init__(self):
        self.__health_points = 100

    def damage_health(self, damage=0):
        self.__health_points -= damage

    def get_health(self):
        return self.__health_points

    def __str__(self):
        return f'{self.__class__.__name__} имеет здоровья: {self.__health_points}'


class Warrior(UnitNPC):
    def __init__(self, name):
        super().__init__()
        self.__call_sign = name

    def damage_health(self, damage=0):
        super().damage_health(damage)

    def get_health(self):
        return super().get_health()

    def __str__(self):
        info = ' '.join([self.__call_sign, super().__str__().lstrip(str(self.__class__.__name__))])

        return '\n'.join(
            (
                info,
                f'Урон по войну: {self.__call_sign}\n'
            )
        )


class Citizen(UnitNPC):
    def __init__(self, name):
        super().__init__()
        self.__name = name

    def damage_health(self, damage=0):
        new_damage = damage * 2
        super().damage_health(damage=new_damage)

    def __str__(self):
        info = ' '.join([self.__name, super().__str__().lstrip(str(self.__class__.__name__))])

        return '\n'.join(
            (
                info,
                f'Урон по гражданину: {self.__name}\n'
            )
        )


npc = UnitNPC()
print(npc)

warrior = Warrior('Artur')
print(warrior)
warrior.damage_health(20)
print(warrior)

citizen = Citizen('Dmitriy')
print(citizen)
citizen.damage_health(20)
print(citizen)
