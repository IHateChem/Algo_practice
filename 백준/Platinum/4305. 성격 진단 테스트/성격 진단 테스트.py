import sys
from collections import defaultdict as dd
input = sys.stdin.readline
def tarjan(n):
    global idx
    nodeId[n] = idx
    idx += 1
    parent = nodeId[n]
    stack.append(n)
    for v in graph[n]:
        if nodeId[v] == 0:
            parent = min(parent, tarjan(v))
        elif not finish[v]: parent = min(parent, nodeId[v])
    if parent == nodeId[n]:
        scc = []
        while 1:
            c = stack.pop()
            scc.append(c)
            finish[c] = True
            if n == c: break
        result.append(sorted(scc))
    return parent

first = True
while 1:
    N = int(input())
    if N == 0: break
    if not first: print()
    idx  = 1
    graph = dd(set)
    nodeId = dd(int)
    finish = dd(lambda: False)
    stack = []
    result = []
    for _ in range(N):
        test = list(input().strip().split())
        v = test[-1]
        for u in test:
            if u == v:
                graph[v]
                continue
            graph[u].add(v)
    for u in graph.keys():
        if nodeId[u]: continue
        tarjan(u)
    result.sort()
    for r in result:
        print(*r)
    first = False