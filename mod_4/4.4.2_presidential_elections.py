year = 1792
current_year = input()

while  int(current_year)>=int(year) :
    print(int(current_year) - int(year), end=' ')
    year = int(year)  + 4
print(year)
