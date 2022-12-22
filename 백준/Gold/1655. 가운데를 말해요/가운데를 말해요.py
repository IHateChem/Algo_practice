import sys
input = sys.stdin.readline
import heapq
from collections import deque as dq
from math import ceil
from bisect import bisect_left as bl
n = int(input())
left = []
right = []
A = dq()
mid = int(input())
answer = [str(mid)]
for i in range(n-1):
    n = int(input())
    if n < mid:
        heapq.heappush(left, -1 * n)
    else:
        heapq.heappush(right, n)
    if len(left) == len(right) or len(left)+1 == len(right):
        pass
    elif len(left) > len(right):
        heapq.heappush(right, mid)
        mid = -1 * heapq.heappop(left)
    else:
        heapq.heappush(left,-1*mid)
        mid = heapq.heappop(right)
    answer.append(str(mid))
print("\n".join(answer))