tiles = set(range(1,201))
def solution(board):
    answer = 0
    for black in range(400, 700):
        ret = blackDown(board, black)
        if not ret : break
        answer += ret
    return answer



def blackDown(board, black):
    N=len(board)
    blackPositions = []
    for i in range(N):
        for j in range(N):
            if board[j][i] in tiles: break
        else: continue
        for k in range(max(j-2,0), j):
            board[k][i] = black
            blackPositions.append((k,i))
    return destroy(board, black, blackPositions)
from collections import defaultdict as dd
def destroy(board, black, blackPositions):
    destroyed = 0
    N=len(board)
    for x,y in blackPositions:
        if x <N-2 and y<N-1 and board[x][y+1] in tiles:
            tileSet = dd(int)
            for i in range(2):
                for j in range(3):
                    tileSet[board[x+j][y+i]] += 1
            if tileSet[black] ==2 and tileSet[board[x][y+1]] ==4:
                destroyed += 1
                for i in range(2):
                    for j in range(3):
                        board[x+j][y+i] = 0
                continue
        if x < N-1 and y<N-2 and board[x+1][y] in tiles:
            tileSet = dd(int)
            for i in range(2):
                for j in range(3):
                    tileSet[board[x+i][y+j]] += 1
            if tileSet[black] ==2 and tileSet[board[x+1][y]] ==4:
                destroyed += 1
                for i in range(2):
                    for j in range(3):
                        board[x+i][y+j] = 0
                continue
        if x < N-2 and y >0 and board[x][y-1] in tiles:
            tileSet = dd(int)
            for i in range(2):
                for j in range(3):
                    tileSet[board[x+j][y-i]] += 1
            if tileSet[black] ==2 and tileSet[board[x][y-1]] ==4:
                destroyed += 1
                for i in range(2):
                    for j in range(3):
                        board[x+j][y-i] = 0
                continue
        if x <N-1 and y>1 and board[x+1][y] in tiles:
            tileSet = dd(int)
            for i in range(2):
                for j in range(3):
                    tileSet[board[x+i][y-j]] += 1
            if tileSet[black] ==2 and tileSet[board[x+1][y]] ==4:
                destroyed += 1
                for i in range(2):
                    for j in range(3):
                        board[x+i][y-j] = 0
                continue
    return destroyed
                
            
            
            
            
            