import sys
input = sys.stdin.readline
R,C = map(int,input().split())
MAP = [list(input().strip()) for _ in range(R)]
start = []
swan = []
parent = [[-1]*C for _ in range(R)]
visited= set()
for i in range(R):
    for j in range(C):
        if MAP[i][j] in (".", "L"): start.append((i,j)); visited.add((i,j))
        if MAP[i][j] == "L": swan.append((i,j))
idx = 1
a, b = swan[0]; c,d = swan[1]
checkrange=  lambda x,y: 0<=x<R and 0<=y<C
for x, y in start:
    if parent[x][y] != -1: continue
    stack = [(x,y)]
    while stack:
        x, y = stack.pop()
        parent[x][y] = idx
        for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
            if not checkrange(x+dx, y+dy): continue
            if parent[x+dx][y+dy] != -1: continue
            if MAP[x+dx][y+dy] == "X": continue
            stack.append((x+dx,y+dy))
    idx += 1
ancestor = {}
for i in range(idx):
    ancestor[i] = i

day = 0; t= []
def getanc(i):
    if ancestor[i] == i: return i
    a = getanc(ancestor[i])
    ancestor[i] = a
    return a
while start:
    x,y = start.pop()
    if MAP[x][y] == "X":
        MAP[x][y] = "."
        types = set()
        anc_types = set()
        for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
            if not checkrange(x+dx, y+dy): continue
            if MAP[x+dx][y+dy] != "X":
                types.add(parent[x+dx][y+dy])
                anc_types.add(getanc(parent[x+dx][y+dy]))
        m = min(anc_types)
        parent[x][y] = m
        for type in types:
            ac = getanc(type)
            ancestor[ac] = m
    for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
        if not checkrange(x+dx, y+dy): continue
        if (x+dx, y+dy) in visited: continue
        t.append((x+dx,y+dy))
        visited.add((x+dx, y+dy))
    if not start:
        if getanc(parent[a][b]) == getanc(parent[c][d]):
            print(day)
            exit(0)
        day += 1
        start = t
        t = []