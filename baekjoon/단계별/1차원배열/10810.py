import sys
sys.stdin = open(
    "/Users/jang-gyeongchan/Desktop/Develop/algorithm/baekjoon/input.txt", "r")


totalBasket, throwCount = map(int, input().split())
basketList = [0 for _ in range(totalBasket)]


for _ in range(throwCount):
    start, end, number = map(int, input().split())
    for v in range(start-1, end):
        basketList[v] = number
print(*basketList)
