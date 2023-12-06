import sys
sys.stdin = open(
    "/Users/jang-gyeongchan/Desktop/Develop/algorithm/baekjoon/input.txt", "r")

basketCount, reverseCount = map(int, input().split())
basketList = [v+1 for v in range(basketCount)]

for _ in range(reverseCount):
    start, end = map(int, input().split())
    temp = basketList[start-1:end]
    temp.reverse()
    basketList[start-1:end] = temp

print(*basketList)

# reversed
N, M = map(int, input().split())

li = [i for i in range(N+1)]

for _ in range(M):
    i, j = map(int, input().split())
    li[i: j+1] = reversed(li[i: j+1])

li.remove(li[0])
print(*li)
