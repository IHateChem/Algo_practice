import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
N, M= map(int, input().split())
get_id = []
graph = [[] for _ in range(N+1)]
graph_r = [[] for _ in range(N+1)]
for _ in range(M):
    v, w = map(int, input().split())
    graph[v].append(w)
    graph_r[w].append(v)

def scc(n):
    visited = [0] *(n+1)
    for i in range(1, n+1):
        t = []
        if not visited[i]:
            visited[i] = 1
            DFS(i, visited, graph, t)
    ret = []
    visited = [0] *(n+1)
    for u in get_id[::-1]:
        t = []
        if not visited[u]:
            visited[u] = 1
            DFS(u, visited, graph_r, t)
        if t: ret.append(sorted(t))
    return ret

def DFS(c, visited, graph, t):
    t.append(c)
    for next in graph[c]:
        if not visited[next]:
            visited[next] = 1
            DFS(next, visited, graph, t)
    get_id.append(c)
ans = scc(N)
ans.sort(key = lambda t: t[0])
print(len(ans))
for t in ans:
    print(" ".join(map(str, t))+" -1")