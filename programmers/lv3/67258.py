from typing import List
from collections import defaultdict


def solution(gems: List[str]) -> List[int]:
    """
    어퍼치는 물건을 살때 진열대 특정 범위의 물건을 모두 산다
    이때 진열대에 있는 모든 물건이 1개 이상 포함되는 연속된 배열의 범위를 구하시오

    Args:
        gems (List[str]): 상품의 종류가 진열된 순서대로 포함되어 있는 배열

    Returns:
        List[int]: 모든 종류의 상품을 포함할 수 있는 가장 짧은 부분배열의 시작지점과 끝지점(양 끝 지점을 포함한다)
    """
    overall = len(set(gems))
    length = len(gems)
    left, right = 0, 0
    basket = defaultdict(int)
    global_min = [1, length]

    while right < length:

        while right < length and len(basket) < overall:
            basket[gems[right]] += 1
            right += 1

        while len(basket) == overall:
            if basket[gems[left]] == 1:
                global_min = (
                    [left + 1, right]
                    if right - left - 1 < global_min[1] - global_min[0]
                    else global_min
                )
                del basket[gems[left]]
                left += 1
                break
            basket[gems[left]] -= 1
            left += 1

    return global_min


if __name__ == "__main__":
    g = ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]
    print(solution(g))