def wrap_output(func):
    def wrapped_func(*args, **kwargs):
        print("*****")
        func(*args, **kwargs)
        print("*****")
    return wrapped_func

@wrap_output
def hello(name, age):
    print(f'Hello, my name is {name} and I am {age} years old')

hello('Arashdeep', 20)