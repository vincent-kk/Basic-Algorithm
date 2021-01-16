from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]):
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        column = len(matrix[0])
        answer = [[0]*column for _ in range(row)]
        size = row - 1

        for i in range(row):
            for j in range(column):
                answer[i][j] = matrix[size-j][i]
        matrix = answer
        return matrix


s = Solution()
i = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
o = s.rotate(i)

for row in o:
    for e in row:
        print(e, end=' ')
    print()
