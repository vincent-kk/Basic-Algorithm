def solution(citations):
    """[summary]
    인용횟수를 담은 배열이 주어지면 그걸 토대로 H-index를 산출
    Args:
        citations (List[int]): 논문별 인용 횟수 [1:1000], e:=[0:10000]

    Returns:
        int: 발표한 논문 n편 중 h번 이상 인용된 논문이 h편 이상이고, 나머지 논문이 h편 이하 인용되었을때, max(h)
    """
    h_index = 0

    for i, c in enumerate(sorted(citations, reverse=True)):
        if c < i + 1:
            break
        h_index += 1
    return h_index


if __name__ == "__main__":
    i = [3, 0, 6, 1, 5]
    print(solution(i))