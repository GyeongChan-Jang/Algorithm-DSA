# 세탁소 사장 동혁 - 거스름돈(그리디)
import sys
sys.stdin = open(
    "/Users/jang-gyeongchan/Desktop/Develop/algorithm/baekjoon/input.txt", "r")

n = int(input())

for _ in range(n):
    money = int(input())
    for i in [25, 10, 5, 1]:
        print(money//i, end=' ')
        money = money % i
