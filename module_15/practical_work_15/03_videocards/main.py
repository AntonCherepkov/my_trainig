def search_max(list_user):
    out_list = []
    maximal = list_user[0]
    for i_num in range(len(list_user)):
        if list_user[i_num] > maximal:
            maximal = list_user[i_num]
    for i_num in range(len(list_user)):
        if maximal == list_user[i_num]:
            out_list.append(i_num)
    return out_list


list_models = []
num = int(input('How many video cards models are there in the store? '))

for i_model in range(num):
    while True:
        print(f'{i_model + 1} Video card:', end= ' ')
        model = int(input())
        if model > 999:
            break
        else:
            print('GeForce graphics card models have a four-digit designation')
    list_models.append(model)

print(f'The old list of video card: {list_models}')

new_list_models = []
index_list = search_max(list_models)

for i_model in range(len(list_models)):
    for i_new in range(len(index_list)):
        if i_model == index_list[i_new]:
            list_models[i_model] = 0
            break
    if list_models[i_model] != 0:
        new_list_models.append(list_models[i_model])

print(f'The new list of video card: {new_list_models}')

# зачет!
