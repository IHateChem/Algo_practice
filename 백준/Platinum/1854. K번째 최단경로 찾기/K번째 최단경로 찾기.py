import sys
import heapq
from collections import deque
input=sys.stdin.readline
n,m,k=map(int,input().split())
graph = [[] for _ in range(n+1)]
INF=10000000000000
distance = [[INF]*k for _ in range(n+1)]
pnts = [0]*(n+1)
for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))
stack = [(0,1)]
while stack:
    l,u = heapq.heappop(stack)
    if pnts[u] <k:
        distance[u][pnts[u]] = l
        pnts[u] += 1
    else: continue
    for v, w in graph[u]:
        if pnts[v] < k:
            heapq.heappush(stack, (l+w,v))
for i in range(n):
    k = distance[i+1][-1] if distance[i+1][-1] != INF else -1
    print(k)