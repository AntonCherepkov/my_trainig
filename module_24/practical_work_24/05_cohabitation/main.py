from random import randint
from class_home import Home
from class_man import Man


def logic_life(man_obj: Man):
    random_num = randint(1, 6)
    man_obj.is_check_satiety()

    if isinstance(man_obj, Man):
        if man_obj.degree_satiety < 20 or random_num == 2:
            print(f'   {man_obj.name}: хочет есть! (Сытость: {man_obj.degree_satiety})')
            man_obj.get_eats()
        elif man_obj.home.fridge < 10 and man_obj.age >= 18:
            print(f'   {man_obj.name}: заканчивается еда! (Запас еды: {man_obj.home.fridge})')
            man_obj.make_purchase()
        elif (man_obj.home.monay_storage < 50 or random_num == 1) and man_obj.age >= 18:
            print(f'   {man_obj.name}: есть необходимость поработать! (Запас денег: {man_obj.home.monay_storage})')
            man_obj.get_job_done()
        else:
            print(f'   {man_obj.name}: играет! (Запас еды: {man_obj.home.fridge})')
            man_obj.get_play()

    else:
        raise TypeError('The argument is not of the <class "Man">')
        

man = Man('Антон', 32)
woman = Man('Татьяна', 19, man.home)
children = Man('Дарья', 5, man.home)

for day in range(365):
    print(f'День -> {day+1}')
    logic_life(man)
    logic_life(woman)
    logic_life(children)

# зачет!
