def solution(n: int) -> str:
    stack = []
    n -= 1
    while n >= 3:
        stack.append(str(2 ** (n % 3)))
        n = (n // 3) - 1

    stack.append(str(2 ** (n % 3)))

    return "".join(reversed(stack))


if __name__ == "__main__":
    i = 3
    print(solution(i))