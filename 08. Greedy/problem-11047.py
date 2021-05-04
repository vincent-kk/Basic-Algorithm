import sys

input = sys.stdin.readline

size, total = map(int, input().split())
coins = []

for _ in range(size):
    coin = int(input())
    coins.append(coin)

coins.sort(reverse=True)

num_of_coins = 0

for coin in coins:
    if total == 0:
        break
    elif total < coin:
        continue
    else:
        num = total // coin
        total = total % coin
        num_of_coins += num

print(num_of_coins)