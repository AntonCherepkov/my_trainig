import os
from errors import *
from carma import Carma


my_carma = Carma()
count_days = 0

path_file = os.path.abspath(os.path.join('logs.txt'))
with open(path_file, 'w', encoding='utf-8') as log_file:
    while True:
        count_days += 1
        my_carma.add_carma()
        check_carma = my_carma.check_carma()
        if isinstance(check_carma, AllErrors):
            log_file.write(
                f'День {str(count_days)}: нас постигла неудача {check_carma}\n'
            )
        elif check_carma:
            log_file.write('Мы добились успеха и достигли просветления!')
            break
        else:
            log_file.write(
                f'День {str(count_days)}: карма {my_carma.current_carma}\n'
            )
