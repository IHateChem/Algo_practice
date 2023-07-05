import sys
from heapq import *
from collections import deque as dq
input=sys.stdin.readline
T=int(input())
INF=1000000000
def getPath(path):
    queue=dq()
    parent=M-1
    while parent!=-1:
        queue.appendleft(parent)
        parent=path[parent]
    return " ".join(map(str,queue))
def dijk():
    dist=[INF]*M
    dist[0]=0
    path=[-1]*M
    stack=[s for s in graph[0]]
    heapify(stack)
    visited=set([0])
    while stack:
        z,x,parent=heappop(stack)
        if x in visited: continue
        visited.add(x)
        path[x]=parent
        if x==M-1:
            print(f"Case #{i+1}: "+getPath(path))
            break
        for newZ,y, newP in graph[x]:
            if y in visited or dist[y]<z+newZ:continue
            dist[y]=z+newZ
            heappush(stack, (z+newZ,y,x))
    else:
        print(f"Case #{i+1}: -1")
for i in range(T):
    N,M=map(int,input().split())
    graph=[[]for  _ in range(M)]
    for _ in range(N):
        x,y,z=map(int,input().split())
        graph[x].append((z,y,x))
        graph[y].append((z,x,y))
    dijk()