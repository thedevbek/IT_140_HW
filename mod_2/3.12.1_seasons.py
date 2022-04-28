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
