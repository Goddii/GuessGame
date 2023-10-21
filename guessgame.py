import random

def guess(x):
    guess = 0
    random_number = random.randint(1, x)

    while guess != random_number:
        guess = int(input(f'Enter guess between 1 and {x}: '))
        if guess > random_number:
            print('Number is too high')
        elif guess < random_number:
            print('Number is too low')
        else:
            print(f'Congratulations you have guessed the number correctly as {random_number}')

guess(10)

