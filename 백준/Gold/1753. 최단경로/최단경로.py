import sys
input = sys.stdin.readline
import heapq
def dijk(graph, s, d, inf):
    stack = [(0, s)]
    visited = [0] * len(graph)
    distance = [inf] * len(graph)
    distance[s] = 0
    while stack:
        w, node = heapq.heappop(stack)
        if visited[node]: continue
        if node == d: return w
        visited[node] = 1
        for next, next_w in graph[node]:
            if not visited[next]:
                if w + next_w < distance[next]:
                    heapq.heappush(stack, (w+next_w, next))
                    distance[next] = w+next_w
    for i in distance[1:]:
        if i == inf: print("INF")
        else: print(i)
    return -1

V, E = map(int, input().split())
graph = [[] for _ in range(V+1)]
S = int(input())
for _ in range(E):
    u, v, w = map(int , input().split())
    graph[u].append((v, w))
n = dijk(graph, S, 0, 10e7)