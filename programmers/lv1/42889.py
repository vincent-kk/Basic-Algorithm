from typing import List
from collections import defaultdict


def solution(N: int, stages: List[int]):
    """[summary]
    스테이지 실패율을 지정하는 모듈
    실패율 : 스테이지에 도달했으나 클리어하지 못한 사람의 수 / 스테이지에 도달한 사람의 수

    Args:
        N (int): 전체 스테이지 수 [1,500]
        stages (List[int]): 게임을 이용하는 현재 사용자가 멈춰있는 스테이지 번호 l=[2,200000] e=[1,N+1]
        단, e=N+1은 마지막 스테이지까지 클리어한 사용자
        실패율이 같으면 작은 번호의 스테이지가 위에 오도록
        스테이지에 도달한 사용자가 없는 경우 실패율은 0

    Returns:
        List[int] : 실패율이 높은 스테이지부터 내림차순 정렬된 스테이지
    """

    user_in_stage = defaultdict(int)
    user_reach_stage = defaultdict(int)
    stages.sort(reverse=True)

    for s in stages:
        user_in_stage[s] += 1
    accumulate = 0
    for s in set(stages):
        accumulate += user_in_stage[s]
        user_reach_stage[s] = accumulate
    answer = []

    for i in range(1, N + 1):
        if i not in user_in_stage or i not in user_reach_stage:
            answer.append((i, 0))
        else:
            answer.append((i, user_in_stage[i] / user_reach_stage[i]))

    return answer


if __name__ == "__main__":
    i = 5
    s = [2, 1, 2, 6, 2, 4, 3, 3]
    print(solution(i, s))
