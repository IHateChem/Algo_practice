import sys
from collections import deque
import heapq
input = sys.stdin.readline
INF = sys.maxsize
N, M = map(int, input().split())
graph = [[]  for _ in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append((b, i))
    graph[b].append((a, i))

q = [(1, 0)]
visited = [INF] *(N+1); visited[1] = 0
while q:
    u , t = heapq.heappop(q)
    if  u == N: break
    if visited[u] < t: continue
    for v, w in graph[u]:
        next_time = t + (w - t) % M+ 1
        if visited[v] > next_time:
            visited[v] = next_time
            heapq.heappush(q, (v, next_time))
print(t)