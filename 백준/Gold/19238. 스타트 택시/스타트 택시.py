import sys
input = sys.stdin.readline
N, M, F = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
x, y = map(int, input().split())
x -= 1; y-=1
passengers = [list(map(int, input().split())) for _ in range(M)]
starts = list(map(lambda t: (t[0]-1, t[1]-1), passengers))
destinations = list(map(lambda t: (t[2]-1, t[3]-1), passengers))
visited = [[0]*N for _ in range(N)]
visited[x][y] = 1
find = False
candidates = []
pos = [(x,y)]
next = []
def getdist(x, y, desx, desy):
    visited = [[0]*N for _ in range(N)]
    visited[x][y] = 1
    dist = 0
    pos =[(x,y)]
    t = []
    while pos:
        dist += 1
        for x, y in pos:
            for dx, dy in ((1,0), (-1,0), (0,1), (0,-1)):
                if not (0<=x+dx<N and 0<=y+dy<N): continue
                if MAP[x+dx][y+dy]: continue
                if visited[x+dx][y+dy]: continue
                visited[x+dx][y+dy] = 1
                if (x+dx,y+dy) == (desx,desy): return dist
                t.append((x+dx, y+dy))
        pos = t
        t=  []
    return 10000000
while F:
    for x, y in pos:
        if (x, y) in starts:
            candidates.append((x, y))
            F += 1
            break
        for dx, dy in ((1,0), (-1,0), (0,1), (0,-1)):
            if not (0<=x+dx<N and 0<=y+dy<N): continue
            if MAP[x+dx][y+dy]: continue
            if visited[x+dx][y+dy]: continue
            visited[x+dx][y+dy] = 1
            if (x+dx, y+dy) in starts:
                candidates.append((x+dx, y+dy))
            else:
                next.append((x+dx,y+dy))
    F -= 1
    pos = next
    next = []
    if candidates:
        candidates.sort()
        x, y = candidates[0]
        for i in range(len(starts)):
            if starts[i] == (x,y):
                break
        destx, desty = destinations[i]
        del starts[i]
        del destinations[i]
        dist = getdist(x,y, destx, desty)
        if dist <= F:
            F += dist
            pos =[(destx, desty)]
            next = []
            candidates = []
            visited = [[0]*N for _ in range(N)]
            visited[destx][desty] = 1
        else:
            F = -1
            break
    if not starts: break
else:
    print(-1)
    exit()
print(F)
