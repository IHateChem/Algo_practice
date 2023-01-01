import sys
import math
input = sys.stdin.readline
sys.setrecursionlimit(100000)
N = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
M = 21
lca_table = [ [0 for __ in range(M)] for _ in range(N+1)]
level = [0] * (N+1)
visited = [0] * (N+1)
def dfs(node, p_node, lv):
    lca_table[node][0] = p_node
    visited[node] = 1
    level[node] = lv
    for i in graph[node]:
        if visited[i]: continue
        dfs(i, node, lv + 1)


def MKlca():
    dfs(1,0, 1)
    for i in range(1, M):
        for j in range(1, N+1):
            lca_table[j][i] = lca_table[lca_table[j][i-1]][i-1]
def getlca(a, b):
    if a == 1 and b == 1: return 1
    target = a if level[a] > level[b] else b
    compare = a if target == b else b
    if level[target] != level[compare]:
        for i in range(M-1, -1, -1):
            if level[target] - level[compare] >= 2**i:
                target = lca_table[target][i]
    if target != compare:
        for i in range(M-1, -1, -1):
            if lca_table[target][i] != lca_table[compare][i]:
                target = lca_table[target][i]
                compare = lca_table[compare][i]
    else: return target
    return lca_table[compare][0]
K = int(input())
MKlca()
answer = []
for _ in range(K):
    a, b = map(int, input().split())
    print(getlca(a,b))
#print("\n".join(answer))