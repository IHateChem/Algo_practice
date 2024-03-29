#맵제한이 문제와 다른듯, 50이 아니라 102로 했더니 런타임 오류없이 통과
N = 102
def isin(rectangle, x, y, dx, dy):
    b4_after =  [(x-dx, y-dy), (x, y)]
    b4_after.sort()
    for x1, y1, x2, y2 in rectangle:
        if x1 < x and x < x2 and y1 < y and y < y2: break
        if b4_after[0][0] == x1 and b4_after[1][0] == x2 and y1 < y and y < y2: break
        if b4_after[0][1] == y1 and b4_after[1][1] == y2 and x1 < x and x < x2: break
    else: return False
    return True
def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    MAP_X = [[0]*N for _ in range(N)]
    visited = [[0 for i in range(N)] for j in range(N)]
    MAP_Y = [[0]*N for _ in range(N)]
    for x1, y1, x2, y2 in rectangle:
        for i in range(x1, x2):
            MAP_X[i][y1] = 1
            MAP_X[i][y2] = 1
        for j in range(y1, y2):
            MAP_Y[x1][j] = 1
            MAP_Y[x2][j] = 1
    stack = [(characterX, characterY)]
    t = []
    visited[characterX][characterY] = 1
    while stack:
        x, y = stack.pop()
        if x == itemX and y == itemY: break
        if x+1 < N and MAP_X[x][y] and not visited[x+1][y] and not isin(rectangle, x+1, y, 1, 0):
            t.append((x+1, y))
            visited[x+1][y] = 1
        if x-1 >= 0 and MAP_X[x-1][y] and not visited[x-1][y] and not isin(rectangle, x-1, y, -1, 0):
            t.append((x-1, y))
            visited[x-1][y] = 1
        if y+1 < N and MAP_Y[x][y] and not visited[x][y+1] and not isin(rectangle, x, y+1, 0, 1):
            t.append((x, y+1))
            visited[x][y+1] = 1
        if y-1 >= 0 and MAP_Y[x][y-1] and not visited[x][y-1] and not isin(rectangle, x, y-1, 0, -1):
            t.append((x, y-1))
            visited[x][y-1] = 1
        if not stack:
            stack = t
            t = []
            answer += 1
    return answer