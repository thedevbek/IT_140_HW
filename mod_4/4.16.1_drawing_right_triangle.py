triangle_char = input('Enter a character:\n')
triangle_height = int(input('Enter triangle height:\n'))
print('')


for i in range(triangle_height):
    for j in range(i+1):
        print(triangle_char, end=' ')
    print()
