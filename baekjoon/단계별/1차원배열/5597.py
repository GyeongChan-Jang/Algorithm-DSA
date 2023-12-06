import sys
sys.stdin = open(
    "/Users/jang-gyeongchan/Desktop/Develop/algorithm/baekjoon/input.txt", "r")

students = [v for v in range(1, 31)]

for _ in range(28):
    students.remove(int(input()))

print(students[0])
print(students[1])

# 줄바꿈하여 출력
print(*students, sep='\n')
