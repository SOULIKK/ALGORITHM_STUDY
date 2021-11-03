# https://www.acmicpc.net/problem/10250


t = int(input())

for _ in range(t):
    h, w, n = map(int, input().split())
    left, right = 0, 0
    if n % h == 0:
        left = h * 100
        right = n // h
    else:
        left = (n % h) * 100
        right = (n // h) + 1

    print(left + right)
