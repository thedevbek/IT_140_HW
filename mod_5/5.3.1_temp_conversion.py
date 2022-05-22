'''Complete the program by writing and calling a function that converts a temperature from Celsius into Fahrenheit. Use the formula F = C x 9/5 + 32. Test your program knowing that 50 Celsius is 122 Fahrenheit.'''

def c_to_f():
    f = c * 9/5 + 32
    return  f

c = float(input('Enter temperature in Celsius: '))
f = None

print(f'you entered {c} celsius which is {f} fahrenheit.')

c_to_f()

