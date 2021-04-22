def solution(dirs):
    roads = set()
    directions = {"U": (0, 1), "D": (0, -1), "L": (-1, 0), "R": (1, 0)}
    x, y = 0, 0
    for d in dirs:
        dx, dy = directions[d]
        nx, ny = x + dx, y + dy
        if not (-6 < nx < 6 and -6 < ny < 6):
            continue
        roads.add((x, y, nx, ny))
        roads.add((nx, ny, x, y))
        x, y = nx, ny
    return len(roads) // 2


if __name__ == "__main__":
    i = "ULURRDLLU"
    print(solution(i))
