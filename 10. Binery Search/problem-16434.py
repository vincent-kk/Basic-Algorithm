import sys
from typing import List

input = sys.stdin.readline


def solution(N: int, hAtk: int, dongeon: List[List[int]]):
    low = 1
    high = sum([(r[2] // hAtk) * r[1] if r[0] == 1 else 0 for r in dongeon]) + 1

    optimal = high

    while high > low:
        pivot = (high + low) // 2
        life = pivot
        atk = hAtk
        for type, dAtk, dHp in dongeon:
            if type == 1:
                turn = dHp // atk
                if dHp % atk == 0:
                    turn -= 1
                life -= turn * dAtk
                if life <= 0:
                    break
            else:
                atk += dAtk
                life = pivot if life + dHp > pivot else (life + dHp)

        if life > 0:
            high = pivot
            optimal = high if optimal > high else optimal
        else:
            low = pivot + 1

    return optimal


if __name__ == "__main__":
    N, Hatk = map(int, input().split())
    dongeon = [list(map(int, input().split())) for _ in range(N)]
    print(solution(N, Hatk, dongeon))
