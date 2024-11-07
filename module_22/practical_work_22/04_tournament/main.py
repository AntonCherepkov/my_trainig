import os

def list_of_past_players(file_obj, result=None, count_win=0):
    if result is None:
        result = []

    list_text = file_obj.readlines()
    work_list = [
        tuple(i_line.split()) 
        for i_line in list_text[1:]
    ]
    work_list = sorted(work_list, key=lambda line: line[2], reverse=True)

    for surname, name, score in work_list:
        if list_text[0] < score:
            count_win += 1
            result.append(
                str(count_win) + ') '
                + ('.'.join(name))[:2]
                + surname + ' '
                + score + '\n'
            )
    return result


work_path = os.path.abspath(os.getcwd())
path_in_file = os.path.join(work_path, 'first_tour.txt')
path_out_file = os.path.join(work_path, 'second_tour.txt')

in_file_obj = open(path_in_file, 'r')
result_tuple_of_list = list_of_past_players(in_file_obj)

out_file_obj = open(path_out_file, 'w')

out_file_obj.write(str(len(result_tuple_of_list)) + '\n')
for player in result_tuple_of_list:
    out_file_obj.write(player)

out_file_obj.close()
in_file_obj.close()

print()
