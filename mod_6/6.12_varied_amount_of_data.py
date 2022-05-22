'''
Statistics are often calculated with varying amounts of input data. Write a program that takes any number of integers as input, and outputs the average and max.'''
nums = []

# loop until there isn't an input
while not nums:
    # ask for user input
    number = input()
    nums = [int(x) for x in number.split() if x]

avg = int(sum(nums) / len(nums))
print(avg, max(nums))