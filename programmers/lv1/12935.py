from typing import List


def solution(arr: List[int]):
    if len(arr) < 2:
        return [-1]
    arr.remove(min(arr))
    return arr


if __name__ == "__main__":
    i = [4, 3, 2, 1]
    print(solution(i))
