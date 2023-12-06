import sys
sys.stdin = open(
    "/Users/jang-gyeongchan/Desktop/Develop/algorithm/baekjoon/input.txt", "r")

correct = [1, 1, 2, 2, 2, 8]
arr = list(int(v) for v in input().split())

answer = []

for i in range(len(correct)):
    answer.append(correct[i] - arr[i])

print(*answer)
