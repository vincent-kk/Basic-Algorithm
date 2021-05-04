import sys

input = sys.stdin.readline


# def findPrimeNumber(n):
#     pm = range(n)[2:]
#     for i in range(n)[2:]:
#         if i not in pm:
#             continue
#         pm = list(filter(lambda x: x == i or x % i != 0, pm))
#     return pm


def isPrimeNumver(n):
    if n == 1:
        return False
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


size = int(input())
numbers = map(int, input().split())

result = 0

for n in numbers:
    if isPrimeNumver(n):
        result += 1

print(result)
