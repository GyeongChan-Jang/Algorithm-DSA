import sys
sys.stdin = open(
    "/Users/jang-gyeongchan/Desktop/Develop/algorithm/baekjoon/input.txt", "r")


arrLength, target = map(int, input().split())
arr = list(map(int, input().split()))
answer = []

# 숫자 리스트를 문자열로 합치는 방법
# 1. print 사용
# for i in range(arrLength):
#     if arr[i] < target:
#         print(arr[i], end=' ')

# 2. for 사용
for i in range(arrLength):
    if arr[i] < target:
        answer.append(arr[i])

print(' '.join(str(num) for num in answer))
