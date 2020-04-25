class MyRange:
    current = 0
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __iter__(self):
        return self

    def __next__(self):
        if MyRange.current < self.last:
            num = MyRange.current
            MyRange.current += 1
            return num
        MyRange.current = 0
        raise StopIteration

my_range = MyRange(0, 3)

for i in my_range:
    print(i)