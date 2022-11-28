import sys
import heapq
input = sys.stdin.readline
N, K= map(int, input().split())
scores = list(map(int, input().split()))
l = 0 ; r = sum(scores)

while l <= r:
    m = (l+r)//2
    t = 0 
    n = 0
    for score in scores:
        t += score
        if t >= m:
            t = 0; n += 1
    if n < K:
        r = m - 1
    else:
        l = m + 1
print(r)