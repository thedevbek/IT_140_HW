'''Prompt the user to input an integer between 32 and 126, a float, a character, and a string, storing each into separate variables. Then, output those four values on a single line separated by a space.'''

user_int = int(input('Enter integer (32 - 126):\n'))
user_float = float(input('Enter float:\n'))
user_character = input('Enter character:\n')
user_string = input('Enter string:\n')
# FIXME (1): Finish reading other items into variables, then output the four values on a single line separated by a space
print(user_int, user_float, user_character, user_string )
# FIXME (2): Output the four values in reverse
print(user_string, user_character, user_float, user_int)
# FIXME (3): Convert the integer to a character, and output that character
print(user_int,'converted to a character is',chr(user_int))