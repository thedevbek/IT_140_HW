'''
Write a program that gets a list of integers from input, and outputs non-negative integers in ascending order (lowest to highest).'''

user_input = input()

my_list = [int(i) for i in user_input.split() 
if (int(i)>=0)] 

my_list.sort()

[print(i, end=' ') for i in my_list]