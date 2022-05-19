
coins = ['dollars', 'quarters', 'dimes', 'nickels', 'pennies']
coin_value = [100, 25, 10, 5, 1]
user_total = 0
for coin in coins:
    number_of_coins = 0
    while user_total > coin_value:
        user_total -= coin_value # user_total = user_total - 100
        number_of_coins += 1
        print(user_total)
        print(coins)