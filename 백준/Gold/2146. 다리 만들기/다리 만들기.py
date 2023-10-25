import sys

sys.setrecursionlimit(300000)
input = sys.stdin.readline
N=int(input())
MAP=[list(map(int,input().split())) for _ in range(N)]
visited = set()
inbound = lambda i,j: 0<=i<N and 0<=j<N
def dfsFirst(i, j, index):
    if (i,j) in visited or not MAP[i][j]: return index
    visited.add((i,j))
    MAP[i][j] = index
    for di, dj in [(0,1),(1,0),(-1,0),(0,-1)]:
        ni, nj = i+di, j+dj
        if inbound(ni,nj) and MAP[ni][nj] and not (ni,nj) in visited:
            dfsFirst(ni,nj, index)
    return index + 1
idx = 1
for i in range(N):
    for j in range(N):
        idx = dfsFirst(i,j, idx)
q = [(v, MAP[v[0]][v[1]]) for v in visited]
answer = 0
t =[]
while q:
    pos, color = q.pop()
    i,j = pos
    if MAP[i][j] and MAP[i][j] != color: break
    for di, dj in [(0,1),(1,0),(-1,0),(0,-1)]:
        ni, nj = i+di, j+dj
        if inbound(ni,nj) and not ((ni,nj), color) in visited:
            visited.add(((ni,nj), color))
            t.append(((ni,nj), color))
    if not q:
        q = t
        t = []
        answer += 1
print(answer-1)