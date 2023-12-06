import sys
sys.stdin = open(
    "/Users/jang-gyeongchan/Desktop/Develop/algorithm/baekjoon/input.txt", "r")

str = input()
alphabet = 'abcdefghijklmnopqrstuvwxyz'

for v in alphabet:
    print(str.find(v), end=' ')

# 인덱스를 활용한 풀이
str = list(input())
alphabet = 'abcdefghijklmnopqrstuvwxyz'

for v in alphabet:
    if v in str:
        print(str.index(v), end=' ')
    else:
        print(-1, end=' ')
