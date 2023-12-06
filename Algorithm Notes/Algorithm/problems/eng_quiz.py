# '8zerothree2' → 8032
# 'seven73nine' → 7739
# 'two53eightfour' → 25384
s1 = '8zerothree2'
s2 = 'seven73nine'
s3 = 'two53eightfour'


def solution(s):
    num_dict = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }

    for str in num_dict:
        s = s.replace(str, num_dict[str])

    answer = int(s)
    return answer


print(solution(s1))
print(solution(s2))
print(solution(s3))
