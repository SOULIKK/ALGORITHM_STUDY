# https://www.acmicpc.net/problem/1092
# 배 [그리디]

import sys

n = int(input())
c = list(map(int, input().split()))

m = int(input())
b = list(map(int, input().split()))

if max(c) < max(b):
    print(-1)
    sys.exit()

num = [0] * n
checked = [False] * m

c.sort(reverse=True)
b.sort(reverse=True)

result = 0
count = 0

while True:
    if count == len(b):
        break

    for i in range(n):
        while num[i] < len(b):
            if not checked[num[i]] and c[i] >= b[num[i]]:
                checked[num[i]] = True
                num[i] += 1
                count += 1
                break
            num[i] += 1
    result += 1
print(result)
