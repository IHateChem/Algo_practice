import sys
import heapq
input=sys.stdin.readline
N, M, X = map(int, input().split())
go_graph = [[] for _ in range(N+1)]
back_graph = [[] for _ in range(N+1)]
for _ in range(M):
    s, e, t = map(int, input().split())
    go_graph[s].append((e, t))
    back_graph[e].append((s, t))
INF = 1e6
go_dist = [INF for _ in range(N+1)]
back_dist = [INF for _ in range(N+1)]
def dijk(graph, dist):
    stack = [(0, X)]
    while stack:
        tot_w, u = heapq.heappop(stack)
        if dist[u] <= tot_w: continue
        dist[u] = tot_w
        for v, w in graph[u]:
            if dist[v] > tot_w+w:
                heapq.heappush(stack, (tot_w+w, v))
dijk(go_graph, go_dist)
dijk(back_graph, back_dist)
dist = [i+j for i, j in zip(go_dist, back_dist)]
print(max(dist[1:]))