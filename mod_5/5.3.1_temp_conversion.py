def c_to_f():
    f = c * 9/5 + 32
    return  f

c = float(input('Enter temperature in Celsius: '))
f = None

print(f'you entered {c} celsius which is {f} fahrenheit.')

c_to_f()

