from collections import Counter


def unique_char_with_Counter(in_str: str) -> int:
    """Функция для подсчета уникальных символов, с использованием метода Counter модуля collections"""
    return sum(map(lambda x: 1 if x == 1 else 0, Counter(in_str.lower()).values()))


def uniaue_char_without_Counter(in_str: str) -> int:
    """Функция для подсчета уникальных символов, используя только лишь lambda и map функции"""
    my_counter = dict(map(lambda sym: (sym, in_str.lower().count(sym)), in_str.lower()))
    return sum(map(lambda x: 1 if x == 1 else 0, my_counter.values()))


message = "Today is a beautiful day! The sun is shining and the birds are singing."

unique_count1 = unique_char_with_Counter(message)
unique_count2 = uniaue_char_without_Counter(message)
print("Количество уникальных символов в строке, решение №1:", unique_count1)
print("Количество уникальных символов в строке, решение №2:", unique_count2)
