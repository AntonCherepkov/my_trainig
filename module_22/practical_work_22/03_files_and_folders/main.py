import os

def info_dirictory(root_dir, size_dir=0, count_file=0, count_dir=0):
    for i_file in os.listdir(root_dir):
        new_dir = os.path.join(root_dir, i_file)

        if os.path.isfile(new_dir):
            size_dir += os.path.getsize(new_dir)
            count_file += 1

        elif os.path.isdir(new_dir):
            count_dir += 1
            size_dir, count_file, count_dir = info_dirictory(
                new_dir, size_dir, count_file, count_dir
            )            
    else:        
        return (size_dir, count_file, count_dir)


work_dir = os.path.abspath(os.path.join('..', '..'))
print('Вывод информации по директории:\n', work_dir)

size, files, subdir = info_dirictory(work_dir)
size = (size/1024)

print(
    'Размер каталога: {:f} кБ\n'
    'Количество подкаталогов: {:d}\n'
    'Количество файлов: {:d}'.format(
        size,
        subdir,
        files
    )
)

print()