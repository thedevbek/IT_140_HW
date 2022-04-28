from collections import Counter
## input characters
## input string 
## count() num of characters in string
## print out num of count characters
char_input = input('')
user_input = input('')
count = 0
for i in user_input:
    if i == char_input:
        count = count + 1
print(count)






'''
user_input = input()
character = input()

counting_char = user_input.count(character) 
print(counting_char)
'''
