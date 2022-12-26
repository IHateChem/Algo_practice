import sys
input = sys.stdin.readline
N = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(N):
    t = list(map(int, input().split()))
    u = t[0]
    vs = t[1:-1]
    for i in range(len(vs)//2):
        graph[u].append((vs[i*2], vs[i*2+1]))
visited = [0] * (N+1)
stack = [(1, 0)]
max_length = 0; node = 1
while stack:
    u, length = stack.pop()
    if length > max_length:
        node = u
        max_length = length
    visited[u] = 1
    for v, weight in graph[u]:
        if not visited[v]:
            stack.append((v, length+weight))
stack = [(node, 0)]
max_length = 0
visited = [0] * (N+1)
while stack:
    u, length = stack.pop()
    max_length = max(length, max_length)
    visited[u] = 1
    for v, weight in graph[u]:
        if not visited[v]:
            stack.append((v, length+weight)) 
print(max_length)