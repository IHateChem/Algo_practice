#bfs
import sys
sys.setrecursionlimit(3000000)
input = sys.stdin.readline
answer = 0
m,n = map(int,input().split())
MAP = [list(map(int,input().strip())) for _ in range(m)]
fungus = [(MAP[i][j], i, j) for i in range(m) for j in range(n) if MAP[i][j]]
inbound = lambda x, y: 0<=x<m and  0<=y<n
t = []
def bfs(i, j, visited):
    for di, dj in ((-1,0), (1,0), (0,1), (0,-1)):
        if not inbound(i+di, j+dj) or (i+di, j+dj) in visited: continue
        if MAP[di+i][j+dj]:
            visited.add((i+di, j+dj))
            bfs(i+di, j+dj, visited)
def check():
    visited = set()
    flag = True
    for i in range(m):
        for j in range(n):
            if flag and MAP[i][j]:
                bfs(i,j, visited)
                flag = False
            elif MAP[i][j] and not (i,j) in visited:
                return False
    return True
if check():
    print(0)
    exit(0)

while fungus:
    v, r, c = fungus.pop()
    for i in range(2*v+1):
        for j in range(2*v+1):
            if inbound(r-v+i, c-v+j) and MAP[r-v+i][c-v+j] < v:
                MAP[r-v+i][c-v+j] = v
                t.append((v, r-v+i, c-v+j))
    if not fungus:
        answer += 1
        if check():
            print(answer)
            break
        fungus = t
        t = []