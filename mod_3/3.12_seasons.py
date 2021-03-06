'''Write a program that takes a date as input and outputs the date's season. The input is a string to represent the month and an int to represent the day.

The dates for each season are:
Spring: March 20 - June 20
Summer: June 21 - September 21
Autumn: September 22 - December 20
Winter: December 21 - March 19
'''
input_month = input()
input_day = int(input())

if input_month in ('January', 'February', 'March'):
	season = 'Winter'
elif input_month in ('April', 'May', 'June'):
	season = 'Spring'
elif input_month in ('July', 'August', 'September'):
	season = 'Summer'
elif input_month in ('October', 'November', 'December'):
	season = 'Autumn'
else:
	season = 'Invalid'

if (input_month == 'March') and (input_day > 19):
	season = 'Spring'
elif (input_month == 'June') and (input_day > 20):
	season = 'Summer'
elif (input_month == 'September') and (input_day > 21 and input_day < 32):
	season = 'Autumn'
elif (input_month == 'December') and (input_day > 20):
	season = 'Winter'
elif (input_day > 31) or (input_day < 0):
    season = 'Invalid'

print(season)

