from typing import List, Tuple, Any


def zipper(lst_a: List[Any], lst_b: List[Any], limit: bool = False) -> List[Tuple[Any, ...]]:
    """
    zip-функция на базе встроенной функции высшего порядка map()
        
    args:
        lst_a (List[Any]): Первый список для объединения;
        lst_b (List[Any]): Второй список для объединения;
        limit (bool): Если False: разница в длине не компенсируется, 
            если True: компенсируется строкой '-'.

    returnes:
        (list[Tuple[str, int]]): Итоговый список из кортежей
    """
    if limit is True:
        max_len = max(len(lst_a),len(lst_b))
        lst_a += '-' * (max_len - len(lst_a))
        lst_b += '-' * (max_len - len(lst_b)) 

    return list(map(lambda x, y: (x, y), lst_a, lst_b))
    