'''
an = (n-1)(an-1 + an-2)

'''
import sys
input = sys.stdin.readline
N = int(input())
graph = [[] for _ in range(N+1)]
E = int(input())
for _ in range(E):
    u, v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [0]*(N+1)
stack = [1]
visited[1] = 1
while stack:
    t = stack.pop()
    for next in graph[t]:
        if not visited[next]:
            visited[next] = 1
            stack.append(next)
answer = -1
for i in visited:
    if i: answer += 1
print(answer)