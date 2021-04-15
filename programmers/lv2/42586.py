from typing import List
from collections import defaultdict, deque
import heapq


def solution(progresses: List[int], speeds: List[int]) -> List[int]:
    """[summary]
    기능 개선 작업 진행중
    각 기능은 진도가 100%일때 서비스 반영
    후행 기능이 선행 기능보다 먼저 개발될 수도 있고, 이 경우에는 선행기술의 개발 완료와 동시에 함께 배포됨
    Args:
        progresses (List[int]): 먼저 배포되어야 하는 순서대로 개발 진행도
        speeds (List[int]): 기능별 개발 속도

    Returns:
        List[int]: 각 배포마다 몇 개가 배포되는지. 배포는 하루에 1회 진행
    """
    release_queue = []
    projects = dict((i, p) for i, p in enumerate(progresses))
    delay = []
    release_turn = 0
    while projects:
        done = []
        for i in projects.keys():
            projects[i] += speeds[i]
            if projects[i] > 99:
                done.append(i)

        done.sort(reverse=True)
        for i in done:
            heapq.heappush(delay, i)
            if i <= release_turn:
                r = 0
                while len(delay) > 0 and delay[0] <= release_turn:
                    heapq.heappop(delay)
                    release_turn += 1
                    r += 1
                release_queue.append(r)
            del projects[i]

    return release_queue

    """
    def solution(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds):
        if len(Q)==0 or Q[-1][0]<-((p-100)//s):
            Q.append([-((p-100)//s),1])
        else:
            Q[-1][1]+=1
    return [q[1] for q in Q]
    """


if __name__ == "__main__":
    p = [99, 99, 99, 98, 98, 99]
    s = [1, 1, 1, 1, 1, 1]
    print(solution(p, s))
