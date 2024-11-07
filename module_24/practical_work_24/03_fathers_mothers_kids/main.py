from random import getrandbits
from my_error import AgeError

class Child:
    state_hunger = {
        0: 'не голоден',
        1: 'немного голоден',
        2: 'чувствительно голоден',
        3: 'сильно голоден',
        4: 'нестерпимо голоден'
    }
    state_calm = True

    def __init__(self, name, age, hp=0):
        self.name_child = name
        self.age_child = age

        self.hunger_point = hp
        self.state_calm = True

    def progress_state(self):
        if self.hunger_point < 4:
            self.hunger_point += 1
        if bool(getrandbits(1)):
            print(f'{self.name_child} неожиданно заплакал!')
            self.state_calm = False
        elif self.hunger_point > 3:
            print(f'{self.name_child} проголодался и заплакал!')
            self.state_calm = False

class Parent:
    def __init__(self, name, age, children=None):
        self.name = name
        self.age = age
        self.lst_children = []

        for child_info in children:
            if len(child_info) == 3:
                state_hungre = child_info[2]
            try:            
                if (self.age - child_info[1]) < 16:
                    raise AgeError(f'Родитель не может быть старше ребенка на {self.age - child_info[1]} лет!')
                self.lst_children.append(Child(*child_info))
            except AgeError as exc:
                self.lst_children.append(None)

    def show_family(self):
        print('Родитель: {}\nВозраст {}: {}'.format(
            self.name, self.name, self.age)
            )

        print('Дети:') if self.lst_children else print('Детей нет!')

        for child in self.lst_children:
            if child is None:
                print('   ####Исключено####\n')
            else:
                print('   Имя: {}\n   Возраст: {}\n   Ребёнок {}\n'.format(
                    child.name_child, child.age_child, child.state_hunger[child.hunger_point]
                ))

    def work_with_child(self):
        for child in self.lst_children:
            if isinstance(child, Child):
                child.progress_state()
                if not child.state_calm:
                    if child.hunger_point >= 3:
                        child.hunger_point = 0
                        print(f'{self.name} покормил {child.name_child}')
                    child.state_calm = True
                    print(f'{self.name} успокоил {child.name_child}')
                print()

#Test
lst_child = [
    ('Dasha', 5),
    ('Alena', 3, 1),
    ('Misha', 18),
    ('Evgenia', 1, 4),
    ('Marishka', 7, 3)
]

father = Parent(name='Anton', age=32, children=lst_child)
father.show_family()
print('-' * 30)

for _ in range(8):
    father.work_with_child()
    father.show_family()
    print('-' * 30)

# зачет!
