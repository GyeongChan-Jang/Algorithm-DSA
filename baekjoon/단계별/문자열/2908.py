import sys
sys.stdin = open(
    "/Users/jang-gyeongchan/Desktop/Develop/algorithm/baekjoon/input.txt", "r")

a, b = map(str, input().split())
arr = list(a)
arr.reverse()
a = ''.join(arr)

arr2 = list(b)
arr2.reverse()
b = ''.join(arr2)

answer = max(int(a), int(b))
print(answer)
