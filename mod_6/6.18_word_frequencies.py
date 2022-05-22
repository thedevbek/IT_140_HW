'''Write a program that reads a list of words. Then, the program outputs those words and their frequencies.'''

list = input('Input text: ')
text = list.split()

for word in text:
    freq = text.count(word) 
    print(word, freq)