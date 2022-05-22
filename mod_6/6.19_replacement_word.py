'''Write a program that replaces words in a sentence. The input begins with word replacement pairs (original and replacement). The next line of input is the sentence where any word on the original list is replaced.'''

pairs = input().split()


originals = pairs[::2]
replacements = pairs[1::2]

sent = input()

for org, repl in zip(originals, replacements):
    sent = sent.replace(org, repl)

print(sent)