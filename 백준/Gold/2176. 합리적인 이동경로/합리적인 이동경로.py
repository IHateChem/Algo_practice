import sys
import heapq
input = sys.stdin.readline
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
distance = [[10**8]*(N+1) for _ in range(N+1)]
for i in range(1, N+1):
    distance[i][i] = 0
for _ in range(M):
    U, V, W = map(int, input().split())
    graph[U].append(V)
    graph[V].append(U)
    distance[U][V] = W
    distance[V][U] = W

visited = [0]*(N+1)
stack = [(0, 2)]
while stack:
    w, u = heapq.heappop(stack)
    if visited[u]:
        continue
    visited[u] = 1
    for next in graph[u]:
        if w+distance[u][next] <= distance[2][next]:
            distance[2][next] = w + distance[u][next]
            distance[next][2] = w + distance[u][next]
            heapq.heappush(stack, (w+distance[u][next], next))
dp = [0]*(N+1)
dp[2] = 1
'''
dp[i] = SIGMA dp[n] for n in possible next node
'''
stack = []
for i , w in enumerate(distance[2][1:]):
    if i == 1:
        continue
    heapq.heappush(stack, (w, (i+1)))
while stack:
    w, u = heapq.heappop(stack)
    u_to_2 = distance[u][2]
    for next in graph[u]:
        if distance[next][2] < u_to_2:
            dp[u] += dp[next]
    if u == 1:
        break
print(dp[1])