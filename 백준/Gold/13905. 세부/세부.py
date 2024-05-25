import sys
import heapq
input = sys.stdin.readline
N,M = map(int,input().split())
s,e = map(int,input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    h1, h2, k = map(int,input().split())
    graph[h1].append((-k, h2))
    graph[h2].append((-k, h1))
Mheap = [(-1000000000000, s)]
visited = set()
while Mheap:
    k, v = heapq.heappop(Mheap)
    if v in visited: continue
    if v == e:
        print(-k)
        break
    visited.add(v)
    for nk, n in graph[v]:
        if n in visited: continue
        heapq.heappush(Mheap, (max(k, nk), n))
else:
    print(0)