from typing import List


def fmax(x, y): return x if x > y else y
def fmin(x, y): return x if x < y else y


def isSquareMatrix(matrix, row, column, size):
    ones = 0
    # height = 0
    # width = 0
    try:
        for r in range(row, row+size):
            for c in range(column, column+size):
                ones += matrix[r][c]
        # width = sum(matrix[row+size][column:column+size+1])
        # for r in matrix[row:row+size+1]:
        #     height += r[column]
    except:
        return False
    return size*size == ones
    # return height+width == size * 2


class Solution:
    def countSquares(self, matrix: List[List[int]]):
        row = len(matrix)
        column = len(matrix[0])
        maximumSubMatrix = fmin(row, column)
        output = 0

        for i in range(row):
            for j in range(column):
                for s in range(1, maximumSubMatrix - fmin(i-1, j-1)):
                    if(isSquareMatrix(matrix, i, j, s)):
                        output += 1
                    else:
                        break
        return output


mat = [
    [0, 1, 1, 1],
    [1, 1, 1, 1],
    [0, 1, 1, 1]
]

s = Solution()
print(s.countSquares(mat))
