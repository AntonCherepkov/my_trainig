from collections import Counter


def can_be_poly(check_str: str) -> bool:
    """
    Функция для проверки строки на возможность формирования из неё палиндрома

    args:
        check_str (str): входная строка

    returns:
        (bool): True - если можно собрать палиндром, False - если нельзя собрать палиндром
    """
    result_count = Counter(check_str)

    check_quant = list(map(lambda x: True if x % 2 == 0 else False, result_count.values()))

    if check_quant.count(False) > 2:
        return False
    return True


print(can_be_poly('abcba'))
print(can_be_poly('abbbc'))
