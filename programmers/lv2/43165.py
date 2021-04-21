from typing import List


def solution(numbers: List[int], target: int) -> int:
    """
    n개의 음이 아닌 정수를 입력받음. 이 수를 적절히 더하거나 빼서 타겟 넘버를 만들려고 함
    이때 가능한 방법의 수를 구함

    Args:
        numbers (List[int]): 양의 정수, l = [2:20], e = [1:50]
        target (int): [1:1000]

    Returns:
        int: [description]
    """
    length = len(numbers)
    answer = 0

    def do(prev: int, i: int):
        if i < length:
            do(prev + numbers[i], i + 1)
            do(prev - numbers[i], i + 1)
        else:
            if prev == target:
                nonlocal answer
                answer += 1
            return

    do(0, 0)
    return answer


if __name__ == "__main__":
    n = [1, 1, 1, 1, 1]
    t = 3
    print(solution(n, t))
