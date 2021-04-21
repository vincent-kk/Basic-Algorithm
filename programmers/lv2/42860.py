from string import ascii_uppercase


def solution(name: str):
    length = len(ascii_uppercase)
    characters = dict(zip(ascii_uppercase, range(length)))

    name = [min(characters[ch], length - characters[ch]) for ch in name]
    name_len = len(name)
    move = 0
    this = 0
    while True:
        move += name[this]
        name[this] = 0
        progress = this
        progress_move = 0

        if not sum(name):
            break

        for i in range(1, name_len):
            progress_move += 1
            if name[(this + i) % name_len]:
                progress = (this + i) % name_len
                break

        reverse = this
        reverse_move = 0
        for i in range(name_len - 1, 0, -1):
            reverse_move += 1
            if name[(this + i) % name_len]:
                reverse = (this + i) % name_len
                break

        if progress_move > reverse_move:
            this = reverse
            move += reverse_move
        else:
            this = progress
            move += progress_move

    return move


if __name__ == "__main__":
    n = "BABAAAAB"
    print(solution(n))