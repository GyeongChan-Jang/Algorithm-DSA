import sys
sys.stdin = open(
    "/Users/jang-gyeongchan/Desktop/Develop/algorithm/baekjoon/input.txt", "r")

n = int(input())
line = 0
end = 0


# 1 -> 1/1
# 2 -> 1/2 2/1
# 3 -> 1/3 2/2 3/1
# 4 -> 1/4 2/3 3/2 4/1
# 5 -> 5/1 2/4 3/3 4/2 5/1

while n > line:
    n -= line
    line += 1

    if line % 2 == 0:
        top = n
        bottom = line - n + 1
    elif line % 2 == 1:
        top = line - n + 1
        bottom = n
print(f'{top}/{bottom}')
# 이해가 안감 어려움!!
