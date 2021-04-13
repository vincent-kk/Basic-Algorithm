from math import gcd


# def getGcd(n, m):
#     while m != 0:
#         temp = n % m
#         n = m
#         m = temp
#     return n


def solution(n: int, m: int):
    # gcd = getGcd(n, m)
    # lcm = n * m // gcd
    # return [gcd, lcm]
    g = gcd(n, m)
    l = n * m // g
    return g, l


if __name__ == "__main__":
    n = 3
    m = 12
    print(solution(n, m))
