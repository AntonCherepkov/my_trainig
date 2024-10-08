import time
from contextlib import contextmanager

@contextmanager
def timer() -> None:
    start = time.perf_counter()
    yield
    run_time = (time.perf_counter() - start)
    print(f'Время работы кода: {run_time}')


def my_summ(num=5):
    return sum(i for i in range(num))


with timer() as t1:
    print(my_summ())
