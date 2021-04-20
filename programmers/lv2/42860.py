from string import ascii_uppercase


def solution(name: str):
    length = len(ascii_uppercase)
    characters = dict(zip(ascii_uppercase, range(length)))

    name = [min(characters[ch], length - characters[ch]) for ch in name]

    progress_list = name[1:]
    progress = name[0]
    for i in range(len(progress_list)):
        if sum(progress_list) == 0:
            break
        progress += progress_list[i] + 1
        progress_list[i] = 0

    reverse_list = name[1:]
    reverse = name[0]
    for i in range(len(reverse_list) - 1, -1, -1):
        if sum(reverse_list) == 0:
            break
        reverse += reverse_list[i] + 1
        reverse_list[i] = 0

    return min(progress, reverse)


if __name__ == "__main__":
    n = "JAN"
    print(solution(n))