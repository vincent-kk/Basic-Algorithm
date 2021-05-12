def solution(n, computers):
    def dfs(n, s, metrix, visited):
        stack = [s]
        visited.add(s)
        while stack:
            this = stack[-1]
            remove = True
            for i in range(n):
                if this == i:
                    continue
                if i in visited:
                    continue
                if metrix[this][i]:
                    visited.add(i)
                    stack.append(i)
                    remove = False
                    break
            if remove:
                stack.pop()

    answer = 0
    visited = set()

    for i in range(n):
        if i not in visited:
            dfs(n, i, computers, visited)
            answer += 1

    return answer


if __name__ == "__main__":
    n = 3
    c = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    print(solution(n, c))
