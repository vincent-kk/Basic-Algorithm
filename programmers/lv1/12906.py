from typing import List


def solution(arr: List[int]):
    answer = []
    prev = -1
    for element in arr:
        if prev != element:
            answer.append(element)
            prev = element
    return answer


if __name__ == "__main__":
    i = [1, 1, 3, 3, 0, 1, 1]
    print(solution(i))
