# https://www.acmicpc.net/problem/2110
# 공유기 설치 [이진탐색]
n, c = map(int, input().split())
home = [int(input()) for _ in range(n)]
home = sorted(home)

left = 1
right = home[-1] - home[0]
result = 0

while right >= left:
    mid = (right + left) // 2
    wifi_count = 1
    tmp = home[0]
    for i in range(1, n):
        if home[i] >= tmp + mid:
            wifi_count += 1
            tmp = home[i]

    if wifi_count < c:
        right = mid - 1
    else:
        left = mid + 1
        result = mid

print(result)
