from abc import ABC, abstractmethod
from typing import Union, Optional


class Transport(ABC):
    """Базовый абстрактный класс, являющийся интерфейсом для автопарка"""
    def __init__(self, color: str, speed: Union[int, float]) -> None:
        self._color = color
        self._speed = speed
        self.name: Optional[str] = None
    

    @property
    def color(self) -> str:
        return self._color

    
    @color.setter
    def color(self, color) -> None:
        self._color = color

    
    @property
    def speed(self) -> Union[int, float]:
        return self._speed

    
    @speed.setter
    def speed(self, speed) -> None:
        self._speed = speed

    
    @abstractmethod
    def give_signal(self) -> None:
        pass


    def __str__(self) -> str:
        return (
            '{:s} имеет следующие характеристики:'
            '\n\tЦвет: {:s}'
            '\n\tМаксимальная скорость: {:d}'.format(
                self.name, self.color, self.speed
            ))


class MusicMixin:
    """Класс-примесь для проигрывания музыки!"""
    def play_music(self):
        print(
            'Надо мною тишина!\n'
            'Небо полное огня!\n'
            'Свет проходит сквозь меня!\n'
            'И я свободен вновь...\n'
        )


class Car(Transport, MusicMixin):
    """Класс, который описывает поведение автомобиля"""
    def __init__(self, color: str, speed: Union[int, float]) -> None:
        super().__init__(color=color, speed=speed)
        self.name = 'автомобиль'
        self.earth_location = 'ездит по земле'

    
    def give_signal(self) -> None:
        print('Би-би')


    def __str__(self) -> str:
        base_str = super().__str__()
        return base_str + f'\n\tНазначение: {self.earth_location}'


class Boat(Transport, MusicMixin):
    """Класс, описывающий поведение плав-средств"""  
    def __init__(self, color: str, speed: Union[int, float]) -> None:
        super().__init__(color=color, speed=speed)
        self.name = 'лодка'
        self.water_location = 'плавает по воде'


    def give_signal(self) -> None:
        print('Ду-ду')


    def __str__(self) -> str:
        base_str = super().__str__()
        return base_str + f'\n\tНазначение: {self.water_location}'


class Amphibian(Car, Boat):
    """Класс, описывающий поведение машин-амфибий"""
    def __init__(self, color: str, speed: Union[int, float]) -> None:
        super().__init__(color=color, speed=speed)
        self.name = 'амфибия'


    def give_signal(self) -> None:
        print('Ду-дуууу!')


    def __str__(self):
        base_str = super().__str__()
        return base_str + f' и {self.water_location}'


car = Car(color='зеленая', speed=120)
print(car)
print('Перекрашиваем автомобиль!')
car.color = 'синяя'
print(car)

print()

boat = Boat(color='красная', speed=50)
print(boat)
print('Перекрашиваем лодку!')
boat.color = 'малиновая'
print(boat)

print()

amphibian = Amphibian(color='серая', speed=70)
print(amphibian)
print('Качаем двигло!')
amphibian.speed = 80
print(amphibian)
