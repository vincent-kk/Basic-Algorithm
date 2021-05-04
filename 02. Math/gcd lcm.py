import sys

input = sys.stdin.readline


def makeGcd(n, m):
    while(m != 0):
        temp = n % m
        n = m
        m = temp
    return n


n, m = map(int, input().split())

gcd = makeGcd(n, m)
lcm = int(n*m / gcd)

print(gcd)
print(lcm)
