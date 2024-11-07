import random

first_team = [round(random.uniform(5, 10), 2) for _ in range(20)]
second_team = [round(random.uniform(5, 10), 2) for _ in range(20)]
result_list = [first_team[i_num] if first_team[i_num] > second_team[i_num]
               else second_team[i_num]
               for i_num in range(20)]

print(first_team)
print(second_team)
print(result_list)

# зачет!
