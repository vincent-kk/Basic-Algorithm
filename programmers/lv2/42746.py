from typing import List


def solution(numbers: List[int]) -> str:

    # max_len = max([len(str(n)) for n in numbers]) - 1

    # def key_function(n):
    # st = str(n)
    # if len(st) > 1:
    #     frac = st[1:].ljust(max_len, st[1:])
    # else:
    #     frac = st.ljust(max_len, st)
    # return st.ljust(max_len, st)

    # numbers.sort(key=key_function, reverse=True)
    # return "".join(map(str, numbers))

    # numbers = list(map(str, numbers))
    # length = len(numbers)
    # for i in range(length):
    #     for j in range(i + 1, length):
    #         if int(numbers[i] + numbers[j]) < int(numbers[j] + numbers[i]):
    #             numbers[i], numbers[j] = numbers[j], numbers[i]
    # return "".join(numbers)

    numbers = list(map(str, numbers))
    # 1000이하이므로, 3번 반복. str 비교이므로, 맨 앞 글자부터 대소비교
    # 패턴을 반복시키면(30:303030, 34:343434, 3:333) 정렬을 할 수 있음
    #  40 <> 403 : 원래대로는 40403이 되어야 하지만, 마지막 글자 반복으로 하면 4.000 4.033이 되서 403이 앞에 나옴
    numbers.sort(key=lambda n: n * 3, reverse=True)
    answer = "".join(numbers)
    return answer if int(answer) > 0 else "0"


if __name__ == "__main__":
    i = [3, 123, 34, 5, 9]
    print(solution(i))