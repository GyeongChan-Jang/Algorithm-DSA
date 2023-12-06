import sys
sys.stdin = open(
    "/Users/jang-gyeongchan/Desktop/Develop/algorithm/baekjoon/input.txt", "r")

max = 0
index = 0


for v in range(9):
    num = int(input())
    if num > max:
        max = num
        index = v+1

print(max)
print(index)

# max 메서드 사용

numbers = []
for _ in range(9):
    v = int(input())
    numbers.append(v)

print(max(numbers))
print(numbers.index(max(numbers))+1)

# list comprehension

numbers = [int(input()) for _ in range(9)]
print(max(numbers))
print(numbers.index(max(numbers))+1)
