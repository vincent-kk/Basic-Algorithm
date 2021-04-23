def solution(m, n, board):
    answer = 0
    removed = set()
    b = list(map(list, board))

    while True:
        removed.clear()

        # check removeable block
        for i in range(m - 1):
            for j in range(n - 1):
                if b[i][j] == "":
                    continue
                if b[i][j] == b[i + 1][j] == b[i][j + 1] == b[i + 1][j + 1]:
                    removed.add((i, j))
                    removed.add((i + 1, j))
                    removed.add((i, j + 1))
                    removed.add((i + 1, j + 1))
        # remove block
        for i, j in removed:
            b[i][j] = ""

        # add score
        answer += len(removed)

        # drop the blocks
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if not b[i][j]:
                    for z in range(i - 1, -1, -1):
                        if b[z][j]:
                            b[i][j] = b[z][j]
                            b[z][j] = ""
                            break
        if not removed:
            break
    return answer


if __name__ == "__main__":
    m, n, b = 7, 2, ["AA", "BB", "AA", "BB", "ZZ", "ZZ", "CC"]
    print(solution(m, n, b))
