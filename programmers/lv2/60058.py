def solution(p: str) -> str:
    def check(s: str) -> bool:
        stack = []
        for c in s:
            if c == "(":
                stack.append(c)
                continue
            if c == ")":
                if stack and stack[-1] == "(":
                    stack.pop()
                else:
                    return False
        return True

    def do(s: str) -> str:
        if not s:
            return ""
        l, r = 0, 0
        i = 1
        for j, c in enumerate(s):
            if c == "(":
                l += 1
            elif c == ")":
                r += 1
            if l == r:
                i = j + 1
                break
        u = s[:i]
        v = s[i:]

        if check(u):
            return u + do(v)
        else:
            return (
                "(" + do(v) + ")" + "".join(["(" if c == ")" else ")" for c in u[1:-1]])
            )

    return do(p)


if __name__ == "__main__":
    i = "()))((()"
    print(solution(i))