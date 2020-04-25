lst = [1, 2, 2, 3, 4, 5, 6, 6, 7]

simple_set = {i for i in lst}

simple_dict = {
    'one': 1,
    'two': 2
}

simple_dict_copy = {k:v for k, v in simple_dict.items()}
dict_from_list = {i:i**2 for i in range(100)}

print(simple_set)
print(simple_dict_copy)
print(dict_from_list)