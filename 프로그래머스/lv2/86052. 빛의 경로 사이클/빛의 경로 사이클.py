import sys
sys.setrecursionlimit(1000000)
def solution(grid):
    path = {"S": lambda d: d, "L": lambda d: (d+1)%4, "R": lambda d: (d-1)%4}
    X=len(grid)
    Y=len(grid[0])
    visited = [[[0]*4 for _ in range(Y)] for i in range(X)]
    dir = [(1,0),(0,1), (-1,0), (0,-1)]
    def light(x, y, d, n):
        visited[x][y][d] = 1
        dx, dy = dir[d]
        x=(x+dx) % X;y=(y+dy)%Y
        d=path[grid[x][y]](d)
        if visited[x][y][d]:
            return n
        else: return light(x,y,d,n+1)
    answer = []
    for i in range(X):
        for j in range(Y):
            for d in range(4):
                if not visited[i][j][d]:
                    dx,dy=dir[d]
                    answer.append(light(i,j, d, 1))
    return sorted(answer)