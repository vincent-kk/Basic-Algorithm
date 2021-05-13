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
    # key가 이긴 상대, key가 진 상대
    winners, losers = defaultdict(set), defaultdict(set)

    for i in range(1, n + 1):
        # 내가 이겼거나 진 상대를 나의 승리/패배 목록에 추가한다
        for winner, loser in results:
            if winner == i:
                winners[i].add(loser)
            if loser == i:
                losers[i].add(winner)
        # 내가 진 모든 상대의 승리목록에 나의 승리 목록을 추가한다
        for w in losers[i]:
            winners[w].update(winners[i])
        # 내가 이긴 모든 상대의 패배목록에 나에게 진 사람들을 추가한다
        for l in winners[i]:
            losers[l].update(losers[i])

    count = 0

    for i in range(1, n + 1):
        # 내가 이긴 사람의 수와 진 사람의 수가 나를 제외한 전체 사람의 수와 동일하다면 순위를 알 수 있다
        if len(winners[i]) + len(losers[i]) == n - 1:
            count += 1

    return count


if __name__ == "__main__":
    n, r = 5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
    print(solution(n, r))
