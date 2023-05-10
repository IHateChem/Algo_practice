import sys
#Do Dfs
input=sys.stdin.readline
sys.setrecursionlimit(2000000)
N, S, P = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [0]*(N+1)
def Dfs(u: int) -> tuple: #(length to penguin, number of not to penguin)
    if u == P: return 1,0
    len2pen, len02pen  = 0, 0
    for v in graph[u]:
        if visited[v]: continue
        visited[v] = 1
        dlen2pen, dlen02pen = Dfs(v)
        len2pen += dlen2pen
        len02pen += dlen02pen
    if len2pen: return len2pen + 1, len02pen
    else: return 0, len02pen + 1
for i in range(N-1): 
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
bridges = []
for i in range(1, S+1):
    visited[i] = 1
    bridges.append(Dfs(i))
    visited[P] = 0
bridges.sort()
answer = N - bridges[0][0] - bridges[1][0] + 1
print(answer)