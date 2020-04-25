from time import time

def performance(func):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'function took {t2 - t1} seconds to execute')
        return result
    return wrapper

@performance
def create_long_list(size):
    lst = [i for i in range(size)]
    return lst

create_long_list(100000000)