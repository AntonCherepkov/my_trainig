from count_func import my_gen_count


for path_file, num_lines in my_gen_count():
    print('В python файле, размещенном в директории: {:s}' 
          '\nИмеется {:d} не пустых строк'.format(
        path_file,
        num_lines
    ))
