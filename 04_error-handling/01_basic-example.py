while True:
    try:
        age = int(input('Enter an age: '))
        test_val = 1/age
    except ZeroDivisionError:
        print('Please enter a number greater than 0')
    except ValueError:
        print('Please enter a number')
    else:
        break