'''
Write a program using integers user_num and x as input, and output user_num divided by x three times.'''

user_num = input()
x = input()
first_time = int(user_num) // int(x)
second_time = int(first_time) // int(x)
third_time = int(second_time) // int(x)
print(first_time, second_time,third_time)
