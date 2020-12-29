import sys

input = sys.stdin.readline


def countFacPrime(n, t):
    step = t
    result = 0
    while n >= step:
        result += n // step
        step *= t
    return result


n, m = map(int, input().split())

facN2 = countFacPrime(n, 2)
facN5 = countFacPrime(n, 5)

facM2 = countFacPrime(m, 2)
facM5 = countFacPrime(m, 5)

facNM2 = countFacPrime(n-m, 2)
facNM5 = countFacPrime(n-m, 5)

result = min(facN2-facM2-facNM2, facN5-facM5-facNM5)

print(result)
