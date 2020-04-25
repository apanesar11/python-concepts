from random import randint
import sys

min = int(sys.argv[1])
max = int(sys.argv[2])
rand_int = randint(min, max)

while True:
    try:
        guess = int(input(f'Guess the number between {min} and {max}: '))
        if guess == rand_int:
            print('Congratulations, you guessed correctly.')
            break
        else:
            print('Sorry, please try again.')
    except:
        print('Please enter a valid number')