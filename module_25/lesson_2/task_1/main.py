class Ship:
    def __init__(self, model):
        self.__model = model

    def sail_ship(self):
        print('Корабль куда то поплыл!')

    def __str__(self):
        return f"Модель корабля: {self.__model}"

class WarShip(Ship):
    def __init__(self, model, gun):
        self.__gun = gun
        super().__init__(model)

    def attack(self):
        print(f'Корабль открыл огонь {self.__gun}')

class CargoShip(Ship):
    def __init__(self, model):
        self.load_tonnage = 0
        super().__init__(model)

    def load_ship(self):
        if self.load_tonnage < 10:
            print('Начинаем загрузку корабля!')
            self.load_tonnage += 1
        else:
            print('Корабль уже полностью загружен')
        print(f'Сейчас загруженность корабля сотсавляет: {self.load_tonnage}')

    def unload_ships(self):
        if self.load_tonnage > 0:
            print('Начинаем разгрузку')
            self.load_tonnage -= 1
        else:
            print('На корабле нет никакого груза!')
        print(f'Сейчас загруженность корабля сотсавляет: {self.load_tonnage}')


cargo_ship = CargoShip('Баржа')
print(cargo_ship)
cargo_ship.load_ship()

war_ship = WarShip('Линкор', 'Ракета Калибр')
print(war_ship)
war_ship.attack()
