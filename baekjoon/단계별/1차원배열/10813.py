import sys
sys.stdin = open(
    "/Users/jang-gyeongchan/Desktop/Develop/algorithm/baekjoon/input.txt", "r")


totalBasket, count = map(int, input().split())
basketList = [v+1 for v in range(totalBasket)]

for _ in range(count):
    a, b = map(int, input().split())

    basketList[a-1], basketList[b-1] = basketList[b-1], basketList[a-1]

print(*basketList)
