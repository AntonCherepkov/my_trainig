# Задача 1
## Счетчик
Как то уже создавали декоратор counter, который считает и выводит количество вывзовов декорируемой функции. Для этого мы использовали интересную особенность классов. В этот раз реализуйте тот же декоратор, но уже с использованием знаний о локальных переменных.

Реализуйте декоратор двумя способами:
1. используйте глобальную переменную `count`;
2. используя локальную переменную `count` внутри декоратора.

Дополнительно: найдите команду (в интернете или даже сами), которая прпчисляет все фунеции и методы находящиеся во встроенном пространстве имён в Python.

Результаты выполнения команды:
```
['__class__','__class_getitem__','__contains__','__delattr__','__del_item__',__dir__' ну и так далее...]
```