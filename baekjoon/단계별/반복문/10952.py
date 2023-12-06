import sys
sys.stdin = open(
    "/Users/jang-gyeongchan/Desktop/Develop/algorithm/baekjoon/input.txt", "r")

while True:
    a, b = map(int, input().split())
    if (a == 0 and b == 0):
        break
    else:
        print(a+b)
