# https://www.acmicpc.net/problem/2012
# 등수 매기기

n = int(input())
array = []

for _ in range(n):
    array.append(int(input()))

array.sort()

result = 0
for i in range(1, len(array) + 1):
    result += abs(i - array[i - 1])

print(result)
