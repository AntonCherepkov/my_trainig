# Задача 1
## Скороговорка
Дан текст вот такой английской скороговорки:
```
How much wood would a woodchuck chuck if a woodchuck could chuck wood?
```
С помощью модуля `re` реализуйте программу, которая следующие действия по порядку:

1. Определить, начинается ли текст с шаблона `wo`.
2. Найдите первое упоминание шаблона `wo` в тексте.
3. Определить содержимое найденной по шаблону подстроки из п.2.
4. Найти позицию, с которого начинается первое упоминание шаблона `wo`.
5. Найти позицию, на которой заканчивается первое упоминание шаблона  `wo`.
6. Получить список из каждого упоминания шаблона `wo`.
7. Заменить в тексте все совпадения по шаблону `wo` на слово '`ЗАМЕНА`'.

По каждому действию вывести соответствующий результат. Не используйте методы строк. Не забывайте использовать приписку `r` в шаблоне.