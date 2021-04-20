def solution(s: str) -> int:
    length = len(s)
    global_min = length
    for i in range(1, (length // 2) + 1):
        l = [s[j : j + i] for j in range(0, length, i)]
        local_min = 0
        prev = ""
        count = 1
        for ch in l:
            if ch == prev:
                count += 1
            else:
                if count > 1:
                    local_min += len(str(count))
                prev = ch
                local_min += len(ch)
                count = 1
        if count > 1:
            local_min += len(str(count))
        global_min = local_min if local_min < global_min else global_min

    return global_min


if __name__ == "__main__":
    i = "ababcdcdababcdcd"
    print(solution(i))