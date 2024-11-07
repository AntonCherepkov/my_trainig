def conversion_on_dict(in_str):
    return {symbol: in_str.count(symbol) for symbol in in_str}


def reverce_dict_first(in_dict):
    result_dict = dict()
    for symbol, count in in_dict.items():
        if count in result_dict:
            result_dict[count].append(symbol)
        else:
            result_dict[count] = [symbol]

    return result_dict


def reverce_dict_second(in_dict):
    result_dict = {
        count: [symbol for symbol, in_count in in_dict.items() if in_count == count]
        for _, count in in_dict.items()
    }

    return result_dict


user_str = 'здесь что-то написано'

first_inversion = reverce_dict_first(conversion_on_dict(user_str))
second_inversion = reverce_dict_second(conversion_on_dict(user_str))

for count_key in first_inversion:
    print(f'{count_key}: {first_inversion[count_key]}')
print()

for count_key in second_inversion:
    print(f'{count_key}: {second_inversion[count_key]}')

# зачет!
