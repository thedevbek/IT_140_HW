word = input()
password = ''

word = word.replace('i', '!')
word = word.replace('a', '@')
word = word.replace('m', 'M')
word = word.replace('B', '8')
word = word.replace('o', '.')
word = word + 'q*s'

print(word)