from my_collection import MyDict


new_dict = MyDict({1: '2', 3: '4', 5: '6'})
print(new_dict.get(1), new_dict.get(2))

old_dict = {7: '8', 9: '10', 11: '12'}
print(old_dict.get(7), old_dict.get(8))
