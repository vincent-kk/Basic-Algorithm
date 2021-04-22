def solution(dirs):
    roads = set()
    directions = {"U": (0, 1), "D": (0, -1), "L": (-1, 0), "R": (1, 0)}
    prev_pos = (0, 0)
    for d in dirs:
        dx, dy = directions[d]
        next_pos = (prev_pos[0] + dx, prev_pos[1] + dy)
        if not (-6 < next_pos[0] < 6 and -6 < next_pos[1] < 6):
            continue
        roads.add(tuple(sorted([prev_pos, next_pos])))
        prev_pos = next_pos
    return len(roads)


if __name__ == "__main__":
    i = "ULURRDLLU"
    print(solution(i))
