def solution(arr1, arr2):
    return [
        [sum([e1 * e2 for e1, e2 in zip(r1, r2)]) for r2 in (zip(*arr2))] for r1 in arr1
    ]


# def productMatrix(A, B):
#     return [
#         [sum(a * b for a, b in zip(A_row, B_col)) for B_col in zip(*B)] for A_row in A
#     ]


if __name__ == "__main__":
    a, b = [[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]]
    print(solution(a, b))
