# not good, we want to be able to store the index as well
class Fibonnaci:
    n1 = 0
    n2 = 1
    def __init__(self, max):
        self.max = max

    def __iter__(self):
        return self

    def __next__(self):
        curr_n1 = Fibonnaci.n1
        curr_n2 = Fibonnaci.n2
        updated_n2 = curr_n1 + curr_n2
        if updated_n2 < self.max:
            Fibonnaci.n1 = curr_n2
            Fibonnaci.n2 = updated_n2
            return updated_n2
        Fibonnaci.n1 = 0
        Fibonnaci.n2 = 1
        raise StopIteration

# fib_range = Fibonnaci(1000)
# for i in fib_range:
#     print(i)

# better
def fibonaci_2(num):
    n1 = 0
    n2 = 1
    for i in range(num):
        yield n1
        new_n2 = n1 + n2
        n1 = n2
        n2 = new_n2

for i in fibonaci_2(19):
    print(i)