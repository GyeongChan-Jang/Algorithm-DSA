import sys
sys.stdin = open(
    "/Users/jang-gyeongchan/Desktop/Develop/algorithm/baekjoon/input.txt", "r")
string = input().split(' ')

count = string.count('')

for _ in range(count):
    string.remove('')
print(len(string))
