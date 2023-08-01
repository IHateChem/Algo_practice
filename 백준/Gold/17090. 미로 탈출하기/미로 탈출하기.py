import sys
from collections import deque
input=sys.stdin.readline
N,M = map(int, input().split())
dest = [[0]*M for _ in range(N)]
MAP=[list(input().strip()) for _ in range(N)]
next={"D":(1,0),"U":(-1,0),"L":(0,-1), "R":(0,1)}
notvisited = set([(i,j) for i in range(N) for j in range(M)])
visited = set()
t = []
def is_in(x,y, dir):
    return 0<=x+next[dir][0]<N and 0<=y+next[dir][1]<M
def coloring(v):
    for x, y in v:
        dest[x][y] = 1
q =[(0,0)]
while notvisited:
    if q:
        x, y = q.pop()
        notvisited.remove((x,y))
    else:
        x, y = notvisited.pop()
    visited.add((x,y))
    t.append((x,y))
    if is_in(x,y, MAP[x][y]):
        dx, dy = next[MAP[x][y]]
        if (x+dx, y+dy) in visited:
            if dest[x+dx][y+dy]:
                coloring(t)
            t = []
        else:
            q.append((x+dx, y+dy))
    else:
        coloring(t)
        t = []
s = 0
for i in dest:
    s += sum(i)
print(s)