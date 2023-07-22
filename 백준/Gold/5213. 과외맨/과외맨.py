import sys
input=sys.stdin.readline
N=int(input())
last = (N*N-N//2)
tiles=[]
before=[]
where = {}
isodd = 0
floor=1
cnt=0
for _ in range(last):
    tiles.append(tuple(map(int, input().split())))
    before.append(_)
    cnt += 1
    where[_] = floor
    if isodd:
        if cnt == N-1:
            isodd = 0
            cnt = 0
            floor += 1
    else:
        if cnt == N:
            isodd = 1
            cnt = 0
            floor += 1
q = [0]
t=[]
UP=-1;DOWN=1
visited = set([0])
def checkupdown(tile, dir, i):
    if dir == UP:
        if i: dt = -(N-1)
        else: dt = -N
    else:
        if i: dt = N
        else: dt = N-1
    if tile + dt>= 0 and tile+dt<last and (not tile+ dt in visited) and tiles[tile][i] == tiles[tile+dt][(i+1)%2] and abs( where[tile] - where[tile+dt] )== 1:
        t.append(tile+dt)
        visited.add(tile+dt)
        before[tile+dt] = tile
def checkleftright(tile, dt):
    if tile + dt>= 0 and tile+dt<last and (not tile+ dt in visited) and tiles[tile][bool(dt+1)] == tiles[tile+dt][bool(dt-1)] and where[tile] == where[tile+dt] :
        t.append(tile+dt)
        visited.add(tile+dt)
        before[tile+dt] = tile
while q:
    tile= q.pop()
    if tile == last-1: break
    checkupdown(tile, UP, 0)
    checkupdown(tile, UP, 1)
    checkupdown(tile, DOWN, 0)
    checkupdown(tile, DOWN, 1)
    checkleftright(tile, +1)
    checkleftright(tile, -1) 
    if not q:
        q = t
        t = []
if tile != last-1:
    tile = max(visited)
p = tile
path = [p+1]
while p:
    path.append(before[p]+1)
    p = before[p]
print(len(path))
print(" ".join(map(str, path[::-1])))