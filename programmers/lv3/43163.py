from typing import List
from collections import defaultdict, deque


def solution(begin: str, target: str, words: List[str]) -> int:
    """
    begin에서 target으로 가는 가장 짧은 경로를 찾는 문제
    한번에 한 글자만 변화시킬 수 있다
    간선을 어떻게 설정하느냐가 포인트

    Args:
        begin (str): 시작 노드(시작 단어)
        target (str): 목표 노드(목표 단어)
        words (List[str]): 노드(변환할 수 있는 단어)

    Returns:
        int: 시작부터 목표까지의 최소 변환수
    """
    if target not in words:
        return 0
    edges = defaultdict(list)
    words = [begin] + words
    for s in words:
        for d in words:
            diff = 0
            for sc, dc in zip(s, d):
                if sc != dc:
                    diff += 1
            if diff == 1:
                edges[s].append(d)
    visited = set()
    queue = deque([(begin, 0)])
    while queue:
        word, cost = queue.popleft()
        for next in edges[word]:
            if next == target:
                return cost + 1
            if next in visited:
                continue
            visited.add(next)
            queue.append((next, cost + 1))

    return 0


if __name__ == "__main__":
    b, t, w = "hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]
    print(solution(b, t, w))
