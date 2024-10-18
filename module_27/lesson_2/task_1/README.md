# Задача 1
## Двойной вызов
Реализуйте декоратор `do_twice`, который дважды вызывает декорируемую функцию. Не забывайте про документацию и аннотацию типов.
Пример декорируемой функции:
```
def greenting(name):
    print(f'Привет, {name}!'.format(name=name))

greenting('Tom')
```
Результат работы программы:
```
Привет, Tom!
Привет, Tom!
```