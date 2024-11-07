violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

user_list = []
songs_time = 0
while True:
    num_songs = int(input('How many songs to add? '))
    if num_songs <= len(violator_songs):
        break
    else:
        print('There are not so many songs on the list')

for i_num in range(num_songs):
    print(f'Enter {i_num + 1} the song:', end=' ')
    user_song = input()
    for song in violator_songs:
        if song[0] == user_song:
            songs_time += song[1]
            break
    else:
        print(f"\tSong No.{i_num + 1} is not on the list. We won't count it")

print(f'\nThe total time of the songs: {songs_time}')

# зачет!
