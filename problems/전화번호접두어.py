def solution(phone_book):
    # 1. Hash map을 만든다.
    hash_map = {}
    for number in phone_book:
        hash_map[number] = 1

    # 2. 접두어가 Hash map에 존재하는지 찾는다.
    for phone_number in phone_book:
        prefix = ''
        for number in phone_number:
            prefix += number
            # 접두어 찾기
            if prefix in hash_map and prefix != phone_number:
                return False
    return True


print(solution(["6", "12", "6789"]))
