class Robot:
    def __init__(self, model):
        self.__model = model

    def operate(self):
        print('Робот выполняет следующие действия:')


class CleaningRobot(Robot):
    def __init__(self, model):
        super().__init__(model)
        self.fill_bag = 0

    def operate(self):
        print('Я собираю мусор!')
        self.fill_bag += 1
        print(f"Заполненность корзины: {self.fill_bag}")


class MilitaryRobot(Robot):
    def __init__(self, model, gun):
        super().__init__(model)
        self.__gun = gun

    def operate(self):
        print(f'Охраняю объект при помощи {self.__gun}!')


class UnderwaterMilitaryRobot(MilitaryRobot):
    def __init__(self, model, gun):
        super().__init__(model, gun)
        self.depth_immertion = 0

    def operate(self):
        super().operate()
        print('Не просто охраняю, а под водой!')


cleaning_android = CleaningRobot('C3PO')
cleaning_android.operate()

military_android = MilitaryRobot('T101', 'Плазмомёт')
military_android.operate()

underwater_android = UnderwaterMilitaryRobot('T102W', 'Стреломет')
underwater_android.operate()
