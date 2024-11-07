import json
import requests
from typing import Union, Optional, Dict, List, Any


def print_info(struct: Any, indent: int = 0) -> None:
    """
    Рекурсивная функция для наглядного отображения в консоли структуры данных, представленных в формате:
    {key:
        value:{
            [
                lst_elem_1
                ...
                lst_elem_n
            ]
        }
    }

    :param struct: Любой тип данных
    :param indent: Глубина рекурсии 1 шаг += 4 пробела
    """
    spaces = ' ' * indent

    if isinstance(struct, (str, int)):
        print(str(struct))
        return
    elif struct is None:
        print('None')

    if isinstance(struct, dict):
        print('{')
        for key, value in struct.items():
            print(spaces, str(key) + ':', end=' ')
            print_info(value, indent=indent + 4)
        print(spaces + '}')

    elif isinstance(struct, list):
        print('[')
        for elem in struct:
            if isinstance(elem, (dict, list)):
                print_info(elem, indent=indent + 4)
            else:
                print(spaces, str(elem))
        print(spaces + ']')


class SWAPIInfo:
    """
    Класс, предоставляющий возможность взаимодействия с ресурсом https://www.swapi.tech, и осуществлять парсинг с
    учетом определенного шаблона, а именно:
    Информация о корабле (класс корабля, максимальная скорость в атмосфере, список пилотов) ->
        Список пилотов (рост, вес, имя, название родной планеты, ссылка на родную планету в базе)

    :param _ship: Словарь, объединяющий в себе все вышеупомянутые данные;
    :type _ship: Dict[Union[Dict, List]]
    :param _pilot: Список из словарей, которые хранят всю информацию о пилотах;
    :type _polot: List[Dict]

    Methods
    -------
    :method request_data(url: str, key_search: str) -> Union[Dict, List, None]:
        Запрашивает данные по указанному URL и возвращает результат поиска по ключу.

        :param url: URL для запроса.
        :type url: str
        :param key_search: Ключ для поиска данных в полученной структуре.
        :type key_search: str
        :return: Найденные данные по ключу или None, если ключ не найден.
        :rtype: Union[Dict, List, None]

    :method get_struct(root_struct: Union[Dict, List], name_struct: str) -> Optional[Union[Dict, List, str]]:
        Рекурсивно ищет и возвращает словарь по указанному ключу в структуре данных.

        :param root_struct: Исходная структура данных для поиска.
        :type root_struct: Union[Dict, List]
        :param name_struct: Имя ключа, который нужно найти.
        :type name_struct: str
        :return: Найденные данные или None, если ключ не найден.
        :rtype: Optional[Union[Dict, List, str]]

    :method dump_file() -> None:
        Заносит результаты парсинга в файл *.json
    """
    def __init__(self):
        self._ship: Dict = dict()
        self._pilots: List[Dict] = []


    def request_data(self, url: str, key_search: str) -> Union[Dict, List, None]:
        """
        Запрашивает данные по указанному URL и возвращает результат поиска по ключу.

        :param url: URL для запроса.
        :type url: str
        :param key_search: Ключ для поиска данных в полученной структуре.
        :type key_search: str
        :return: Найденные данные по ключу или None, если ключ не найден.
        :rtype: Union[Dict, List, None]
        """
        in_data = requests.get(url)
        proc_data = json.loads(in_data.text)

        return self.__class__.get_struct(proc_data, key_search)


    @classmethod
    def get_struct(cls, root_struct: Union[Dict, List], name_struct: str) -> Optional[Union[Dict, List, str]]:
        """
         Рекурсивно ищет и возвращает словарь по указанному ключу в структуре данных.

        :param root_struct: Исходная структура данных для поиска.
        :type root_struct: Union[Dict, List]
        :param name_struct: Имя ключа, который нужно найти.
        :type name_struct: str
        :return: Найденные данные или None, если ключ не найден.
        :rtype: Optional[Union[Dict, List, str]]
        """
        return_struct = None

        if isinstance(root_struct, (str, int, float)):
            return None

        if isinstance(root_struct, dict):
            for key, value in root_struct.items():
                if name_struct == key:
                    return root_struct[key]
                elif isinstance(value, (dict, list)):
                    return_struct = cls.get_struct(value, name_struct)
                    if return_struct is not None:
                        return return_struct


    @property
    def ship(self) -> Union[Dict, None]:
        return self._ship


    @ship.setter
    def ship(self, ship_name: str) -> None:
        all_ships = self.request_data('https://www.swapi.tech/api/starships/', 'results')

        for ships_dict in all_ships:
            if ship_name in ships_dict['name']:
                right_ship = self.request_data(ships_dict['url'], 'properties')

                self._ship = {
                    key: value for key, value in right_ship.items()
                    if key in ['name', 'starship_class', 'max_atmosphering_speed']
                }

                self._ship['pilots'] = []
                if 'pilots' in right_ship:
                    self.pilots = right_ship['pilots']
                    self._ship['pilots'] = self.pilots
                return
        else:
            raise AttributeError(f'{ship_name}: Такого корабля нет в каталоге!')


    @property
    def pilots(self) -> Union[List[Dict], None]:
        return self._pilots


    @pilots.setter
    def pilots(self, url_pilots: List[str]) -> None:

        for url_pilot in url_pilots:
            info_pilot = self.request_data(url_pilot, 'properties')
            dct_pilot = {
                key: value for key, value in info_pilot.items()
                if key in ['name', 'mass', 'height']
            }

            if 'homeworld' in info_pilot and info_pilot['homeworld']:
                dct_pilot['homeworld_url'] = info_pilot['homeworld']
                dct_pilot['homeworld'] = self.request_data(dct_pilot['homeworld_url'], 'name')

            self._pilots.append(dct_pilot)


    def dump_file(self) -> None:
        """
        Метод для занесения результата парсинга в файл *.json

        :return: None
        """
        with open('info_sw.json', 'w') as file:
            json.dump(self.ship, file, indent=4)



if __name__ == '__main__':
    new_info = SWAPIInfo()
    new_info.ship = 'X-wing'
    print_info(new_info.ship)
    new_info.dump_file()
