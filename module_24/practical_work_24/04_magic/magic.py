class Spell:
    dct_spell = {
        ('вода','огонь'): {
            'name': 'пар',
            'domage': 20,
            'type_domage': ['ожог']
            },
        ('вода','земля'): {
            'name': 'грязь',
            'domage': 5,
            'type_domage': ['замедление', 'удушье']
            },
        ('вода','воздух'): {
            'name': 'шторм',
            'domage': 10,
            'type_domage': ['замедление', 'удушье']
            },
        ('огонь','земля'): {
            'name': 'лава',
            'domage': 25,
            'type_domage': ['ожог', 'удушье']
            },
        ('огонь', 'воздух'): {
            'name': 'молния',
            'domage': 30,
            'type_domage': ['ожог']
            },
        ('земля', 'воздух'): {
            'name': 'пыль',
            'domage': 15,
            'type_domage': ['удушье']
            }
    }

    def __init__(self, composite_key):
        self.name = self.dct_spell[composite_key]['name']
        self.domage = self.dct_spell[composite_key]['domage']
        self.type_domage = self.dct_spell[composite_key]['type_domage']

    def show_info(self):        
        print('Заклинание: {}\nУрон от магии: {}'.format(
            self.name, self.domage)            
            )
        print('Тип воздействия:', end=' ')
        for imp in self.type_domage:
            print(imp, end=' ')
        print('\n')

    @classmethod
    def all_spells(self):
        for scroll, info_spell in self.dct_spell.items():
            print('Свитки, необходимые для сотворения заклинания:', end=' ')
            for elem in scroll:
                print(elem, end= ' ')
            print('\n\tЗаклинание: {}\n\tУрон от магии: {}'.format(
                info_spell['name'], info_spell['domage']
            ))
            print('\tТип воздействия:', end=' ')
            for imp in info_spell['type_domage']:
                print(imp, end=' ')
            print('\n')
                       

class MagicScroll:
    scrolls = {
        1: 'вода',
        2: 'огонь',
        3: 'земля',
        4: 'воздух',
    }

    def __init__(self, elem):
        if not isinstance(elem, int):
            raise TypeError('Значения должны быть целочисленными')
        elif 0 > elem or elem > 4:
            raise ValueError('Значения должны быть в интервале от 1 до 4')
        
        self.elem = elem
    
    def __add__(self, sub_elem):
        if not isinstance(sub_elem, MagicScroll):
            raise TypeError(f'Значение  {sub_elem} должно быть объектом класса MagicScroll')
        elif self.elem == sub_elem.elem:
            raise ValueError('Свитки должны быть различны')
        
        keys = sorted([k for k in self.scrolls.keys() if k == self.elem or k == sub_elem.elem])

        return Spell(tuple(self.scrolls[elem] for elem in keys))
