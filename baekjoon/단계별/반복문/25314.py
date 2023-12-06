import sys
sys.stdin = open(
    "/Users/jang-gyeongchan/Desktop/Develop/algorithm/baekjoon/input.txt", "r")


count = int(input()) // 4


string = ""

for _ in range(count):
    string += 'long '

print(string + 'int')
