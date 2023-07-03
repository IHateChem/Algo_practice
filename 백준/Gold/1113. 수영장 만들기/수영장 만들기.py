import sys
input=sys.stdin.readline
N,M=map(int,input().split())
MAP=[list(map(int,input().strip())) for _ in range(N)]
scoreMap=[[0]*M for _ in range(N)]
directions=((1,0),(0,1),(-1,0),(0,-1))
def getTerritory(score, x, y):
    stack = [(x,y)]
    history = set([(x,y)])
    flag=True
    while stack:
        x,y=stack.pop()
        if not (x and y):
            flag=False
            continue
        if (x ==N-1 or y==M-1):
            flag=False
            continue
        visited.add((x,y))
        history.add((x,y))
        for dx, dy in directions:
            if not 0<=x+dx<N and 0<=y+dy<M: continue
            if (x+dx, y+dy) in visited or ( MAP[x+dx][y+dy]>score): continue
            stack.append((x+dx,y+dy))
    if flag:
        for x,y in history:
            scoreMap[x][y] = score
for s in range(1,9):
    visited = set()
    for i in range(1,N-1):
        for j in range(1,M-1):
            if (i,j) in visited: continue
            if MAP[i][j] > s: continue
            getTerritory(s, i,j)
answer = 0
for i in range(N):
    for j in range(M):
        if scoreMap[i][j]:
            answer += scoreMap[i][j] - MAP[i][j] + 1
print(answer)