import os
from contextlib import contextmanager
from collections.abc import Iterator 


@contextmanager
def in_dir(path: str) -> Iterator[str]:
    fst_dir = os.getcwd()
    print(f"Текущая директория: {fst_dir}")

    try:
        if not os.path.isdir(path):
            raise FileNotFoundError('Нет такой директории!')

        os.chdir(path)
        yield os.getcwd()

    except FileNotFoundError as exc:
        print(exc)

    finally:
        os.chdir(fst_dir)
        print("Директория после завершения: ", os.getcwd(), '\n')

 
path1 = os.path.abspath(os.path.join('..', '..', '..', 'module_28'))
path2 = os.path.abspath(os.path.join('not_dir')) 

with in_dir(path1) as next_dir:
    print("Измененная директория: ", next_dir)


with in_dir(path2) as next_dir:
    print("Измененная директория: ", next_dir)

