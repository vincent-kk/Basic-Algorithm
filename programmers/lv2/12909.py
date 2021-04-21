def solution(s: str) -> bool:
    stack = []
    left = 0
    right = 0
    for c in s:
        if not stack:
            if c == ")":
                return False
            stack.append(c)
            left += 1
            continue
        if c == ")":
            if stack[-1] == "(":
                stack.pop()
                right += 1
            else:
                return False
        else:
            stack.append(c)
            left += 1
    return left == right


if __name__ == "__main__":
    # i = "(())()"
    i = ")()("
    print(solution(i))
