def solution(m, n, board):
    answer = 0
    board = [list(b) for b in board]
    while 1:
        t = pop(board)
        if not t: break
        answer += t
        down(board)
    return answer
def pop(board):
    m = len(board)
    n = len(board[0])
    deleted = set()
    for i in range(m-1):
        for j in range(n-1):
            if board[i][j] and board[i][j] == board[i+1][j] == board[i][j+1] == board[i+1][j+1]:
                deleted.add((i,j))
                deleted.add((i+1,j))
                deleted.add((i,j+1))
                deleted.add((i+1,j+1))
    ret = len(deleted)
    for i, j in deleted:
        board[i][j] = ""
    return ret
from collections import deque
def down(board):
    m = len(board)
    n = len(board[0])
    
    for j in range(n):
        blank = deque()
        for i in range(m-1,-1,-1):
            if not board[i][j]:
                blank.append((i,j))
            elif blank:
                (ti,tj) = blank.popleft()
                board[ti][tj] = board[i][j]
                board[i][j] = ""
                blank.append((i,j))
    
            
            
        
            