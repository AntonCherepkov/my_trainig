class Spell:
    dct_spell = {
        ('вода', 'огонь'): 'пар',
        ('вода', 'земля'): 'грязь',
        ('вода', 'воздух'): 'шторм',
        ('земля', 'огонь'): 'лава',
        ('воздух', 'огонь'): 'молния',
        ('воздух', 'земля'): 'пыль'
    }

    def __init__(self, tuple_elements):
        self.name = self.dct_spell[tuple_elements]

class ElementWater:
    def __init__(self):
        self.name = 'вода'

    def __add__(self, sec_element):
        try:
            if isinstance(sec_element, (ElementFire, ElementEarth, ElementWind)):
                composite = tuple(sorted([self.name, sec_element.name]))
                return Spell(composite)
            else:
                raise TypeError('Не верный тип данных!')
        except TypeError as te:
            print('Error: ', te)
            return None


class ElementFire:
    def __init__(self):
        self.name = 'огонь'

    def __add__(self, sec_element):
        try:
            if isinstance(sec_element, (ElementWater, ElementEarth, ElementWind)):
                composite = tuple(sorted([self.name, sec_element.name]))
                return Spell(composite)
            else:
                raise TypeError('Не верный тип данных!')
        except TypeError as te:
            print('Error: ', te)
            return None

class ElementEarth:
    def __init__(self):
        self.name = 'земля'

    def __add__(self, sec_element):
        try:
            if isinstance(sec_element, (ElementFire, ElementWater, ElementWind)):
                composite = tuple(sorted([self.name, sec_element.name]))
                return Spell(composite)
            else:
                raise TypeError('Не верный тип данных!')
        except TypeError as te:
            print('Error: ', te)
            return None

class ElementWind:
    def __init__(self):
        self.name = 'воздух'

    def __add__(self, sec_element):
        try:
            if isinstance(sec_element, (ElementFire, ElementEarth, ElementWater)):
                composite = tuple(sorted([self.name, sec_element.name]))
                return Spell(composite)
            else:
                raise TypeError('Не верный тип данных!')
        except TypeError as te:
            print('Error: ', te)
            return None


water = ElementWater()
fire = ElementFire()
earth = ElementEarth()
wind = ElementWind()

spell_1 = water + fire
print(spell_1.name)

spell_2 = fire + earth
print(spell_2.name)

spell_3 = earth + water
print(spell_3.name)
