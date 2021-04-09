from typing import List


def solution(nums: List[int]):
    length = len(nums)
    category = set(nums)
    if len(category) > length / 2:
        return int(length / 2)
    else:
        return len(category)


if __name__ == "__main__":
    i = [3, 3, 3, 2, 2, 4]
    print(solution(i))
