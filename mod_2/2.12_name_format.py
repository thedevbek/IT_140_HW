'''Many documents use a specific format for a person's name. Write a program whose input is:
firstName middleName lastName
and whose output is:
lastName, firstInitial.middleInitial.
Ex: If the input is:
Pat Silly Doe
the output is:
Doe, P.S.
If the input has the form:
firstName lastName
the output is:
lastName, firstInitial.
Ex: If the input is:
Julia Clark
the output is:
Clark, J.'''

full_name = input('Enter full name: ')
output_name = full_name.split(' ')
temp = '.'.join([output_name[i][0] for i in range (0, len(output_name)-1)])
if temp == '':
    print(output_name[-1])
else:
    print(output_name[-1] + ','+ ' ' + temp + '.')