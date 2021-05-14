from typing import List
import heapq


def solution(operations: List[str]) -> List[int]:
    """
    최소값과 최대값을 모두 찾을 수 있는 힙을 구성하는 문제
    이게 근데 원리상 가능한가?
    힙트리는 그런 구조가 아닐텐데?

    Args:
        operations (List[str]): 삽입/삭제 연산에 대한 기록

    Returns:
        List[int]: 힙에 남아있는 최소값과 최대값을 리스트로 반환
    """
    min_heap = []
    max_heap = []
    for op in operations:
        cmd, value = op.split()
        value = int(value)
        if cmd == "I":
            heapq.heappush(min_heap, value)
            heapq.heappush(max_heap, -value)
        if cmd == "D":
            if not min_heap or not max_heap:
                continue
            if value > 0:
                heapq.heappop(max_heap)
                if not max_heap or -max_heap[0] < min_heap[0]:
                    min_heap, max_heap = [], []
            else:
                heapq.heappop(min_heap)
                if not min_heap or -max_heap[0] < min_heap[0]:
                    min_heap, max_heap = [], []

    if not min_heap or not max_heap:
        return (0, 0)
    return (-max_heap[0], min_heap[0])


if __name__ == "__main__":
    o = ["I 7", "I 5", "I -5", "D -1"]
    print(solution(o))