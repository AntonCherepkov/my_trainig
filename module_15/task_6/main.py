print('Задача 3. Пакеты')
# При работе с сервером мы кодируем сообщение и отправляем его в виде пакетов информации. Их количество равно N.
# Допустим каждый пакет содержит четыре числа, каждое из которых равно нулю или единице. Эти числа называются 
# битами. Иногда в кодировке сообщения встречаются ошибки, и в пакете эта ошибка обозначается числом -1. Если
# таких ошибок не больше одной, то этот пакет мы целиком добавляем в список для декодирования, а иначе 
# отбрасываем. 
# Напишите программу, которая будет обрабатывать полученные пакеты и выведет на экран итоговое сообщение для 
# декодирования, а также количество ошибок в нем и количество необработанных пакетов.
# 
# Пример:
# Количество пакетов: 3
# Пакет номер: 1
# 1 бит: 1
# 2 бит: 0
# 3 бит: -1
# 4 бит: 1
# Пакет номер: 2
# 1 бит: -1
# 2 бит: -1
# 3 бит: 1
# 4 бит: 1
# Пакет номер: 3
# 1 бит: 0
# 2 бит: 1
# 3 бит: 1
# 4 бит: 1
# Полученное сообщение: [1, 0, -1, 1, 0, 1, 1, 1]
# Количество ошибок в сообщении: 1
# Количество потерянных пакетов: 1

num_pack = int(input('Enter the number of puackages: ')) 
package = []
message = []
count_lost_pack = num_pack

for pack in range(num_pack):
    print(f'Package number: {pack + 1}')
    for i_bit in range(4):
        bit = int(input(f'{i_bit + 1} bit: '))
        package.append(bit)
    if package.count(-1) <= 1:
        message.extend(package)
        count_lost_pack -= 1
    package = []

print(f'The received message: {message}')
print(f'The number of errors in the message: {message.count(-1)}')
print(f'The number of lost packets: {count_lost_pack}')