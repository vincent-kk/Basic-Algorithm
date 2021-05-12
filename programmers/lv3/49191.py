from typing import List
from collections import defaultdict


def solution(n: int, results: List[List[int]]) -> int:
    """
    n명의 권투선수가 참가하는 대회
    선수의 수와 경기 결과를 담은 2차원 배열이 주어진다
    그것을 바탕으로 정확하게 순서를 매길 수 있는 선수의 수를 구하시오

    Args:
        n (int): 선수의 수
        results (List[List[int]]): 경기 결과. [A,B]는 A가 B를 이겼다는 의미이다

    Returns:
        int: 정확하게 순위를 매길 수 있는 선수의 수
    """

    winners, losers = defaultdict(set), defaultdict(set)

    for i in range(1, n + 1):
        for winner, loser in results:
            if winner == i:
                winners[i].add(loser)
            if loser == i:
                losers[i].add(winner)
        for winner in losers[i]:
            winners[winner].update(winners[i])
        for loser in winners[i]:
            losers[loser].update(losers[i])

    count = 0

    for i in range(1, n + 1):
        if len(winners[i]) + len(losers[i]) == n - 1:
            count += 1

    return count


if __name__ == "__main__":
    n, r = 5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
    print(solution(n, r))
