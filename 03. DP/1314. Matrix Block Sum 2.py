from typing import List


def fmax(x, y): return x if x > y else y
def fmin(x, y): return x if x < y else y
def initzero(r, c): return [[0]*c for _ in range(r)]


class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int):
        row, column = len(mat), len(mat[0])
        mat = [[0] * (column + 1)] + [[0] + r for r in mat]
        answer = initzero(row, column)

        for i in range(1, row + 1):
            for j in range(1, column + 1):
                mat[i][j] += mat[i - 1][j] + mat[i][j - 1] - mat[i - 1][j - 1]

        for i in range(row):
            for j in range(column):
                r1, r2 = fmax(i - K, 0), fmin(i + K + 1, row)
                c1, c2 = fmax(j - K, 0), fmin(j + K + 1, column)
                answer[i][j] = mat[r2][c2] - \
                    mat[r2][c1] - mat[r1][c2] + mat[r1][c1]
        return answer


s = Solution()
mat: List[List[int]] = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
a = s.matrixBlockSum(mat, 1)

for r in a:
    for e in r:
        print(e, end=' ')
    print()
