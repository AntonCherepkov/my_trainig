from typing import Callable, Any, List
import functools

def decorator_question(function: Callable[[Any, ...], Any]) -> Callable[[Any, ...], Any]:
    """
    Навязчивый декоратор, который не позволит запустить переданную ему функцию, 
    пока пользователь не ответит на вопрос
    """
    @functools.wraps(function)
    def wrapped_func(*args: Any, **kwargs: Any) -> Any:
        print('Как дела?', end=' ')
        answer = input()
        print('А у меня не очень! Ладно, получай свою функцию:')
        if answer:
            result = function(*args, **kwargs)
        
        return result
    return wrapped_func


@decorator_question
def list_numbers_fib(number: int) -> List[int]:
    result_list = [0, 1]
    started_num = 0
    ended_num = 1

    for _ in range(number - 2):
        summ = started_num + ended_num
        result_list.append(summ)
        started_num = ended_num
        ended_num = summ
    
    return result_list


numbers_fib = list_numbers_fib(10)

print(f'This is test:\nРяд чисел Фиббоначи ->', end=' ')
for num in numbers_fib:
    print(num, end=' ')

print(f'\nОтработала функция: {list_numbers_fib.__name__}')
