import sys
sys.stdin = open(
    "/Users/jang-gyeongchan/Desktop/Develop/algorithm/baekjoon/input.txt", "r")

n = int(input())

nums_pileup = 1  # 벌집의 개수
cnt = 1

while n > nums_pileup:
    nums_pileup += 6 * cnt
    cnt += 1  # 반복문 횟수

print(cnt)
