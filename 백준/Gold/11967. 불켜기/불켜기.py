import sys
from collections import defaultdict as dd
input = sys.stdin.readline
N,M = map(int, input().split())
MAP = [[[] for i in range(N+1)] for _ in range(N+1)]
for _ in range(M):
    x,y,a,b = map(int,input().split())
    MAP[x][y].append((a,b))
lightOn = set([(1,1)])
canVisit = set([(1,1), (0,1), (1,0),(1,2), (2,1)])
visited = set([(1,1)])
q = [(1,1)]
while q:
    a,b = q.pop()
    for da, db in ((1,0), (0,1), (-1,0), (0,-1)):
        if (a+da,b+db) in visited or not (a+da,b+db) in lightOn: continue
        visited.add((a+da,b+db))
        for dx, dy in ((0,0), (1,0), (0,1), (-1,0), (0,-1)):
            canVisit.add((a+da+dx, b+db+dy))
        q.append((a+da,b+db))
    for x, y in MAP[a][b]:
        if (x,y) in lightOn or (x,y) in visited: continue
        lightOn.add((x,y))
        if(x,y) in canVisit and not (x,y) in visited:
            q.append((x,y))
            visited.add((x,y))
            for dx, dy in ((0,0), (1,0), (0,1), (-1,0), (0,-1)):
                canVisit.add((x+dx, y+dy))
print(len(lightOn))