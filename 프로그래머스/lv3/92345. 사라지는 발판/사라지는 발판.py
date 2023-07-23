answer = 1000
INF =  100000000
def canmove(loc, eloc, dx, dy):
    x = loc[0] +dx
    y = loc[1] +dy
    return 0<=x<X and 0<=y<Y and board[x][y]
board = []
X=0;Y=0

def move(aloc, bloc, n):
    flag = True
    results = []
    a = n
    for dx, dy in ((0,-1), (0,1), (-1,0),(1,0)):
        if not canmove(aloc, bloc, dx, dy): continue
        flag = False
        if aloc == bloc:
            return False, n + 1
        board[aloc[0]][aloc[1]] = 0
        aloc[0] += dx
        aloc[1] += dy
        results.append(move(bloc, aloc, n+1))
        aloc[0] -= dx
        aloc[1] -= dy
        board[aloc[0]][aloc[1]] = 1
    if flag:
        return True, n
    else:
        w = INF
        l = 0
        for r in results:
            if r[0]:
                w = min(w, r[1])
            else:
                l = max(l, r[1])
        if w != INF:
            return False, w
        else:
            return True, l

def solution(Board, aloc, bloc):
    global board
    board =Board
    global X
    X = len(board)
    global Y
    Y = len(board[0])
    answer = move(aloc, bloc, 0)[1]
    return answer
