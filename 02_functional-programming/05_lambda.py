from functools import reduce
lst = [1, 2, 3]

doubled_lst = list(map(lambda item: item * 2, lst))
print(lst)
print(doubled_lst)

odd_lst = list(filter(lambda item: item%2, lst))
print(lst)
print(odd_lst)

total_sum = reduce(lambda i, j: i+j, lst, 0)

print(lst)
print(total_sum)