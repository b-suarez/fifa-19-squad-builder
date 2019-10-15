def count_values_dict_keys(dict, key):
    count = 0
    for values in dict[key]:
        count = count + 1

    return count
