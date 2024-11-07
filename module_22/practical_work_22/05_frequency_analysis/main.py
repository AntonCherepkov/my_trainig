import os
from os import path


def create_dict(list_text):
    return {
        symbol: sum(
            1 for c_symbol in list_text
            if (symbol == c_symbol)
        )
        for symbol in list_text
        if (96 < ord(symbol) < 123)
    }


work_path = path.abspath(os.getcwd())
in_file_path = path.join(work_path, 'text.txt')
out_file_path = path.join(work_path, 'analysis.txt')

in_file_obj = open(in_file_path, 'r')

text_from_file = in_file_obj.read()

dict_symbol_count = create_dict(text_from_file)
dict_symbol_count = dict(sorted(
    dict_symbol_count.items(), key=lambda item: item[1], reverse=True))

long_text = len(text_from_file)

out_file_obj = open(out_file_path, 'w')
for symbol, count in dict_symbol_count.items():
    out_file_obj.write(
        symbol
        + '  '
        + str(round((count / long_text * 100), 3))
        + '\n'
    )

out_file_obj.close()
in_file_obj.close()

print()