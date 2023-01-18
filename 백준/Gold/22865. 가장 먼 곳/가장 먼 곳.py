import sys
import heapq
input = sys.stdin.readline
N = int(input())
INF = 1e6
friends = set(map(int, input().split()))
M =  int(input())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    D, E, L = map(int, input().split())
    graph[D].append((E, L))
    graph[E].append((D, L))
tot_dist = [INF] * (N+1)
for friend in friends:
    stack = [(0, friend)]
    dist = [INF] * (N+1)
    dist[friend] = 0
    visited = set()
    while stack:
        d, u = heapq.heappop(stack)
        if u in visited: continue
        visited.add(u)
        for v, w in graph[u]:
            if not v in visited:
                if dist[v] > dist[u] + w:
                    dist[v] =  dist[u] + w
                    heapq.heappush(stack, (dist[v], v))
    for i, w in enumerate(dist):
        tot_dist[i] = min(tot_dist[i], w)
max_v = (0,0)
for i in range(1, N+1):
    if tot_dist[i] > max_v[0]:
        max_v = (tot_dist[i], i)
print(max_v[1])