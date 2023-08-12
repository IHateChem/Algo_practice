import sys
from collections import defaultdict as dd
input=sys.stdin.readline
dir = [(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1)]
M, S=map(int,input().split())
MAP = dd(int)
NEWMAP=dd(int)
SMELLS = dd(int)
for _ in range(M):
    x, y, d = map(int, input().split())
    MAP[(x,y,d-1)] += 1
x,y=map(int,input().split())
def move():
    for k, v in MAP.items():
        if not v: continue
        tx, ty, d = k
        for i in range(8):
            nd = (d-i)%8 
            dx, dy = dir[nd]
            if 0<tx+dx<=4 and 0<ty+dy<=4 and not SMELLS[(tx+dx,ty+dy)] and (tx+dx !=x or ty+dy!=y):
                NEWMAP[(tx+dx,ty+dy,nd)] +=v
                break
        else:
            NEWMAP[(tx,ty,d)] +=v
def shark():
    paths=[]
    for i in (2,0,6,4):
        for j in (2,0,6,4):
            for k in (2,0,6,4):
                paths.append((i,j,k))
    caught  = []
    howmany = -1
    nx,ny=x,y

    for path in paths:
        t = 0
        visited = set()
        catch = []
        tx,ty = x,y
        for d in path:
            dx, dy = dir[d]
            tx += dx; ty+=dy
            if (tx, ty) in visited: continue
            visited.add((tx, ty))
            if 0<tx<=4 and 0<ty<=4:
                for i in range(8):
                    if NEWMAP[(tx,ty, i)]:
                        t += NEWMAP[(tx,ty, i)]
                        catch.append((tx,ty,i))

            else: break
        else:
            if howmany < t:
                nx, ny = tx,ty
                caught = catch
                howmany = t
        continue
    for fish in caught:
        NEWMAP[fish] = 0
        tx,ty,_=fish
        SMELLS[(tx,ty)] = 3
    return nx, ny
for _ in range(S):
    move()
    x, y  = shark()
    for k, v in MAP.items():
        if v: NEWMAP[k] +=v
    MAP= dd(int)
    for k, v in NEWMAP.items():
        if v: MAP[k] +=v
    NEWMAP = dd(int)
    for pos in SMELLS.keys():
        if SMELLS[pos]: SMELLS[pos]-=1
print(sum([v for v in MAP.values()]))