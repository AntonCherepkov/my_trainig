from random import randint


class Warrior:
    def __init__(self, name):
        self.name = name
        self.health = 100
    
    def show_stat(self):
        print('Имя война: {}\nЗдоровье {}: {}'.format(
            self.name, self.name, self.health
        ))

    def is_check_health(self):
        if self.health == 0:
            return False
        return True
    
class Battle:
    def __init__(self, *name):
        self.warriors = {num: Warrior(name) for num, name in enumerate(name)}
    
    def show_all_warriors(self):
        for index, name in self.warriors.items():
            name.show_stat()
    
    def find_defender(self, exc):
        while True:
            defender = randint(0, len(self.warriors) - 1)
            if defender != exc:
                return defender

    def completion_control(self):
        if not all([warrior.is_check_health() for warrior in self.warriors.values()]):
            print('\nБитва завершена!')
        else:
            self.start_fight()

    def start_fight(self):
        i_off = randint(0, len(self.warriors) - 1)
        i_def = self.find_defender(i_off)

        striker = self.warriors[i_off]
        defender = self.warriors[i_def]

        print(f'\n{striker.name} атакует {defender.name}')
        defender.health -= 20
        print(f'Остаток здоровья {defender.name}: {defender.health}')
        
        self.completion_control()


first_fight = Battle('Subzero', 'Scorpio')
first_fight.show_all_warriors()
first_fight.start_fight()

# зачет!
