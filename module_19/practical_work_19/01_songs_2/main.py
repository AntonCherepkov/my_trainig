violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

while True:
    count_song = int(input('How many songs to choose: '))
    if len(violator_songs) >= count_song:
        break
    else:
        print(f'Select no more then {len(violator_songs)}')

total_duration = 0
for song in range(count_song):
    while True:
        print(f'Enter the name of the {song + 1} song:', end=' ')
        user_song = input()
        if user_song in violator_songs.keys():
            total_duration += violator_songs[user_song]
            break
        else:
            print('There is no such song in the list')

print('The total duration of the songs is {:.2f} minutes'.format(
    total_duration
))

# зачет!
