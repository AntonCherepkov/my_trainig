import os

def summ_number(file_obj):
    summ = 0
    for i_line in file_obj:
        for i_elem in i_line.split():
            if i_elem.isdigit():
                summ += int(i_elem)
    return str(summ)


def gen_summ(file_obj):
    return str(sum(int(i_elem) for i_line in file_obj
                for i_elem in i_line.split() if i_elem.isdigit()))


work_dir = os.path.abspath(os.getcwd())
print(work_dir)

in_file_1 = open(os.path.join(work_dir, 'numbers.txt'), 'r', encoding='utf-8')
summ_1 = summ_number(in_file_1)

in_file_2 = open(os.path.join(work_dir, 'numbers.txt'), 'r', encoding='utf-8')
summ_2 = gen_summ(in_file_2)

in_file_1.close()
in_file_2.close()

out_file = open(os.path.join(work_dir, 'answer.txt'), 'w', encoding='utf-8')
out_file.write(
    'Сумма, подсчитанная функцией summ_number(): '
    + summ_1
    + '\nСумма, подсчитанная функцией gen_summ(): '
    + summ_2
)
out_file.close()

print()