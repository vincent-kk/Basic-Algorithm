def solution(phone_number: str):
    return "*" * (len(phone_number) - 4) + phone_number[-4:]


if __name__ == "__main__":
    i = "027778888"
    print(solution(i))