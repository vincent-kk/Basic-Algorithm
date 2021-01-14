from typing import List


class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int):
        row, column = len(mat), len(mat[0])

        answer: List[List[int]] = [[0]*column for _ in range(row)]
        for i in range(K+1 if K+1 < row else row):
            answer[0][0] += sum(mat[i][0:K+1 if K+1 < column else column])

        for r in range(row):
            for c in range(column):
                if r == 0 and c == 0:
                    continue
                if c == 0:
                    end = column if c+K+1 > column else c+K+1
                    answer[r][c] = answer[r-1][c] - \
                        (0 if r-K-1 < 0 else sum(mat[r-K-1][0:end])) + \
                        (0 if r+K > row - 1 else sum(mat[r+K][0:end]))
                else:
                    start = 0 if r-K < 0 else r-K
                    end = row if r+K+1 > row else r+K+1

                    leave = 0
                    arrive = 0

                    if c-K-1 >= 0:
                        for i in range(start, end):
                            leave += mat[i][c-K-1]
                    if c+K < column:
                        for i in range(start, end):
                            arrive += mat[i][c+K]

                    answer[r][c] = answer[r][c-1] - leave + arrive
        return answer


s = Solution()
mat: List[List[int]] = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
s.matrixBlockSum(mat, 2)
