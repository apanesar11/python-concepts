lst = [1, 2, 2, 3, 4, 5, 5, 6, 7]

dups = list({i for i in lst if lst.count(i) > 1})
print(dups)