import sys
input=sys.stdin.readline
N,M=map(int,input().split())
graph=[[]for _ in range(N+1)]
for _ in range(M):
    A,B,C=map(int,input().split())
    graph[A].append((B,C))
    graph[B].append((A,C))
s,e=map(int,input().split())
r=max([i[1] for i in graph[s]])
l=1
def bfs(c):
    visited=set([s])
    q=[s];t=[]
    while q:
        u=q.pop()
        if u==e: return True
        for v, w in graph[u]:
            if w<c: continue
            if v in visited: continue
            visited.add(v)
            t.append(v)
        if not q:
            q = t
            t = []
    return False
while l+1<r:
    c=(l+r)//2
    if bfs(c):
        l = c
    else:
        r = c - 1
if bfs(r): print(r)
else: print(l)