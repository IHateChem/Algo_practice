import sys
input = sys.stdin.readline
dir = [0, (-1,0), (1,0), (0, -1), (0,1)]
N,M,K=map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
POS = {}
for i in range(N):
    for j in range(N):
        if MAP[i][j]:
            POS[MAP[i][j]] = (i, j)
            MAP[i][j] = [MAP[i][j], K]
shark_dir = [0] + list(map(int, input().split()))
priority = [0]
die = set()
for _ in range(M):
    t = [0]
    for __ in range(4):
        t.append(list(map(int, input().split())))
    priority.append(t)
def move():
    for i in range(1, M+1):
        if i in die: continue
        x, y = POS[i]
        d = shark_dir[i]
        for ddir in priority[i][d]:
            dx, dy = dir[ddir]
            if not (0 <= x+dx < N and 0 <= y+dy < N): continue
            if not MAP[x+dx][y+dy]: break
        else:
          for ddir in priority[i][d]:
              dx, dy = dir[ddir]
              if not (0 <= x+dx < N and 0 <= y+dy < N): continue
              if MAP[x+dx][y+dy][0] == i: break
        shark_dir[i] = ddir
        POS[i] = (x+dx, y+dy)
def kill():
    t_MAP = set()
    for i in range(1,M+1):
        if i in die: continue
        p = POS[i]
        if p in t_MAP: die.add(i)
        else: t_MAP.add(p)
def smell():
    for i in range(N):
        for j in range(N):
            if MAP[i][j]:
                if MAP[i][j][1] != 1: MAP[i][j][1] -= 1
                else: MAP[i][j] = 0
    for i in range(1,M+1):
        if i in die: continue
        x, y = POS[i]
        MAP[x][y] = [i, K]
def check():
    if len(die) == M-1: return True
    return False
time = 0
while time < 1000:
    time += 1
    move()
    kill()
    smell()
    if check(): break
else:
    time = -1
print(time)