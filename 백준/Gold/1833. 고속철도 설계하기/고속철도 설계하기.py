import sys
import heapq
input = sys.stdin.readline
N = int(input())
graph = [list(map(int,input().split())) for _ in range(N)]
visited = set()
m = 100000000000
for j in range(1, N):
    if graph[0][j] < m: 
        m = graph[0][j]
        x, y = 0, j
heap = [(graph[x][y],x,y)]
used = set()
used.add((x,y))
used.add((y,x))
C = 0
M = []
edge = 0
def addHeap(u):
    if not u in visited:
        for j in range(N):
            if u == j or (u,j) in used: continue
            if graph[u][j] > 0 and j in visited: continue
            heapq.heappush(heap, (graph[u][j], u, j))
            used.add((u,j))
            used.add((j,u))
while heap and (edge < N-1 or (heap[0][0] < 0)):
    cost, u, v = heapq.heappop(heap)
    if cost >= 0:
        if u in visited and v in visited: continue
        C += cost
        M.append((u,v))
        edge += 1
    else:
        C -= cost
        if u in visited and v in visited: continue
        edge += 1
    addHeap(u)
    addHeap(v)
    visited.add(u);visited.add(v)
print(C, len(M))
for u, v in M:
    print(u+1,v+1)