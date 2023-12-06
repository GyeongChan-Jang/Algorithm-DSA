# 펠린드롬
import sys
sys.stdin = open(
    "/Users/jang-gyeongchan/Desktop/Develop/algorithm/baekjoon/input.txt", "r")

string = list(input())

if list(reversed(string)) == string:
    print(1)
else:
    print(0)
