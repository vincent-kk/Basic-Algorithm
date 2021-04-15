from typing import List
from collections import deque

# any? any 함수에 대해서 알아보자
def solution(p: List[int], l: int):
    answer = 0
    printer_queue = deque(enumerate(p))

    while printer_queue:
        maxp = max(printer_queue, key=lambda x: x[1])
        while printer_queue[0][1] < maxp[1]:
            printer_queue.rotate(-1)
        paper = printer_queue.popleft()
        answer += 1
        if paper[0] == l:
            break
    return answer


if __name__ == "__main__":
    p = [2, 1, 3, 2]
    l = 2
    print(solution(p, l))
