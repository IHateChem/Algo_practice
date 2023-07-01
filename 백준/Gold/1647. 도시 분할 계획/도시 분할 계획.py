import sys
import heapq
#prim 
input = sys.stdin.readline
N,M = map(int, input().split())
graph = [[]for i in range(N+1)]
for _ in range(M):
    a,b,c = map(int, input().split())
    graph[a].append((c,b))
    graph[b].append((c,a))
visited = set()
visited.add(1)
stack = [];path= []
for t in graph[1]: heapq.heappush(stack, t)
while stack:
    c, b = heapq.heappop(stack)
    if b in visited: continue
    visited.add(b)
    path.append(c)
    for c, a in graph[b]:
        if a in visited: continue
        heapq.heappush(stack, (c,a))
print(sum(path)-max(path))