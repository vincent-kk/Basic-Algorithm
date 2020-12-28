import sys

input = sys.stdin.readline


m, n = map(int, input().split())


def isprime(m, n):
    n += 1
    prime = [True] * n
    for i in range(2, int(n**0.5)+1):
        if prime[i]:
            for j in range(2*i, n, i):
                prime[j] = False

    for i in range(m, n):
        if i > 1 and prime[i] == True:
            print(i)


isprime(m, n)
