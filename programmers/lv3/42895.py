def solution(N: int, number: int):
    if N == number:
        return 1

    # 연속된 N으로 생성할 수 있는 숫자를 모두 만들어둠
    sample = [set([int(str(N) * i)]) for i in range(1, 9)]

    # 모든 숫자에 대해서 가능한 조합을 생성
    for i in range(8):
        for j in range(i):
            for op1 in sample[j]:
                for op2 in sample[i - j - 1]:
                    sample[i].add(op1 + op2)
                    sample[i].add(op1 - op2)
                    sample[i].add(op1 * op2)
                    if op2:
                        sample[i].add(op1 // op2)
            # 타겟 숫자가 발견되면 정지
            if number in sample[i]:
                return i + 1

    # 위 반복문을 통과해서 찾지 못하면 8개 이상 사용해야 하는 경우
    return -1


if __name__ == "__main__":
    i = 5
    n = 12
    print(solution(i, n))
