from typing import List


def solution(prices: List[int]) -> List[int]:
    length = len(prices)
    answer = [0] * length
    stack = []

    for i, p in enumerate(prices):
        if len(stack) == 0:
            stack.append((i, p))
        else:
            while len(stack) > 0 and stack[-1][1] > p:
                price = stack.pop()
                answer[price[0]] = i - price[0]
            stack.append((i, p))

    for i, p in stack:
        answer[i] = length - i - 1

    return answer


if __name__ == "__main__":
    inp = [1, 2, 3, 2, 3]
    print(solution(inp))