from random import randint
from my_error import AccidentalException

sum_num = 0
with open('out_file.txt', 'a', encoding='utf-8') as out_file:
    try:
        while True:
            # TODO лучше сделать проверку на число, чем отлавливать исключение
            in_num = input('Введите число: ')
            if in_num.isdigit():
                in_num = int(in_num)
                sum_num += in_num
                out_file.write(str(in_num) + '\n')
                if randint(1, 13) == 1:
                    raise AccidentalException
                if sum_num >= 777:
                    break
            else:
                print('Необходимо ввести число!')

    except AccidentalException as exc:
        print('Вы потерпели неудачу...')
        out_file.write(
            'Вы втретились со случайным исключением!'
            )
        raise

    else:
        print('Вы успешно выполнили поставленные условия!')
        out_file.write(
            'Сумма введенных чисел: '
            + str(sum_num)
            + '\nВы достигли поставленной задачи!'
        )

# зачет!
