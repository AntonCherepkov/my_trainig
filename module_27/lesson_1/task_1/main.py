from typing import Callable

def first_order_func(number: int) -> int:
    return number + 10

def higher_order_func(func: Callable[[int], int], number: int) -> int:
    return func(number) * func(number)


print(higher_order_func(first_order_func, 9))
