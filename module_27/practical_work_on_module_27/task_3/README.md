# Задача 3
## Логирование
Реализуйте декоратор logging, который будет отвечать за логгирование функций. На экран выводится название функций и её документация. Если во время выполнения декорируемой функции возникла ошибка, то в файл `function_error.log` записывается название функции и ошибки.

Постарайтесь сделать так, что бы программа не завершалась после нахождения первой же ошибки, а обрабатывала все декодируемые функции и сразу записывала все ошибки в файл.

Дополнительно: Запишите дату и время возникновения ошибки, используя модуль `datetime`.