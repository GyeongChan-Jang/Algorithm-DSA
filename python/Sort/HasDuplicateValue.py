def hasDuplicateValue_IndexError(list):
    existingNumbers = []
    for i in range(len(list)):
        if existingNumbers[list[i]] == 1:
            print('중복 있음!')
            return True
        else:
            # 파이썬에서 리스트의 특정 인덱스를 참조하려면
            # 해당 인덱스가 이미 존재해야함
            existingNumbers[list[i]] = 1
    print('중복 없음!')
    return False


def hasDuplicateValue(list):
    existingNumbers = set()
    for i in list:
        if i in existingNumbers:
            print('중복 있음!')
            return True
        else:
            existingNumbers.add(i)
    print('중복 없음!')
    return False


hasDuplicateValue([3, 1, 4, 5, 2, 3])
