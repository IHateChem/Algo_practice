n,m = map(int,input().split())
MAP = [list(map(int,input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
answer = 0
def t(x, y):
    flag = False
    pos = (x,y)
    for j in range(y, -1, -1):
        if visited[x][j]: break
        if MAP[x][j]:
            flag = True
            pos = (i,j)
    visited[x][y] = 1
    return flag, pos
for i in range(n-1, -1, -1):
    flag, pos = t(i,m-1)
    npos = pos
    if flag:
        answer += 1
        for x in range(pos[0]-1, -1, -1):
            _, npos = t(x, npos[1])
print(answer)
    