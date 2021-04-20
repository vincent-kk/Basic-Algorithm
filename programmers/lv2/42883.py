# from collections import deque


# def solution(n: str, k: int) -> str:
#     number = list(n)
#     l = len(number)
#     i = 0
#     num = [deque(), deque(number)]
#     while i < k:
#         local_max = 0
#         left, right = num[i % 2], num[(i + 1) % 2]
#         rm = ""
#         for n in range(l - i):
#             temp = right.popleft()
#             local_value = int("".join(left + right))
#             if local_value > local_max:
#                 local_max = local_value
#                 rm = temp
#             left.append(temp)
#         num[i % 2].remove(rm)
#         i += 1

#     return "".join(num[(i + 1) % 2] + num[i % 2])


def solution(number, k):
    answer = ""
    stack = []

    for i, num in enumerate(number):
        while k and len(stack) and num > stack[-1]:
            stack.pop()
            k -= 1
        if k == 0:
            stack += list(number[i:])
            break
        stack.append(num)
    else:
        if k != 0:
            stack = stack[:-k]

    answer = "".join(stack)

    return answer


if __name__ == "__main__":
    n = "4177252841"
    k = 4
    print(solution(n, k))
