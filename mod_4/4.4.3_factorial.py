'''
Write a program that lets a user enter N and that outputs N! (N factorial, meaning N*(N-1)*(N-2)*...*2*1). Hint:Use a loop variable i that counts from total-1 down to 1. Compare your output with some of these answers: 1:1, 2:2, 3:6, 4:24, 5:120, 8:40320.

'''
N = int(input())  # Read user-entered number
total = N
x = 0
i = 0
while i > 1:
    N *= i
    x -= 1

print(total)