import sys
sys.stdin = open(
    "/Users/jang-gyeongchan/Desktop/Develop/algorithm/baekjoon/input.txt", "r")

while True:
    try:
        a, b = map(int, input().split())
        print(a + b)
    except:
        break
