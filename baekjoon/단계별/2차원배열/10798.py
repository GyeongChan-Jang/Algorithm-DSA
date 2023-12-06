import sys
sys.stdin = open(
    "/Users/jang-gyeongchan/Desktop/Develop/algorithm/baekjoon/input.txt", "r")

arr = [input() for _ in range(5)]

max_length = max(len(word) for word in arr)

result = ''

for i in range(max_length):
    for j in range(5):
        if i < len(arr[j]):
            print(arr[j][i], end='')
