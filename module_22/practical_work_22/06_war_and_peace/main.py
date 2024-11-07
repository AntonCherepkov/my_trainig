import os, zipfile, math


def dict_count_character(in_str):
    dict_stat = dict()
    for char in in_str:
        if char.isalpha():
            if char in dict_stat:
                dict_stat[char] += 1
            else:
                dict_stat[char] = 1
    return dict_stat


def write_file(in_dict, out_file, rows=20):
    col = math.ceil(len(in_dict) / rows)
    array = [['' for _ in range(col)] for _ in range(rows)]

    for i, key in enumerate(in_dict):
        row = i % rows
        col = i // rows
        array[row][col] = str(key) + ': ' + str(in_dict[key])

    for row in array:
        out_file.write(
            '  '.join(row)
            + '\n'
        )


file_name = str()
wim_zip = zipfile.ZipFile('voina-i-mir.zip', 'r')
for name in wim_zip.namelist():
    if name.endswith('.txt'):
        file_name = name
        wim_zip.extract(file_name)
        break
else:
    print('Архив не содержит текстовых файлов.')

wim_zip.close()

path_file = os.path.abspath(os.path.join(os.getcwd(), file_name))
print('Путь к файлу: ', path_file)

book_file = open(path_file, 'r', encoding='utf-8')
str_file = book_file.read()
book_file.close()

statistic_dict = dict_count_character(str_file)
statistic_dict = dict(sorted(statistic_dict.items(), key=lambda item: item[1], reverse=True))

path_file = os.path.abspath(os.path.join(os.getcwd(), 'analysis.txt'))
analysis_file = open(path_file, 'w', encoding='utf-8')

write_file(statistic_dict, analysis_file)

print()
