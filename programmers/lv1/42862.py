from typing import List


def solution(n: int, lost: List[int], reserve: List[int]):

    lost = set(lost)
    reserve = set(reserve)
    block = lost & reserve
    lost = list(lost - block)
    reserve = list(reserve - block)

    lost.sort(reverse=True)
    reserve.sort()
    remainder = len(lost)
    for person in reserve:

        if len(lost) > 0 and person > lost[-1] + 1:
            while person > lost[-1] + 1:
                lost.pop()
                if len(lost) == 0:
                    break
        if len(lost) == 0:
            break

        if abs(person - lost[-1]) <= 1:
            lost.pop()
            remainder -= 1

    return n - remainder


if __name__ == "__main__":
    n = 5
    i1 = [2, 3, 4]
    i2 = [1, 2, 3]
    print(solution(n, i1, i2))
