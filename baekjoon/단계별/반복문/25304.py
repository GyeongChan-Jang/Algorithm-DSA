import sys
sys.stdin = open(
    "/Users/jang-gyeongchan/Desktop/Develop/algorithm/baekjoon/input.txt", "r")


total = int(input())
sum = 0

for _ in range(int(input())):
    price, count = map(int, input().split())
    sum += (price * count)

if total == sum:
    print('Yes')
else:
    print('No')
