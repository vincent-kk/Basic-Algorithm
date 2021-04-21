from typing import List
import heapq


def solution(people: List[int], limit: int) -> int:
    """[summary]
    사람들의 몸무게와 보트의 적재한계랑으로 필요한 최소보트수를 산출
    Args:
        people (List[int]): 사람들의 몸무게, l:[1:50000], e:[40:240]
        limit (int): 구명보트 제한 무게, lim:[40:240]
        단, 보트의 제한무게는 사람들 중 최대 무게보다 크게 주어지므로, 구하지 못하는 사람은 없다.
    Returns:
        int: 필요한 보트의 최소값
    """
    boats = []
    people.sort(reverse=True)
    answer = 0
    for person in people:
        if not boats:
            heapq.heappush(boats, -(limit - person))
            answer += 1
            continue

        if person + boats[0] > 0:
            heapq.heappush(boats, -(limit - person))
            answer += 1
        else:
            heapq.heappop(boats)
    return answer


if __name__ == "__main__":
    p, l = [70, 50, 80, 50], 100
    print(solution(p, l))
