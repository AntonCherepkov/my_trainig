# Задача 2.
## Случайная сумма
Алексею по работе необходимо обработать огромное количество данных из миллионов элементов. Каждый новый элемент - это сумма случайного вещественного числа от 0 до 1 и предыдущего элемента (первый элемент - просто случайное вещественное число от 0 до 1). Алексею нельзя хранить в памяти весь этот список, а со значениями работать как то надо.
Помогите Алексею, реализуйте такой класс-итератор и проверте его работу. Также сделайте так, что бы при каждом новом вызове итератора в цикле значения считались заново.
Пример работы программы:
```
Количество элементов: 5
Элементы итератора: 
0.74
1.13
1.95
2.2
2.55
Новое количество элементов: 6
Элементы итератора:
0.79
1.58
2.55
2.81
3.06
3.34
```