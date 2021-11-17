# https://www.acmicpc.net/problem/1927
# 최소 힙

import heapq

n = int(input())
array = []
result = []

for _ in range(n):
    data = int(input())
    if data == 0:
        if array:
            result.append(heapq.heappop(array))
        else:
            result.append(0)
    else:
        heapq.heappush(array, data)

for data in result:
    print(data)