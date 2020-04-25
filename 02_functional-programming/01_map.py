lst = [1, 2, 3]

def multiply_by_2(item):
    return item*2

doubled_lst = list(map(multiply_by_2, lst))

print(lst)
print(doubled_lst)