from abc import ABC, abstractmethod

class Robot:
    def __init__(self, model, *args, **kwargs):
        self.model = model
        super().__init__(*args, **kwargs)
        
    def __str__(self):
        skill = super().__str__()
        return 'Я - робот!'+ " " + skill

    @abstractmethod
    def operate(self):
        pass


class CanFly:
    def __init__(self):
        self.height = 0
        self.speed = 0

    def takeoff(self, value: int):
        """Метод, отвечающий за взлёт"""
        self.height += value

    def flight(self):
        """Метод, отвечающий за полёт"""
        self.speed = int(input('С какой скоростью двигаться?'))
        return self.speed

    def landing(self):
        """Метод, отвечающий за посадку"""
        self.height = 0

    def __str__(self):
        return 'Умею летать!'


class Scout(Robot, CanFly):
    def __init__(self, model):
        super().__init__(model)

    def __str__(self):
        robot_str = super().__str__()
        return robot_str + ' Еще и разведчик!'

    def operate(self):
        """Метод для команды разведчику к осмотру местности!"""
        print('Приступаю к разведке местности!')
        if self.height == 0:
            new_height = int(input('На какую высоту поднять дрон?: '))
            self.takeoff(new_height)
        distance = self.flight()
        print(f'Целый час кружил, пролетел {distance} км!')
        print('Иду на посадку!')
        self.landing()


class CombatRobot(Robot, CanFly):
    def __init__(self, model, weapon):
        super().__init__(model)
        self.weapon = weapon

    def __str__(self):
        robot_str = super().__str__()
        return robot_str + ' Еще и боец!'

    def operate(self):
        print(f'Я защищаю Вас! Есть крутые {self.weapon}')


robot_scout_01 = Scout(model='r2d2')
print(robot_scout_01, robot_scout_01.model)
robot_scout_01.operate()

robot_terminator = CombatRobot(model='c3po', weapon='пушки')
print(robot_terminator, robot_terminator.model)
robot_terminator.operate()

print(robot_scout_01.__class__.__mro__)
print(robot_terminator.__class__.__mro__)
