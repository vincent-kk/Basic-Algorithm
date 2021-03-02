import sys
from typing import List

input = sys.stdin.readline


def countPaper(N: int, paper: List[List]):
    def cutPaper(size: int, pr: int, pc: int):
        if size == 1:
            local_sum = [0, 0, 0]
            local_sum[paper[pr][pc] + 1] += 1
            return local_sum

        global_number = paper[pr][pc]
        for r in range(pr, pr + size):
            for c in range(pc, pc + size):
                if global_number != paper[r][c]:
                    global_number = None
                    break
            if global_number == None:
                break

        counter = [0, 0, 0]
        if global_number == None:
            step = size // 3
            for r in range(3):
                for c in range(3):
                    local_sum = cutPaper(step, pr + step * r, pc + step * c)
                    for i in range(3):
                        counter[i] += local_sum[i]
        else:
            counter[global_number + 1] += 1
        return counter

    return cutPaper(N, 0, 0)


N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
output = countPaper(N, paper)
for e in output:
    print(e)
