# 별 찍기 - 7
import sys
sys.stdin = open(
    "/Users/jang-gyeongchan/Desktop/Develop/algorithm/baekjoon/input.txt", "r")

n = int(input())

for i in range(1, n):
    print(' '*(n-i)+'*'*(2*i-1))

for j in range(n, 0, -1):
    print(' '*(n-j)+'*'*(2*j-1))
