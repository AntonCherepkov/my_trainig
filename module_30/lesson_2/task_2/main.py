class Person:
    def __init__(self, name: str, age: int, info: str) -> None:
        self._name = name
        self._age = age
        self.info = info

    
    @property
    def name(self):
        return self._name

    
    @name.setter
    def name(self, name):
        self._name = name


    @property
    def age(self):
        return self._age

    
    @age.setter
    def age(self, age):
        self._age = age


man_1 = Person(name='Anton', age=44, info='man')
man_2 = Person(name='Igor', age=67, info='man')
man_3 = Person(name='Irina', age=62, info='woman')

people_lst = [man_1, man_2, man_3]

sort_people_lst = sorted(people_lst, key=lambda man: man.age)

print(f'Это не сортированный список: ')
for man in people_lst:
    print(f'{man.name} -> {man.age}', end='\t')

print()

print(f'Это сортированный список: ')
for man in sort_people_lst:
    print(f'{man.name} -> {man.age}', end='\t')
