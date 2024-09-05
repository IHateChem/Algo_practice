import sys
import heapq
input = sys.stdin.readline
N,K = map(int,input().split())
r = 2000000000
l = 1
places = [[0,0]] + [list(map(int,input().split())) for _ in range(N)] + [[10000,10000]]
N += 2
distances = [[0]*N for _ in range(N)]
def getDistance(x,y):
    return (((places[x][0]-places[y][0])**2+(places[x][1]-places[y][1])**2)**0.5) /10
for i in range(N):
    for j in range(N):
        distances[i][j] = getDistance(i,j)
answer = 0.0
K += 1
while l <= r:
    m = float((l+r)//2)
    visited = set()
    q = [(0, 0)]
    while q:
        cnt, node = heapq.heappop(q)
        if node == N-1:
            visited.add(node)
            break
        if node in visited:
            continue
        visited.add(node)
        for i in range(1,N):
            if i in visited:
                continue
            if distances[node][i] <= m:
                heapq.heappush(q,(cnt +1,i))
    else:
        l = m + 1
        continue
    if cnt > K:
        l = m + 1
    else:
        r = m -1
        answer = m
print(int(answer))