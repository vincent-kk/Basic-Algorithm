from typing import List


def solution(seoul: List[str]):
    return f"김서방은 {seoul.index('Kim')}에 있다"


if __name__ == "__main__":
    i = ["Jane", "Kim"]
    print(solution(i))
