# def isPrimery(n: int):
#     i = 2
#     while i * i <= n:
#         if n % i == 0:
#             return False
#         i += 1
#     return True


def solution(n: int):
    count = 0
    n += 1
    prime = [True] * n
    for i in range(2, n):
        if prime[i]:
            count += 1
            for j in range(2 * i, n, i):
                prime[j] = False
    return count


if __name__ == "__main__":
    i = 10
    print(solution(i))
