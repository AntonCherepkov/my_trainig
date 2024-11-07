import random
from monsters import MonsterHunter


class Hero:
    # Базовый класс, который не подлежит изменению
    # У каждого наследника будут атрибуты:
    # - Имя
    # - Здоровье
    # - Сила
    # - Жив ли объект
    # Каждый наследник будет уметь:
    # - Атаковать
    # - Получать урон
    # - Выбирать действие для выполнения
    # - Описывать своё состояние

    max_hp = 150
    start_power = 10

    def __init__(self, name):
        self.name = name
        self.__hp = self.max_hp
        self.__power = self.start_power
        self.__is_alive = True

    def get_hp(self):
        return self.__hp

    def set_hp(self, new_value):
        self.__hp = max(new_value, 0)

    def get_power(self):
        return self.__power

    def set_power(self, new_power):
        self.__power = new_power

    def is_alive(self):
        return self.__is_alive

    # Все наследники должны будут переопределять каждый метод базового класса (кроме геттеров/сеттеров)
    # Переопределенные методы должны вызывать методы базового класса (при помощи super).
    # Методы attack и __str__ базового класса можно не вызывать (т.к. в них нету кода).
    # Они нужны исключительно для наглядности.
    # Метод make_a_move базового класса могут вызывать только герои, не монстры.
    def attack(self, target):
        # Каждый наследник будет наносить урон согласно правилам своего класса
        raise NotImplementedError("Вы забыли переопределить метод Attack!")

    def take_damage(self, damage):
        # Каждый наследник будет получать урон согласно правилам своего класса
        # При этом у всех наследников есть общая логика, которая определяет жив ли объект.
        print("\t", self.name, "Получил удар с силой равной = ", round(damage), ". Осталось здоровья - ", round(self.get_hp()))
        # Дополнительные принты помогут вам внимательнее следить за боем и изменять стратегию, чтобы улучшить выживаемость героев
        if self.get_hp() <= 0:
            self.__is_alive = False

    def make_a_move(self, friends, enemies):
        # С каждым днём герои становятся всё сильнее.
        self.set_power(self.get_power() + 0.1)

    def __str__(self):
        # Каждый наследник должен выводить информацию о своём состоянии, чтобы вы могли отслеживать ход сражения
        raise NotImplementedError("Вы забыли переопределить метод __str__!")


class Healer(Hero):
    # Целитель:
    # Атрибуты:
    # - магическая сила - равна значению НАЧАЛЬНОГО показателя силы умноженному на 3 (self.__power * 3)
    # Методы:
    # - атака - может атаковать врага, но атакует только в половину силы self.__power
    # - получение урона - т.к. защита целителя слаба - он получает на 20% больше урона (1.2 * damage)
    # - исцеление - увеличивает здоровье цели на величину равную своей магической силе
    # - выбор действия - получает на вход всех союзников и всех врагов и на основе своей стратегии выполняет ОДНО из действий (атака,
    # исцеление) на выбранную им цель
    def __init__(self, name):
        super().__init__(name)
        self.__magic_force = self.get_power() * 3

    def attack(self, target):
        target.take_damage(self.get_power() / 2)

    def take_damage(self, damage):
        new_hp = self.get_hp() - (1.2 * damage)
        self.set_hp(new_value=new_hp)
        super().take_damage(damage)

    def heal(self, ally):
        ally.set_hp(ally.get_hp() + self.__magic_force)
        if ally.get_hp() > ally.max_hp:
            ally.set_hp(ally.max_hp)

    def make_a_move(self, friends, enemies):
        list_wounded = [hero for hero in friends if hero.get_hp() < hero.max_hp * 0.75]
        if list_wounded:
            most_critical = list_wounded[0]
            for i in range(1, len(list_wounded), 1):
                if list_wounded[i].get_hp() < list_wounded[i-1].get_hp():
                    most_critical = list_wounded[i]
            print('{0} лечит самого раненного - {1} -> hp[{2}] + {3}'.format(
                self.name, most_critical.name, most_critical.get_hp(), self.__magic_force
            ))
            self.heal(most_critical)
        else:
            target = random.choice(enemies)
            print(f'{self.name} атакует {target.name}')
            self.attack(target)

    def __str__(self):
        return 'Name: {0} | HP: {1}'.format(self.name, self.get_hp())

