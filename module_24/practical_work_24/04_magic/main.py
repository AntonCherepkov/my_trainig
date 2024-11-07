import magic
import weapon
import math


class WarriorWitcher:
    total_domage = 0

    def __init__(self, weap=1, scroll_1=3, scroll_2=2):
        self.weapon_war = weapon.Weapon(weap)
        self.scroll_1 = magic.MagicScroll(scroll_1)
        self.scroll_2 = magic.MagicScroll(scroll_2)
        self.magic_strike = self.scroll_1 + self.scroll_2
        self.total_domage = self.calc_domage()

    def calc_domage(self):
        boost = math.ceil(self.magic_strike.domage / 100 * self.weapon_war.streng_magic)
        return self.magic_strike.domage + boost + self.weapon_war.domage
    
    def show_info(self):
        print(f'Суммарный урон война: {self.total_domage}')
        print(f'-> оружием {self.weapon_war.name}: {self.weapon_war.domage}')
        print(f'-> заклинанием {self.magic_strike.name}: {self.magic_strike.domage}')
        print(f'-> увеличение урона из за характеристик {self.weapon_war.name}:'
              f' {self.total_domage - self.weapon_war.domage - self.magic_strike.domage}')

warrior = WarriorWitcher()
print(warrior.show_info())
