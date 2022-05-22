'''Prompt the user to enter two words and a number, storing each into separate variables. Then, output those three values on a single line separated by a space. (Submit for 1 point)

Ex: If the input is:

yellow
Daisy
6
the output after the prompts is:

You entered: yellow Daisy 6
Note: User input is not part of the program output.'''

favorite_color = input('Enter favorite color:\n')
favorite_animal = input('')
num = input('')
print('You entered:',favorite_color, favorite_animal, num)

password1 = favorite_color + '_' + favorite_animal
password2 = num + favorite_color + num
print('\nFirst password:',password1)
print(f'Second password: {password2}''\n')

print(f'Number of characters in {password1}:', len(password1))
print(f'Number of characters in {password2}:', len(password2))