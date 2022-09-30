import sys
input = sys.stdin.readline
N, M = map(int, input().strip().split())
bluerays = list(map(int, input().strip().split()))
low = max(bluerays)
maxsize = 0
high = sum(bluerays)
while low <= high:
    mid = (high+low) // 2
    cnt = 0
    size = 0
    for song in bluerays:
        if size +song > mid:
            cnt += 1
            size = 0
        size += song
    if size > 0:
        cnt += 1
    if cnt > M:
        low = mid+1
    else:
        high = mid-1
print(low)