import sys

input = sys.stdin.readline


def primeTable(n):
    n += 1
    prime = [True] * n
    prime[0] = prime[1] = False
    for i in range(2, int(n**0.5)+1):
        if prime[i]:
            for j in range(2*i, n, i):
                prime[j] = False
    return prime


prime = primeTable(1000000)

while True:

    n = int(input())

    if n == 0:
        break

    for i in range(n, 2, -1):
        if prime[i] == True:
            if prime[n-i] == True:
                print('%d = %d + %d' % (n, n-i, i))
                break