class Tank(Hero):
    # Танк:
    # Атрибуты:
    # - показатель защиты - изначально равен 1, может увеличиваться и уменьшаться
    # - поднят ли щит - танк может поднимать щит, этот атрибут должен показывать поднят ли щит в данный момент
    # Методы:
    # - атака - атакует, но т.к. доспехи очень тяжелые - наносит половину урона (self.__power)
    # - получение урона - весь входящий урон делится на показатель защиты (damage/self.defense) и только потом отнимается от здоровья
    # - поднять щит - если щит не поднят - поднимает щит. Это увеличивает показатель брони в 2 раза, но уменьшает показатель силы в 2 раза.
    # - опустить щит - если щит поднят - опускает щит. Это уменьшает показатель брони в 2 раза, но увеличивает показатель силы в 2 раза.
    # - выбор действия - получает на вход всех союзников и всех врагов и на основе своей стратегии выполняет ОДНО из действий (атака,
    # поднять щит/опустить щит) на выбранную им цель
    def __init__(self, name):
        super().__init__(name)
        self.is_raising_shield = False
        self.defence = 1
        self.fatigue_count = 0

    def attack(self, target):
        target.take_damage(self.get_power() / 2)

    def take_damage(self, damage):
        result_damage = damage / self.defence
        new_hp = self.get_hp() - result_damage
        self.set_hp(new_value=new_hp)
        super().take_damage(result_damage)

    def up_shield(self):
        if not self.is_raising_shield:
            self.set_power(self.get_power() / 2)
            self.defence *= 2
            self.is_raising_shield = True
            print(f'{self.name} поднял щит!')
        else:
            print('Щит уже поднят!')

    def lower_shield(self):
        if self.is_raising_shield:
            self.set_power(self.get_power() * 2)
            self.defence /= 2
            self.is_raising_shield = False
            print(f'{self.name} устал держать щит, и опустил его!')
        else:
            print('Щит уже опущен!')

    def change_fatigue(self):
        if self.is_raising_shield:
            self.fatigue_count += 1
        else:
            if self.fatigue_count > 0:
                self.fatigue_count -= 1

    def check_fatigue(self):
        return self.is_raising_shield and self.fatigue_count >= 10

    def make_a_move(self, friends, enemies):
        self.change_fatigue()
        if self.check_fatigue():
            self.lower_shield()
            return
        else:
            if random.randint(1, 3) == 1:
                self.up_shield()
            else:
                print(f'{self.name} атакует ближайшего сопернника: {enemies[0]}')
                self.attack(enemies[0])

    def __str__(self):
        return 'Name: {0} | HP: {1}'.format(self.name, self.get_hp())

class Attacker(Hero):
    # Убийца:
    # Атрибуты:
    # - коэффициент усиления урона (входящего и исходящего)
    # Методы:
    # - атака - наносит урон равный показателю силы (self.__power) умноженному на коэффициент усиления урона (self.power_multiply)
    # после нанесения урона - вызывается метод ослабления power_down.
    # - получение урона - получает урон равный входящему урона умноженному на половину коэффициента усиления урона - damage * (
    # self.power_multiply / 2)
    # - усиление (power_up) - увеличивает коэффициента усиления урона в 2 раза
    # - ослабление (power_down) - уменьшает коэффициента усиления урона в 2 раза
    # - выбор действия - получает на вход всех союзников и всех врагов и на основе своей стратегии выполняет ОДНО из действий (атака,
    # усиление, ослабление) на выбранную им цель
    def __init__(self, name):
        super().__init__(name)
        self.gain_factor = 0.5

    def attack(self, target):
        target.take_damage(self.get_power() + self.get_power() * 0.5)
        self.power_down()

    def take_damage(self, damage):
        self.set_hp(self.get_hp() - damage * (self.gain_factor / 2))

    def power_up(self):
        self.gain_factor *= 2

    def power_down(self):
        self.gain_factor /= 2

    def check_gain_factor(self):
        if self.gain_factor <= 0:
            return False
        else:
            return True

    def make_a_move(self, friends, enemies):
        if self.check_gain_factor():
            if self.gain_factor >= 1:
                victim = random.choice(enemies)
                print(f'У {self.name} переизбыток сил и он решает атаковать {victim.name}!')
                self.attack(victim)
            elif self.get_hp() < self.max_hp / 2:
                print(f'У {self.name} тяжелое ранение, и он из последних сил атакует ближайшего врага: {enemies[0]}!')
                self.attack(enemies[0])
            else:
                for victim in enemies:
                    if isinstance(victim, MonsterHunter):
                        print(f'{self.name} видит благоприятные условия для атаки на хилера: {victim}!')
                        self.attack(victim)
                else:
                    victim = random.choice(enemies)
                    print(f'{self.name} не находит хилера в стане врага, и атакует случайного: {victim}!')
                    self.attack(victim)
        else:
            print(f'У {self.name} нет сил, и он решает подготовиться для следующей атаки!')
            self.power_up()

    def __str__(self):
        return 'Name: {0} | HP: {1}'.format(self.name, self.get_hp())
