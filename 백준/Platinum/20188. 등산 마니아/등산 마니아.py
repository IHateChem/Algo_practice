import sys
from itertools import combinations as C

input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)] 
child =  [0 for _ in range(N+1)] 
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [0] *(N+1); visited[1] = 1
def dfs(node):
    n = 1
    for next in graph[node]:
        if not visited[next]:
            visited[next] = 1
            n += dfs(next)
    child[node] = n
    return n
answer = 0
dfs(1)
for n in child:
    if n >=2 :
        answer += n*(n-1)//2
    answer += n * (N-n)
print(answer-child[1]*(child[1]-1)//2)