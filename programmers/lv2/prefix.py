def solution(phone_book):
    sorted_phone_book = sorted(phone_book)
    prefix = None
    for phone in sorted_phone_book:
        if prefix and phone.startswith(prefix):
            return False
        else:
            prefix = phone

    return True


if __name__ == "__main__":
    i = ["119", "97674223", "1195524421"]
    print(solution(i))
