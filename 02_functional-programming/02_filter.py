lst = [1, 2, 3]

def is_odd(item):
    return item%2

odd_lst = list(filter(is_odd, lst))

print(lst)
print(odd_lst)