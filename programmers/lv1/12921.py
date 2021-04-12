# def solution(n):
#     num = set(range(2, n + 1))

#     for i in range(2, n + 1):
#         if i in num:
#             num -= set(range(2 * i, n + 1, i))
#     return len(num)


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
