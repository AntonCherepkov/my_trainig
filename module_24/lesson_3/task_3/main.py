class Potato:
    level_dict = {
        0: 'отсутствует',
        1: 'росток',
        2: 'зелёная',
        3: 'зрелая'
    }

    def __init__(self, index):
        self.index = index
        self.level = 0
    
    def print_potato_info(self):
        print('Картошка {} сейчас {}'.format(
            self.index, Potato.level_dict[self.level]
        ))
    
    def grow(self):
        if self.level < 3:
            self.level += 1
        self.print_potato_info()
        
    def is_readiness(self):
        if self.level == 3:
            return True
        return False    

class PotatoGarden:
    def __init__(self, num):
        self.lst_potatoes = [Potato(index) for index in range(1, num + 1)]

    def total_grow(self):
        print('Картошка прорастает!')
        for i_potato in self.lst_potatoes:
            i_potato.grow()

    def control_readliness(self):
        if not all([i_potato.is_readiness() for i_potato in self.lst_potatoes]):
            print('Картошка не созрела!')
        else:
            print('Картошка созрела! Можно собирать!')
        

first_garden = PotatoGarden(5)
first_garden.control_readliness()
for _ in range(3):
    first_garden.total_grow()
    first_garden.control_readliness()
