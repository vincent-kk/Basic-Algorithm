from typing import List


def solution(arr1: List[List[int]], arr2: List[List[int]]):
    for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            arr1[i][j] += arr2[i][j]
    return arr1


if __name__ == "__main__":
    i1 = [[1, 2], [2, 3]]
    i2 = [[3, 4], [5, 6]]
    print(solution(i1, i2))
