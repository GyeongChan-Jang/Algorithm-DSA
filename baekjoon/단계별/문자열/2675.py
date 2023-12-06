import sys
sys.stdin = open(
    "/Users/jang-gyeongchan/Desktop/Develop/algorithm/baekjoon/input.txt", "r")

n = int(input())

for _ in range(n):
    count, string = input().split()
    for v in string:
        print(v * int(count), end='')
    print()
