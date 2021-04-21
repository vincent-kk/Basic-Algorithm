def solution(n: int) -> int:
    """[summary]
    자연수 n이 주어질 때, 다음 큰 수를 구하시오
    다음 큰 수:
      1) n보다 큰 자연수
      2) n과 다음 큰 수는 2진수 변환시 1의 갯수가 같다
      3) 1)2)를 만족하는 가장 작은 자연수
    Args:
        n (int): 10^6 이하의 자연수

    Returns:
        int: n의 다음 큰 수
    """

    target = sum(map(int, format(n, "b")))
    i = n + 1
    while True:
        if target == sum(map(int, format(i, "b"))):
            return i
        i += 1


if __name__ == "__main__":
    i = 78
    print(solution(i))