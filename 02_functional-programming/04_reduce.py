from functools import reduce

values = [1, 2, 3]

def add_values(item1, item2):
    return item1 + item2

total_sum = reduce(add_values, values, 0)

print(values)
print(total_sum)