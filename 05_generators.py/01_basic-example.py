def generator(num):
    for i in range(num):
        yield i

g = generator(3)
print(next(g))
print(next(g))
print(next(g))