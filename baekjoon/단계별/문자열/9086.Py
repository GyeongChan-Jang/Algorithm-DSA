import sys
sys.stdin = open(
    "/Users/jang-gyeongchan/Desktop/Develop/algorithm/baekjoon/input.txt", "r")

count = int(input())

for _ in range(count):
    str = input()
    print(str[0] + str[-1])
