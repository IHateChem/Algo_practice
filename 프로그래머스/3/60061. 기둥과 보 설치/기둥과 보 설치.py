def solution(n, build_frame):
    building = [[[0]*(n+1) for _ in range(n+1)] for _ in range(2)]
    def check():
        for x in range(n+1):
            for y in range(n+1):
                if building[0][x][y]:
                    if y == 0 or building[0][x][y-1] or building[1][x][y] or (x != 0 and building[1][x-1][y]): pass
                    else: return False
                if building[1][x][y]:
                    if building[0][x][y-1] or building[0][x+1][y-1] or (building[1][x+1][y] and (x!=0 and building[1][x-1][y])): pass
                    else: return False
        return True
    for x,y,a,b in build_frame:
        building[a][x][y] = b
        if not check(): building[a][x][y] = not b
    return [[i,j,k] for i in range(n+1) for  j in range(n+1) for k in range(2) if building[k][i][j]]