'''A variable like user_num can store a value like an integer. Extend the given program as indicated.

Output the user's input. (2 pts)
Output the input squared and cubed. Hint: Compute squared as user_num * user_num. (2 pts)
Get a second user input into user_num2, and output the sum and product. (1 pt)'''

user_num = int(input('Enter integer:\n'))
print('You entered:', user_num)
square = user_num * user_num
print(user_num, 'squared is', square)
cube = user_num * user_num * user_num
print('And', user_num , 'cubed is', cube ,'!!')
user_num2 = int(input('Enter another integer:\n'))
add = user_num + user_num2
sub = user_num * user_num2
print(user_num, '+', user_num2, 'is', add)
print(user_num, '*', user_num2, 'is', sub)