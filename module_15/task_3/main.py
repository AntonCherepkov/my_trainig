print('Задача 3. Кино')
# Мы поддерживаем свой киносайт и хотим сделать так, что бы пользователи после регистрации могли создать свой
# рейтинг фильмов из тех, которые есть на сайте. Вот сам список фильмов (конечно же можете брать свои):

film = [
    'Крепкий орешек', 'Зелёная миля', 'Назад в будующее', 'Леон', 'Город грехов', 'Матрица',
    'Остров проклятых', 'Начало', 'Мементо', 'Деревня', 'Отступники', 'Джентельмены удачи'
    ]

# Напишите программу, которая позволяет добавлять в свой рейтинг фильмы, удалять их от туда, а также вставлять на
# нужное пользователю место. Обеспечте контроль ввода и сделайте так, чтобы в список нельзя было добавить один и 
# тот же фильм несколько раз.
 
# Пример работы программы:

# Ваш текущий топ фильмов: []
# Название фильма: Леон
# Команды: добавить, вставить, удалить
# Введите команду: добавить
#  
# Ваш текущий топ фильмов: ['Леон']
# Название фильма: Леон
# Команды: добавить, вставить, удалить
# Введите команду: добавить
# Этот фильм уже в вашем списке
# 
# Ваш текущий топ фильмов: ['Леон']
# Название фильма: Матрица
# Команды: добавить, вставить, удалить
# Введите команду: добавить
#
# Ваш текущий топ фильмов: ['Леон', 'Матрица']
# Название фильма: Леон
# Команды: добавить, вставить, удалить
# Введите команду: удалить
# 
# Ваш текущий топ фильмов: ['Матрица']
# Название фильма:

def search_in_film_library(movie, list_film):
    for i_movie in list_film:
        if i_movie == movie:
            return True
    return False


list_top = []

while True:
    print(f'Your list of favorite movies: {list_top}')
    print(f'Enter the favorit movie:', end= ' ')
    my_movie = input()
    if search_in_film_library(my_movie, film):
        print('Select the comand: [add], [past], [delete]:', end= ' ')
        command = input()
        if command == 'add':
            if not(search_in_film_library(my_movie, list_top)):
                list_top.append(my_movie)   
            else:
                print('Such a films is already on the list')         
        elif command == 'past':
            if not(search_in_film_library(my_movie, list_top)):
                position_movie = int(input('To what position? '))
                list_top.insert(position_movie - 1, my_movie)
            else:
                print('Such a films is already on the list')
        elif command == 'delete':
            list_top.remove(my_movie)
    else:
        print('This movie is not on the site!')
    print()