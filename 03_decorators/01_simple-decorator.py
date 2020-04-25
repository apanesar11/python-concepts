def wrap_output(func):
    def wrapped_func():
        print("*****")
        func()
        print("*****")
    return wrapped_func

@wrap_output
def hello():
    print('Hi there')

hello()