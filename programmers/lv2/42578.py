from typing import List
from collections import defaultdict


def solution(clothes: List[List[str]]) -> int:
    """[summary]
    의상 조합 찾기
    Args:
        clothes (List[List[str]]): 의상들 입력 [1:30]
        cloth := [<name>, <type>]
        사람은 최소 1개 이상의 옷을 입음
    Returns:
        int: 만들 수 있는 의상의 조합 수
    """
    closet = defaultdict(int)
    for name, type in clothes:
        closet[type] += 1
    answer = 1
    for i in closet.values():
        answer *= i + 1
    return answer - 1


if __name__ == "__main__":
    i = [["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]
    print(solution(i))
