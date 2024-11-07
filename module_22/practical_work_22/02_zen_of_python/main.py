import os

work_dir = os.path.abspath(os.getcwd())
path_file = os.path.join(work_dir, 'zen.txt')

file_zen = open(path_file, 'r')

list_zen = []
list_zen.extend(file_zen)
for line in range(len(list_zen)-1, 0, -1):
    print(list_zen[line], end='')

file_zen.close()

print()