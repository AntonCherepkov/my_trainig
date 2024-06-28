class Soda:
    supp_dict = {
        1: 'Тархун',
        2: 'Колла',
        3: 'Байкал'
    }

    def __init__(self, supplement=None):
        self.supplement = supplement
    
    def show_soda(self):
        if self.supplement in Soda.supp_dict:
            print(f'Газировка - {Soda.supp_dict[self.supplement]}')
        else:
            print('Это обычная газировка!')


first_soda = Soda()
second_soda = Soda(2)

first_soda.show_soda()
second_soda.show_soda()
