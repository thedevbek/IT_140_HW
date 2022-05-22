'''
Write a program whose input is a string which contains a character and a phrase, and whose output indicates the number of times the character appears in the phrase.'''

user_input = str(input())
char = user_input[0]
phrase = user_input[1:]
counter = phrase.count(char)
print(counter)