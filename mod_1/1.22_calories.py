'''The following equation estimates the average calories burned for a person when exercising, which is based on a scientific journal article (source):

Calories = ( (Age x 0.2757) + (Weight x 0.03295) + (Heart Rate x 1.0781) — 75.4991 ) x Time / 8.368

Write a program using inputs age (years), weight (pounds), heart rate (beats per minute), and time (minutes), respectively. Output the average calories burned for a person.

Output each floating-point value with two digits after the decimal point, which can be achieved as follows:
print('Calories: {:.2f} calories'.format(calories))'''

age = int(input())
weight = int(input())
heart_rate = int(input())
time = int(input())
calories = (age * 0.2757 + weight * 0.03295 + heart_rate * 1.0781 - 75.4991) * time / 8.368
print('Calories: {:.2f} calories'.format(calories))