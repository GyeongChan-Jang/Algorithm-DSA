import sys
sys.stdin = open(
    "/Users/jang-gyeongchan/Desktop/Develop/algorithm/baekjoon/input.txt", "r")

up, down, height = map(int, input().split())

if ((height - down) % (up - down) == 0):
    print((height - down)//(up - down))
else:
    print((height - down)//(up - down)+1)

# 시간초과
# day = 0
# distance = 0

# while True:
#     day += 1
#     distance += up
#     if distance == height:
#         print(day)
#         break
#     distance -= down
