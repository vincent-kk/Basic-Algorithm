from collections import defaultdict
import heapq


def solution(N, road, K):
    edges = defaultdict(dict)
    for s, d, c in road:
        if d in edges[s] and s in edges[d]:
            edges[s][d] = min(c, edges[s][d])
            edges[d][s] = min(c, edges[d][s])
        else:
            edges[s][d] = c
            edges[d][s] = c

    distances = defaultdict(lambda: K + 1)
    start = 1
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])

    while queue:  # queue에 남아 있는 노드가 없으면 끝
        current_distance, current_destination = heapq.heappop(
            queue
        )  # 탐색 할 노드, 거리를 가져옴.

        if (
            distances[current_destination] < current_distance
        ):  # 기존에 있는 거리보다 길다면, 볼 필요도 없음
            continue

        for new_destination, new_distance in edges[current_destination].items():
            distance = current_distance + new_distance  # 해당 노드를 거쳐 갈 때 거리
            if distance > K:
                continue
            if distance < distances[new_destination]:  # 알고 있는 거리 보다 작으면 갱신
                distances[new_destination] = distance
                heapq.heappush(
                    queue, [distance, new_destination]
                )  # 다음 인접 거리를 계산 하기 위해 큐에 삽입

    return len(distances)


if __name__ == "__main__":
    n = 5
    i = [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]]
    k = 3
    print(solution(n, i, k))