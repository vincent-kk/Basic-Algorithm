from typing import List


def solution(n: int, times: List[int]):
    left, right = 1, max(times) * n
    while left + 1 < right:
        pivot = (left + right) // 2

        people = 0
        for time in times:
            people += pivot // time
            if people >= n:
                break

        if people < n:
            left = pivot
            # 최소값을 구하고 있기 때문에, 하계값은 항상 불가능한 값이어야 한다
        else:  # people == n
            right = pivot
            # 최소값을 구하고 있기 때문에, 상계값이 항상 가능한 값이어야 한다

    return right


# def solution(n: int, times: List[int]):
#     left, right = 1, n * max(times)
#     answer = 0
#     while left + 1 < right:
#         pivot = (right + left) // 2
#         people = 0
#         for time in times:
#             people += pivot // time
#             if people >= n:
#                 break
#         if people < n:
#             left = pivot
#         else:
#             answer = pivot
#             right = pivot

#     return answer


if __name__ == "__main__":
    n = 6
    time = [7, 10]
    print(solution(n, time))
