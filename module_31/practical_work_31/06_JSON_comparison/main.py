from typing import Optional, Dict, List, Union, Any
import json
from pprint import pprint


ValueType = Union[str, int, float, List[Any], Dict[str, Any]]
NestedDict = Dict[str, ValueType]

def comparison_struct(struct_a: NestedDict,  struct_b: NestedDict) -> bool:
    """
    Функция, которая рекурсивно проходит по переданным структурам данных, и как только находит различие в них прекращает
    свою работу и возвращает True. Если же в ходе работы функции различий в структуре данных не обнаружено, то тогда
    возвращается False.

    :params struct_a and struct_b: Структуры данных для сравнения
    :return: True/False
    """
    is_compar = False

    if all(isinstance(x, dict) for x in (struct_a, struct_b)):
        for key, value in struct_a.items():
            is_compar = comparison_struct(value, struct_b[key])
            if is_compar:
                return is_compar

    elif all(isinstance(y, list) for y in (struct_a, struct_b)):
        for elem_a, elem_b in zip(struct_a, struct_b):
            if all(isinstance(z, (list, dict)) for z in (elem_a, elem_b)):
                is_compar = comparison_struct(elem_a, elem_b)
                if is_compar:
                    return is_compar
    else:
        if struct_a != struct_b:
            return True


def find_control_struct(
        struct_a: NestedDict,
        struct_b: NestedDict,
        tracked_keys: List[str],
        result_dct: Optional[NestedDict] = None
) -> Dict[str, NestedDict]:
    """
    Функция, предназначенная для локализации областей структур данных, для дальнейшего анализа их соответствия
    друг другу, посредствам вызова вспомогательной функции comparison_struct(). Если этой вспомогательной функцией
    подтверждается несоответствие указанных областей (значений ключей), то тогда эта рабочая пара ключ-значение вносится
    в итоговый словарь, взятый из первой структуры данных.

    :param struct_a: Первая, базовая структура данных, значения которой вносятся в итоговый словарь с изменениями;
    :param struct_b: Вторая, опорная структура данных, относительно которой отслеживаются изменения;
    :param tracked_keys: Список ключей, значения которых будут определять области для поиска изменений в структуре
        данных;
    :param result_dct: Итоговый словарь для вывода областей с выявленными изменениями
    :return: result_dct
    """
    if result_dct is None:
        result_dct = dict()

    if all(isinstance(x, dict) for x in (struct_a, struct_b)):
        for key, value in struct_a.items():
            diff = dict()
            if key in tracked_keys:
                is_correspondence = comparison_struct(value, struct_b.get(key))
                if is_correspondence:
                    diff[key] = value
                    result_dct.update(diff)

            elif all(isinstance(y, (list, dict)) for y in (value, struct_b[key])):
                result_dct = find_control_struct(value, struct_b[key], tracked_keys, result_dct)

    return result_dct


with open('json_new.json', 'r', encoding='utf-8') as f:
    new_json = json.load(f)

with open('json_old.json', 'r', encoding='utf-8') as f:
    old_json = json.load(f)

diff_list = ["services", "staff", "datetime"]

print(f'Все изменения, выбранные пользователем для контроля: {diff_list}:')
result_dct = find_control_struct(new_json, old_json, diff_list)

pprint(result_dct)

with open('result_json.json', 'w', encoding='utf-8') as f:
    json.dump(result_dct, f, indent=4)
