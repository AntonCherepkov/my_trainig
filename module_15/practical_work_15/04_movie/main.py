films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']

while True:
    numbers_films = int(input('Number of movies to enter: '))
    if numbers_films <= len(films):
        break
    else:
        print('There are not so many films in the films library')
count_input = 0
list_favorite_movie = []

while count_input != numbers_films:
    film_user = input('Enter the name of the movie: ')
    for movie in range(len(films)):
        if films[movie] == film_user:
            list_favorite_movie.append(films[movie])
            count_input += 1
            break
    else:
        print("Error: we don't have such a movie")

print(f'Your list of favorite movies: {list_favorite_movie}')

# зачет!
