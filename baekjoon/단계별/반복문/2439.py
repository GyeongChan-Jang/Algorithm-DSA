import sys
sys.stdin = open(
    "/Users/jang-gyeongchan/Desktop/Develop/algorithm/baekjoon/input.txt", "r")

count = int(input())
string = ''


for v in range(1, count+1):
    print(' ' * (count - v) + '*' * v)
