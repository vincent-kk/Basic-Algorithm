def solution(string: str):
    stack = []
    for s in string:
        if len(stack) == 0:
            stack.append(s)
        else:
            if stack[-1] == s:
                stack.pop()
            else:
                stack.append(s)
    return 0 if len(stack) else 1


if __name__ == "__main__":
    i = "baabaa"
    print(solution(i))
