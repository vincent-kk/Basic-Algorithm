def solution(array, commands):
    answer = []
    for s, e, i in commands:
        temp = sorted(array[s - 1 : e])
        answer.append(temp[i - 1])
    return answer


if __name__ == "__main__":
    i = [1, 5, 2, 6, 3, 7, 4]
    c = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
    print(solution(i, c))
