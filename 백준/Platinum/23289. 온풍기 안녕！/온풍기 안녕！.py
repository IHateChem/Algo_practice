import sys
import heapq
input = sys.stdin.readline
R,C,K = map(int,input().split())
MAP = [list(map(int,input().split())) for _ in range(R)]
heaters = [(i,j, MAP[i][j]) for i in range(R) for j in range(C) if MAP[i][j] in (1,2,3,4)]
targets = [(i,j) for i in range(R) for j in range(C) if MAP[i][j] == 5]
W = int(input())
walls = [tuple(map(int,input().split())) for _ in range(W)]
walls = [(w[0]-1, w[1]-1, w[2]) for w in walls]
directions = {1:(0,1), 2:(0,-1), 3:(-1,0), 4:(1,0)}
nextdPos = {1:[(0,1), (1,1), (-1,1)], 2:[(0,-1), (1,-1), (-1,-1)], 3:[(-1,0), (-1,1), (-1,-1)], 4:[(1,0), (1,-1), (1,1)]}
inbound = lambda x, y: 0<=x<R and 0<=y<C
def canGo(x,y, dx, dy, d):
    go = True
    if d == 1: # 오
        if (dx, dy) == (-1, 1) and ((x, y, 0) in walls or (x-1, y, 1) in walls): go = False
        elif (dx, dy) == (0, 1) and (x, y, 1) in walls: go = False
        elif (dx, dy) == (1, 1) and ((x+1, y, 0) in walls or (x+1, y, 1) in walls): go = False
    elif d == 2: # 왼
        if (dx, dy) == (-1, -1) and ((x, y, 0) in walls or (x-1, y-1, 1) in walls): go = False
        elif (dx, dy) == (0, -1) and (x, y-1, 1) in walls: go = False
        elif (dx, dy) == (1, -1) and ((x+1, y, 0) in walls or (x+1, y-1, 1) in walls): go = False
    elif d == 3: # 위
        if (dx, dy) == (-1, -1) and ((x, y-1, 0) in walls or (x, y-1, 1) in walls): go = False
        elif (dx, dy) == (-1, 0) and (x, y, 0) in walls: go = False
        elif (dx, dy) == (-1, 1) and ((x, y+1, 0) in walls or (x, y, 1) in walls): go = False
    elif d == 4: # 아래
        if (dx, dy) == (1, -1) and ((x+1, y-1, 0) in walls or (x, y-1, 1) in walls): go = False
        elif (dx, dy) == (1, 0) and (x+1, y, 0) in walls: go = False
        elif (dx, dy) == (1, 1) and((x+1, y+1, 0) in walls or (x, y, 1) in walls): go = False
    else:
        if dx and (x+dx, y,0) in walls: go = False
        if dy and  (x,y,1) in walls: go = False
    return go
def blowArea(x,y,d):
    ret = {5-i: set() for i in range(5)}
    t = set()
    dx, dy = directions[d]
    ret[5] = set([(x+dx, y+dy)])
    q = [(x+dx,y+dy,d, 5)]
    while q:
        x,y,d, k = q.pop()
        if k == 1: continue
        for dx, dy in nextdPos[d]:
            nx, ny = x+dx, y+dy
            if not inbound(nx, ny): continue
            if not canGo(x,y,dx,dy,d): continue
            t.add((nx,ny, d, k-1))
        if not q:
            ret[k-1] = set([(tset[0], tset[1]) for tset in t])
            q = list(t)
            t = set()
    return ret
for x, y,d8 in heaters:
    MAP[x][y] = 0
for x,y in targets:
    MAP[x][y] = 0
heatersPos = [blowArea(*heater) for heater in heaters]
def blow():
    for posSet in heatersPos:
        for k in range(5):
            for i, j in posSet[k+1]:
                MAP[i][j] += k+1

def mediate():
    dMAP = [[0]*C for i in range(R)]
    for i in range(R):
        for j in range(C):
            for di, dj in ((1,0), (0,1)):
                ni, nj = i+di, j+dj
                if not inbound(ni, nj): continue
                if not canGo(i,j,di,dj,0): continue
                temp = MAP[i][j]
                ntemp = MAP[ni][nj]
                dTemp = abs(temp-ntemp)//4
                if temp < ntemp:
                    dMAP[ni][nj] -= dTemp
                    dMAP[i][j] += dTemp
                else:
                    dMAP[ni][nj] += dTemp
                    dMAP[i][j] -= dTemp
    for i in range(R):
        for j in range(C):
            MAP[i][j] += dMAP[i][j]

def outSideDown():
    for i in range(R):
        if MAP[i][0]: MAP[i][0] -= 1
        if MAP[i][C-1]: MAP[i][C-1] -= 1
    for i in range(1,C-1):
        if MAP[0][i]: MAP[0][i] -= 1
        if MAP[R-1][i]: MAP[R-1][i] -= 1
ans = 0
#print(heatersPos)
for i in range(101):
    blow()
    mediate()
    outSideDown()
    ans += 1
    if sum([MAP[i][j] >= K for i, j in targets]) == len(targets): break
print(ans)