# 단어 공부
import sys
sys.stdin = open(
    "/Users/jang-gyeongchan/Desktop/Develop/algorithm/baekjoon/input.txt", "r")

word = input().lower()
word_list = list(set(word))
cnt = []

for v in word_list:
    cnt.append(word.count(v))

if cnt.count(max(cnt)) > 1:
    print('?')
else:
    print(word_list[cnt.index(max(cnt))].upper())


# count_dict = {}
# answer = []

# for i in range(len(string)):
#     if string[i] in count_dict:
#         count_dict[string[i]] += 1
#         answer.append(count_dict[string[i]])
#     else:
#         count_dict[string[i]] = 1

# max_count = max(answer)

# if answer.count(max_count) > 1:
#     print('?')
# else:
#     print(str(max(count_dict.values())).upper())
