def divide(num, den):
    try:
        print(num/den)
    except (TypeError, ZeroDivisionError) as e:
        print(e)
    finally:
        print('done executing')

divide(1, 2)
divide(1, 0)
divide('1', 1)