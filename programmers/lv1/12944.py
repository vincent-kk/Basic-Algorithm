from typing import List


def solution(arr: List[int]):
    return sum(arr) / len(arr)


if __name__ == "__main__":
    i = [1, 2, 3, 4]
    print(solution(i))
