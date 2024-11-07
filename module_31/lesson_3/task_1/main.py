import requests
import json


def search_name(in_dict: dict, search_key: str, new_value: str = None) -> None:
    """
    Рекурсивная функция для поиска значения по заданному ключу, и его замене при установке аттрибута new_value
    :param in_dict: Словарь, передаваемый для поиска в нём ключа
    :type in_dict: dict
    :param search_key: Искомый ключ
    :type search_key: str
    :param new_value: значение, которое нужно установить по заданному ключу
    :return: значение, найденное по заданному ключу
    """
    out_value = None
    for key, value in in_dict.items():
        if search_key not in in_dict:
            if isinstance(value, dict):
                out_value = search_name(value, search_key, new_value)
        else:
            if new_value is not None:
                in_dict['name'] = new_value
            return in_dict[search_key]
    else:
        return out_value



download_json_1 = requests.get('https://www.swapi.tech/api/people/3')
json_in_python_1 = json.loads(download_json_1.text)

search_name(json_in_python_1, 'name', new_value='Anton')
new_link = search_name(json_in_python_1, search_key='homeworld')

with open('people_3_info.json', 'w') as file:
    json.dump(json_in_python_1, file, indent=4)
#
download_json_2 = requests.get(new_link)
json_in_python_2 = json.loads(download_json_2.text)

with open('planets_8_info.json', 'w') as file:
    json.dump(json_in_python_2, file, indent=4)
