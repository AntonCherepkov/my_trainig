from abc import ABC, abstractmethod


class Transport(ABC):
    """Базовый aбстрактный класс для всех транспортных средств"""
    def __init__(self, color, speed):
        self.color = color
        self.speed = speed


    @abstractmethod
    def movement(self):
        pass


    @abstractmethod
    def giving_signal(self):
        pass


class MusicMixin:
    """Класс-примесь, для обеспечения включения музыки в ТС"""
    __is_plays = False
    def turn_on_music(self):
        print('Наваливает музло!') if self.__is_plays else print('В салоне тишина!')


    def set_status_sound(self):
        self.__is_plays = not self.__is_plays


class Automobile(Transport, MusicMixin):
    """Класс автомобили"""
    def __init__(self, color, speed):
        super().__init__(color, speed)
        self.name = 'автомобиль'
        self.location_land = 'едет по дороге'


    def movement(self):
        transit_stack_movement = super().movement()
        return f'{self.color} {self.name} {self.location_land}, со скоростью {self.speed}', transit_stack_movement


    def giving_signal(self):
        transit_stack_giving = super().giving_signal()
        return f'{self.name} подаёт сигнал: БИ-БИ!!', transit_stack_giving


class Boat(Transport, MusicMixin):
    """Класс лодка"""
    def __init__(self, color, speed):
        super().__init__(color, speed)
        self.name = 'лодка'
        self.location_water = 'плывет по воде'


    def movement(self) -> str:
        return f'{self.color} {self.name} {self.location_water}, со скоростью {self.speed}'


    def giving_signal(self) -> str:
        return f'{self.name} подает сигнал: ДУ-ДУ!!'


class Amphibian(Automobile, Boat):
    def __init__(self, color, speed_land, speed_water):
        super().__init__(color, speed_land)
        self.name = 'амфибия'
        self.speed_water = speed_water


    def movement(self):
        return (f"{self.name} {self.location_water} co скоростью {self.speed_water}" +
                f" и {self.location_land} co скоростью {self.speed}")


    def giving_signal(self):
        return f"{self.name} подает сигнал и на суше и на воде!"


car = Automobile(color='Зеленый', speed=100)
boat = Boat(color='Синяя', speed=50)
amphibian = Amphibian(color='Желтая', speed_land=70, speed_water=30)

for transport in [car, boat, amphibian]:
    print(transport.movement())
    transport.turn_on_music()
    print(transport.giving_signal())
    print('Давай включим музыку?')
    transport.set_status_sound()
    transport.turn_on_music()
    print()
