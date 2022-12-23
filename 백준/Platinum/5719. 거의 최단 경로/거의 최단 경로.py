import sys
import heapq
from collections import deque
input = sys.stdin.readline
INF = 10e8

def dijk_path(graph, s, d, inf):
    stack = [(0, s)]
    visited = [0] * len(graph)
    distance = [inf] * len(graph)
    path = [[]] * len(graph)
    distance[s] = 0
    while stack:
        w, node = heapq.heappop(stack)
        if visited[node]: continue
        if node == d: return distance[d], path
        visited[node] = 1
        for next, next_w in graph[node]:
            if not visited[next]:
                if w + next_w < distance[next]:
                    heapq.heappush(stack, (w+next_w, next))
                    path[next] = [node]
                    distance[next] = w+next_w
                elif w+ next_w == distance[next]: path[next].append(node)
    return -1, path

while True:
    N, M = map(int, input().split())
    if N == 0 and M ==0: break
    S, D = map(int, input().split())
    graph = [[] for _ in range(N)]
    weight_dict = {}
    for _ in range(M):
        u, v, p = map(int, input().split())
        graph[u].append((v, p))
        weight_dict[(u,v)] = p
    w, path = dijk_path(graph, S, D, INF)
    stack = deque([D])
    t = []
    visited = [0] * len(graph)
    while w > 0 and stack:
        node = stack.popleft()
        if visited[node]: continue
        visited[node] = 1
        for next in path[node]:
            if weight_dict[(next, node)]:
                graph[next].remove((node, weight_dict[(next, node)]))
                weight_dict[(next, node)] = 0
        for i in path[node]:
            if not visited[i]:
                stack.append(i)
    new_w, path = dijk_path(graph, S, D, INF)
    print(new_w)