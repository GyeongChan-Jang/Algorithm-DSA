import sys
sys.stdin = open(
    "/Users/jang-gyeongchan/Desktop/Develop/algorithm/baekjoon/input.txt", "r")

table = [list(map(int, input().split())) for _ in range(9)]


max = 0
X, Y = 0, 0

for row in range(9):
    for col in range(9):
        if table[row][col] >= max:
            max = table[row][col]
            X = row + 1
            Y = col + 1

print(max)
print(X, Y)
