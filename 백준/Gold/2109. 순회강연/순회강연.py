import heapq
import sys
input=sys.stdin.readline
N=int(input())
dead = [[] for _ in range(10001)]
for _ in range(N):
    c, d = map(int,input().split())
    heapq.heappush(dead[d-1], -1*c)
total = []
for i in range(10001):
    while dead[i] and len(total)<=i:
        heapq.heappush(total, -1 * heapq.heappop(dead[i]))
    while dead[i] and total[0] < -1*dead[i][0]:
        heapq.heappop(total)
        heapq.heappush(total, -1*heapq.heappop(dead[i]))
print(sum(total))