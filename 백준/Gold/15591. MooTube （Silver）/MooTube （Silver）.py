import sys 
input = sys.stdin.readline
N, Q = map(int, input().split())
graph = [[] for _ in  range(N+1)]
for _ in range(N-1):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
usado = [[1e10 for _ in range(N+1)] for __ in range(N+1)]
def dfs(n):
    visited = [0]*(N+1)
    stack = [(n,1e10)]
    _min = 1e10
    while stack:
        v, m = stack.pop()
        if visited[v]: continue
        usado[n][v] = min(usado[n][v], m) 
        visited[v] = 1
        for u, w in graph[v]:
            if not visited[u]:
                if w > m: stack.append((u, m))
                else: stack.append((u,w))
for i in range(1,N+1):
    dfs(i)
for i in range(Q):
    k, v = map(int, input().split())
    answer = 0
    for n, _k in enumerate(usado[v][1:]):
        if n+1 != v and _k >= k: answer += 1
    print(answer)