import sys
from collections import defaultdict as dd
input = sys.stdin.readline
N,M=map(int,input().split())
graph = dd(list)
indegree = dd(int)
for _ in range(M):
    a,b = input().strip().split()
    indegree[b] += 1;indegree[a]
    graph[a].append(b)
madeBy = set([k for k, v in indegree.items() if not v])
def arrest(who):
    for next in graph[who]:
        indegree[next] -= 1
        if indegree[next]: continue
        arrest(next)
for arrested in list(input().strip().split())[1:]:
    if arrested in madeBy:
        madeBy.remove(arrested)
    indegree[arrested] = 0
    arrest(arrested)
visited = set()
def dfs(u):
    visited.add(u)
    for v in graph[u]:
        if v in visited or not indegree[v]: continue
        dfs(v)
for provider in madeBy:
    if not provider in visited: dfs(provider)
print(len(visited)- len(madeBy))