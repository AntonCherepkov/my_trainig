import os
from gen_func import gen_file_path


address_files = gen_file_path(key='Module')
for address in address_files:
    print(address)

print(gen_file_path.__doc__)
