import sys
input = sys.stdin.readline
N, M = map(int, input().split())
A, B, K, G = map(int, input().split())
kings_paths = list(map(int, input().split()))
INF = 1024
graph = [[INF] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    u, v, l = map(int, input().split())
    graph[u][v] = l
    graph[v][u] = l

blocken = [[-1] * (N + 1) for _ in range(N + 1)]
t = 0
p = 0
visited = set()

for path in kings_paths:
    blocken[p][path] = t
    blocken[path][p] = t
    if p != 0:
        t += graph[p][path]
    p = path
import heapq
heap = [(K, A)]
while heap:
    t, u = heapq.heappop(heap)
    if u == B: break
    if u in visited: continue
    visited.add(u)
    for i in range(N+1):
        if graph[u][i] == INF or i in visited: continue
        if blocken[u][i] <= t < blocken[u][i] + graph[u][i]:
            heapq.heappush(heap, (blocken[u][i] + 2*graph[u][i],i) )
        else:
            heapq.heappush(heap, (t + graph[u][i],i))
print(t-K)