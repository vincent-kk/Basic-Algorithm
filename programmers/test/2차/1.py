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
    binery = list("0" + format(n, "b"))
    prev = 0
    for i in range(len(binery) - 1, -1, -1):
        if int(binery[i]) != prev:
            if binery[i] == "0":
                next_bin = binery[:i] + [binery[i + 1], binery[i]]
                if i + 2 < len(binery):
                    next_bin += reversed(binery[i + 2 :])
                break
            else:
                prev = 1
    return int("".join(next_bin), 2)


if __name__ == "__main__":
    i = 78
    print(solution(i))