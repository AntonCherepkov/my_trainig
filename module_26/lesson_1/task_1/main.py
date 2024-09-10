from collections.abc import Iterable


def iterate(user_obj):
    if isinstance(user_obj, Iterable):
        my_iterator = iter(user_obj)
        while True:
            try:
                print(next(my_iterator))
            except StopIteration:
                print('End on iteration')
                break
    else:
        print('Object is not iterable')


iterate([34, 56, 23])
iterate({1: 'a', 2: 'b', 3: 'c'})
iterate('abcdf')
iterate((1, 2, 3))
iterate(47)