import sys
import heapq
input = sys.stdin.readline
sx, sy = map(float, input().split())
ex, ey = map(float, input().split())
n = int(input())
canons = [list(map(float, input().split())) for _ in range(n)]
graph = []
#s e canons
def get_dist(x,y, r,s): return ((x-r)**2+(y-s)**2)**0.5
postion = [(sx,sy), (ex, ey)] + canons
for i in range(n+2):
    t = []
    for j in range(n+2):
        t.append(get_dist(*postion[i], *postion[j]))
    graph.append(t)
stack = []
visited = [1]+[0]*(n+1)
for i in range(n+1):
    d = graph[0][i+1]
    heapq.heappush(stack, (d/5, i+1))
while stack:
    t, u = heapq.heappop(stack)
    if u == 1: break
    visited[u] = 1
    for i in range(n+2):
        if visited[i]: continue
        next_d = graph[u][i]
        next_t = min(2+abs(next_d-50)/5, next_d/5)
        heapq.heappush(stack,(t+next_t, i))
print(t)