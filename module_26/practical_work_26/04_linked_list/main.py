from linkedlist_class import LinkedList


linked_list = LinkedList()

print('Создаю связный список из четырех элементов: 11, 22.2, 33, 44')
for num in [11, 22.2, 33, 44]:
    linked_list.append(num)

print('Вывожу весь список: ', end=' ')
linked_list.show_linklist()

print(f'Верну превый элемент списка: {linked_list.get(0)}')
print(f'Верну второй элемент списка: {linked_list.get(1)}')
print(f'Верну третий элемент списка: {linked_list.get(2)}')
print(f'Верну четвертый элемент списка: {linked_list.get(3)}')

# Тест: выход за границы списка: вывод None
# print(f'Ничего не верну: {linked_list.get(4)}') 


del_node = linked_list.remove(2)
print(f'Удалил элемент списка: {del_node}')

print('Вывожу измененный список:', end=' ')
linked_list.show_linklist()

del_node = linked_list.remove(0)
print(f'Удалил элемент списка: {del_node}')

print('Вывожу измененный список:', end=' ')
linked_list.show_linklist()

print('Восстанавливаю список, добавив в него следующие элементы: 55, 66')
for num in [55, 66]:
    linked_list.append(num)

print('Вывожу измененный список:', end=' ')
linked_list.show_linklist()

print('Итерируемся по значениям связного списка:')
for num in linked_list:
    print(num, end=' ')
    