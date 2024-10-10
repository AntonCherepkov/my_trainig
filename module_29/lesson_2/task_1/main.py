from typing import Callable, Optional, Any
from functools import wraps


def call_multiplier(_func: Optional[Callable] = None, *, num_call: int = 1) -> Callable:
    def decorator_call(func: Callable) -> Callable:
        
        @wraps(func)
        def wrapped_call(*args, **kwargs) -> Any:
            result_list = []
            for _ in range(num_call):
                result = func(*args, **kwargs)
                result_list.append(result)
            
            return result_list
        return wrapped_call
    
    if _func is None:
        return decorator_call
    return decorator_call(_func)



@call_multiplier(num_call=5)
def mul_even_num(num):
    return sum([i ** 2 for i in range(num)])


result = mul_even_num(4)
print(result)
