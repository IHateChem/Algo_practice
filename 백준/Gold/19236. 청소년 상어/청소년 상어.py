import sys
input = sys.stdin.readline
sea = []
direction = {1 : (-1,0), 2: (-1,-1), 3: (0,-1), 4:(1,-1), 5: (1, 0), 6: (1,1), 7:(0,1), 8:(-1, 1)}
alive = set(range(1, 17))
position = {}

def die(n):
    alive.remove(n)
def change(dir, n, pos, sea):
    pos[n][2] = dir
    sea[pos[n][0]][pos[n][1]][1] = dir
def move(n, shark_pos, position, sea):
    for i in range(8):
        x, y, dir = position[n]
        dx, dy = direction[dir]
        if (x+dx, y+dy) == shark_pos or x+dx < 0 or x+dx == 4 or y+dy <0 or y+dy == 4:
            dir = dir%8 + 1
            change(dir, n, position, sea)
            continue
        sea[x+dx][y+dy], sea[x][y] = sea[x][y], sea[x+dx][y+dy]
        position[n] = [x+dx, y+dy, dir]
        position[sea[x][y][0]] = [x, y, sea[x][y][1]]
        break
for i in range(4):
    a,b,c,d,e,f,g, h =map(int, input().split())
    sea.append([[a,b], [c,d], [e,f],[g,h]])
    for j, [n, dir] in enumerate(sea[-1]): position[n] = [i,j, dir]
n, dir = sea[0][0]
first = n
x, y = 0, 0
die(n)
def eat(x,y, dir, sea):
    dx, dy = direction[dir]
    target = []
    for i in range(1,4):
        if x+dx*i < 0 or x+dx*i == 4 or y+dy*i <0 or y+dy*i == 4: break
        if sea[x+dx*i][y+dy*i][0] in alive:
            target.append(sea[x+dx*i][y+dy*i][0])
    return target
from copy import deepcopy
def episode(x, y, dir, position, sea):
    ans = 0
    for i in range(1, 17):
        if i in alive:
            move(i, (x,y), position, sea)
    targets = eat(x, y, dir, sea)
    for i in targets:
        x, y, dir = position[i]
        die(i)
        pos = deepcopy(position)
        s = deepcopy(sea)
        ans = max(ans, i+episode(x, y, dir, position, sea))
        alive.add(i)
        position = pos
        sea = s
    return ans
print(first+episode(x, y, dir, position, sea))