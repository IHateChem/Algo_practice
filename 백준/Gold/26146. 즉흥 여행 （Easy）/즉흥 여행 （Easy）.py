import sys
input = sys.stdin.readline
sys.setrecursionlimit(200000)
N, M= map(int, input().split())
get_id = [0]*(N+1)
id = 1
graph = [[] for _ in range(N+1)]
graph_r = [[] for _ in range(N+1)]
for _ in range(M):
    v, w = map(int, input().split())
    graph[v].append(w)
    graph_r[w].append(v)

def scc(n):
    stack = []
    visited = [0] *(n+1)
    for i in range(1, n+1):
        if not visited[i]:
            visited[i] = 1
            DFS(i, visited)
    ret = []
    visited = [0] *(n+1)
    t = set(); stack = []
    for u in get_id[1:][::-1]:
        t = set()
        if not visited[u]:
            stack = [u]
            visited[u] = 1
        while stack:
            s = stack.pop()
            t.add(s)
            for next in graph_r[s]:
                if not visited[next]:
                    visited[next] = 1
                    stack.append(next)
        if t: ret.append(t)
    return ret

def DFS(c, visited):
    global id
    for next in graph[c]:
        if not visited[next]:
            visited[next] = 1
            DFS(next, visited)
    get_id[id] = c
    id += 1
ans = scc(N)
if len(ans) == 1:
    print("Yes")
else:
    print("No")