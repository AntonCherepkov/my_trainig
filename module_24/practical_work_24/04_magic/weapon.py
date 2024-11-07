class Weapon:
    dict_weapon = {
        0: {
            'name': 'двуручный меч',
            'damage': 20,
            'streng_magic': 15
            },
        1: {
            'name': 'охотничий лук',
            'damage': 15,
            'streng_magic': 20
            },
        2: {
            'name': 'топор севера',
            'damage': 30,
            'streng_magic': 5
            },
        3: {
            'name': 'булава гномов',
            'damage': 25,
            'streng_magic': 10}
    }

    def __init__(self, weapon):
        self.name = self.dict_weapon[weapon]["name"]
        self.domage = self.dict_weapon[weapon]["damage"]
        self.streng_magic = self.dict_weapon[weapon]["streng_magic"]

    def show_info(self):
        print('Название оружия: {}\nФизический урон оружием: {}\nБонус к магии: {}\n'.format(
            self.name, self.domage, self.streng_magic)
        )

    @classmethod
    def all_weapon(self):
        print('Оружие, доступное для использования:')
        for info_weapon in self.dict_weapon.values():
            print('\tНазвание оружия: {}\n\tФизический урон оружием: {}\n\tБонус к магии: {}\n'.format(
                info_weapon['name'], info_weapon['damage'], info_weapon['streng_magic'])   
            )
