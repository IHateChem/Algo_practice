import sys
import heapq
from collections import deque
input = sys.stdin.readline
INF = 10e8
T = int(input())
def dijk(graph, s, d):
    stack = [(0, s)]
    visited = [0] * len(graph)
    ret = 0
    while stack:
        w, node = heapq.heappop(stack)
        if node == d: 
            ret = w
            continue
        visited[node] = 1
        for next, next_w in graph[node]:
            if not visited[next]:
                heapq.heappush(stack, (w+next_w, next))
    return ret
answer = []
def toposort_bfs(graph, s, in_degree): #s: start set
    s = deque(s)
    T = []
    while s:
        u = s.pop()
        T.append(u)
        for next, w in graph[u]:
            in_degree[next] -=1
            if in_degree[next] == 0: s.appendleft(next)
    return T
for _ in  range(T):
    N, K = map(int, input().split())
    D = list(map(int, input().split()))
    start_set = set(range(1, N+1))
    graph = [[] for __ in range(N+1)]
    in_degree = [0]*(N+1)
    for i in range(K):
        u, v = map(int, input().split())
        in_degree[v] += 1
        if v in start_set: start_set.remove(v)
        graph[u].append((v, D[u-1]))
    w = int(input())
    T = toposort_bfs(graph, start_set, in_degree)
    distance = [0]*(N+1)
    for i in start_set:
        distance[i] = D[i-1]
    for i in T:
        for j, k in graph[i]:
            distance[j] = max(distance[j], distance[i]+D[j-1])        
    answer.append(str(distance[w]))
print("\n".join(answer))
