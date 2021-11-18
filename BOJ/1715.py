# https://www.acmicpc.net/problem/1715
# 카드 정렬하기 [힙, 그리디]import heapq

n = int(input())
array = []

for i in range(n):
    data = int(input())
    heapq.heappush(array, data)

result = 0

while len(array) != 1:
    value1 = heapq.heappop(array)
    value2 = heapq.heappop(array)
    sum_value = value1 + value2
    result += sum_value
    heapq.heappush(array, sum_value)

print(result)