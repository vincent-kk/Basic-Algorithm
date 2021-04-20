from itertools import permutations


def isPrimery(n: int):
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def solution(numbers: str) -> int:
    numbers = list(numbers)
    l = len(numbers)
    comb = set()
    for i in range(1, l + 1):
        comb |= set(map(int, map("".join, permutations(numbers, i))))

    comb -= set(range(0, 2))
    answer = set()
    for num in comb:
        if isPrimery(num):
            answer.add(num)

    # for i in range(2, int(max(comb) ** 0.5) + 1):
    #     comb -= set(range(i * 2, max(comb) + 1, i))

    return len(answer)


if __name__ == "__main__":
    i = "17"
    print(solution(i))
