import sys
f = lambda: map(int, sys.stdin.readline().split())
N, M = f()
Hx,Hy = map(lambda t: t-1, f())
Ex,Ey = map(lambda t: t-1, f())
MAP = []
for _ in range(N):
    MAP.append(list(f()))
visited = [[[0]*2 for _ in range(M)] for i in range(N)]
stack = [(Hx, Hy, 0)]
visited[Hx][Hy][0] = 1
def checkpossible(x, y, m):
    if not MAP[x][y] and not visited[x][y][m]: return True
    if not m:
        if MAP[x][y]: return True
    return False
    
def get_next_pos(x, y, m):
    ret = []
    if x > 0:
        if m and checkpossible(x-1, y, m):
            ret.append((x-1,y,m))
            visited[x-1][y][m] = 1
        elif not m and checkpossible(x-1, y, m) and MAP[x-1][y]:
            ret.append((x-1,y,1))
            visited[x-1][y][1] = 1
        elif not m and checkpossible(x-1, y, m):
            ret.append((x-1,y,0))
            visited[x-1][y][0] = 1
    if y > 0:
        if m and checkpossible(x, y-1, m):
            ret.append((x,y-1,m))
            visited[x][y-1][m] = 1
        elif not m and checkpossible(x, y-1, m) and MAP[x][y-1]:
            ret.append((x,y-1,1))
            visited[x][y-1][1] = 1
        elif not m and checkpossible(x, y-1, m):
            ret.append((x,y-1,0))
            visited[x][y-1][m] = 1
    if x < N-1:
        if m and checkpossible(x+1, y, m):
            ret.append((x+1,y,m))
            visited[x+1][y][m] = 1
        elif not m and checkpossible(x+1, y, m) and MAP[x+1][y]:
            ret.append((x+1,y,1))
            visited[x+1][y][1] = 1
        elif not m and checkpossible(x+1, y, m):
            ret.append((x+1,y,0))
            visited[x+1][y][m] = 1
    if y < M-1:
        if m and checkpossible(x, y+1, m):
            ret.append((x,y+1,m))
            visited[x][y+1][m] = 1
        elif not m and checkpossible(x, y+1, m) and MAP[x][y+1]:
            ret.append((x,y+1,1))
            visited[x][y+1][1] = 1
        elif not m and checkpossible(x, y+1, m):
            ret.append((x,y+1,0))
            visited[x][y+1][m] = 1
    return ret
t = []
answer = 0
while stack:
    x, y, m = stack.pop()
    if x == Ex and y == Ey: break
    t.extend(get_next_pos(x, y, m))
    if not stack:
        stack = t
        t = []
        answer += 1
else:
    answer = -1
print(answer)
