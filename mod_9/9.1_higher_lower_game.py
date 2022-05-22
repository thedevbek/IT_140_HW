import random

name = input('What is your name? ')
lower = int(input(f'{name}, What is the lowest number you want to start with? '))
upper = int(input(f'{name}, What is the hightest number you want to end with? '))

num = random.randint(lower, upper)
num = int(num)

guess = None
game = True
while game:
    print(f"Let's play! Make a guess {name}!")
    user_input = input()
    if user_input.isdigit():
        guess = int(user_input)
    else:
        print(f'{name}, Invalid input! Please play a number! ')
        continue
    if guess < num:
        print(f'Sorry, to low {name}.' )
    elif guess > num:
        print(f'Sorry, to high {name}.' ) 
    else:
        print(f'Hot Dog, {name} you won.' ) 
        play_again = input(f'{name} do you want to play again? y/n ')
        if play_again == 'y':
            lower = int(input(f' {name}, What is the lowest number you want to start with? '))
            upper = int(input(f' {name}, What is the hightest number you want to end with? '))
            num = random.randint(lower, upper)
            guess = None
        else:
            print(f'{name}, thanks for playing.')
            break  