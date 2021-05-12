from typing import List


def solution(n: int, times: List[int]):
    left, right = 1, n * max(times)
    answer = 0
    while left < right - 1:
        pivot = (right + left) // 2
        people = 0
        for time in times:
            people += pivot // time
            if people >= n:
                break
        if people < n:
            left = pivot + 1
        else:
            answer = pivot
            right = pivot - 1

    return answer


if __name__ == "__main__":
    n = 6
    time = [7, 10]
    print(solution(n, time))
