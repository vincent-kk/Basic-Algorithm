from typing import List
from collections import defaultdict
import heapq


def solution(tickets: List[List[str]]) -> List[str]:
    """[summary]
    항공권을 모두 이용하여 이용경로 작성
    항상 인천'ICN'에서 시작
    모두 이용이기 때문에 아마도 DFS가 아닐지
    Args:
        tickets (List[List[str]]): 티켓 배열 (A->B: A에서 B로 가는 항공권)
        모든 공항은 3글자 공항명
        공항 수는 3~10^4
        모든 항공권 사용해야함
        가능한 경로가 2개일 경우 알파벳 순서가 앞서는 것을 리턴

    Returns:
        List[str]: [description]
    """
    path = []

    edges = defaultdict(list)
    check = defaultdict(bool)
    for s, d in tickets:
        heapq.heappush(edges[s], d)
    start = "ICN"

    # # do dfs
    # while len(stack) > 0:
    #     this = stack[-1]
    #     remain = False
    #     while edges[this]:
    #         direction = heapq.heappop(edges[this])
    #         path.append(direction)
    #         stack.append(direction)
    #         remain = True
    #         break
    #     if not remain:
    #         stack.pop()

    def dfs_re(this):
        check[this] = True
        path.append(this)
        temp = []
        while edges[this]:
            direction = heapq.heappop(edges[this])
            temp.append(direction)
            dfs_re(direction)

    dfs_re(start)

    return path


if __name__ == "__main__":
    t = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]

    print(solution(t))