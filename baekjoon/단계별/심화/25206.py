import sys
import math
sys.stdin = open(
    "/Users/jang-gyeongchan/Desktop/Develop/algorithm/baekjoon/input.txt", "r")

rating = ['A+', 'A0', 'B+', 'B0', 'C+', 'C0', 'D+', 'D0', 'F']
grade = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0]

total = 0  # 학점의 총합
result = 0  # (학점 * 과목평점)

for i in range(20):
    s, c, g = input().split()
    c = float(c)
    if g != 'P':
        total += c
        result += c * grade[rating.index(g)]

print(result / total)
