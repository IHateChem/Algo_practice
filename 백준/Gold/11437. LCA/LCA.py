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
M = 22
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
    if level[a]> level[b]:a,b=b,a
    for i in range(20,-1,-1):
        if level[b]-level[a]>=2**i:
            b=lca_table[b][i]
    if a==b:return a
    for i in range(20,-1,-1):
        if lca_table[a][i]!=lca_table[b][i]:
            a,b=lca_table[a][i],lca_table[b][i]
    return lca_table[a][0]
K = int(input())
MKlca()
answer = []
for _ in range(K):
    a, b = map(int, input().split())
    print(getlca(a,b))
#print("\n".join(answer))