from typing import List
import heapq


def solution(scoville: List[int], K: int) -> int:
    """[summary]
    맵게 만든다
    가장 맵지 않은 메뉴 2개를 선택
    가장 덜 매운 + 두번째로 덜 매운*2 = 새 메뉴 추가
    이렇게 섞어서 가장 안매운 메뉴가 k보다 맵게 하면 된다
    Args:
        scoville (List[int]): 메뉴의 맵기
        K (int): 목표 맵기

    Returns:
        int: 섞은 횟수
    """
    answer = 0
    l = len(scoville)
    heapq.heapify(scoville)
    while scoville[0] < K:
        if l < 2:
            return -1
        primery = heapq.heappop(scoville)
        secondary = heapq.heappop(scoville)
        heapq.heappush(scoville, primery + secondary * 2)
        answer += 1
        l -= 1
    return answer


if __name__ == "__main__":
    i, k = [1, 2, 3, 9, 10, 12], 7
    print(solution(i, k))
