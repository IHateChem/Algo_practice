#위상정렬가능한지 확인
from collections import deque
import sys
sys.setrecursionlimit(3000000)
def solution(n, path, order): #[[8, 5], [6, 7], [4, 1], [0,4]]
    graph = [set() for  _ in range(n)]
    graph2 = [set() for  _ in range(n)]
    inDegree = [0]*n
    for u, v in path:
        graph[u].add(v)
        graph[v].add(u)
    visited = set()
    q = deque([0])
    while q:
        u = q.popleft()
        for v in graph[u]:
            graph[v].remove(u)
            q.append(v)
            graph2[u].add(v)
            inDegree[v]+=1
    for u, v in order:
        if not v in graph2[u]:
            graph2[u].add(v)
            inDegree[v] += 1
    if not inDegree[0]: q = deque([0])
    else: q = []
    while q:
        u = q.popleft()
        for v in graph2[u]:
            inDegree[v] -= 1
            if inDegree[v]: continue
            q.append(v)
    return not sum(inDegree)