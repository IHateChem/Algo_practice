directions = [(1,0),(0,1),(-1,0),(0,-1)]
N=0
board=[]
def bfs():
    q=[(0,0,0,1)]
    visited=set([(0,0,0,1)])
    t=[]
    ret=0
    while q:
        x1,y1,x2,y2 = q.pop()
        if x2 ==N-1 and y2 ==N-1: break
        for dx,dy in directions:
            if not (0<=x1+dx and 0<= y1+dy and x2+dx<N and y2+dy<N): continue
            if not (x1+dx,y1+dy,x2+dx,y2+dy) in visited and not board[x1+dx][y1+dy] and not board[x2+dx][y2+dy]:
                visited.add((x1+dx,y1+dy,x2+dx,y2+dy))
                t.append( (x1+dx,y1+dy,x2+dx,y2+dy))
        for npos in rotate(x1,y1,x2,y2):
            if not npos in visited:
                visited.add(npos)
                t.append(npos)
        if not q:
            ret += 1
            q = t; t=[]
    return ret
def rotate(x1,y1,x2,y2):
    ret =[]
    if y1-y2 and x1 < N-1 and not board[x1+1][y1] and not board[x2+1][y2]:
        ret.append((x1,y2,x2+1,y2))
        ret.append((x1,y1,x2+1,y1))
        
    if y1-y2 and x1 > 0 and not board[x1-1][y1] and not board[x2-1][y2]:
        ret.append((x1-1,y2,x2,y2))
        ret.append((x1-1,y1,x2,y1))
    if x1-x2 and y1 < N-1 and not board[x1][y1+1] and not board[x2][y2+1]:
        ret.append((x1,y1,x1,y2+1))
        ret.append((x2,y1,x2,y1+1))
    if x1-x2 and y1 > 0 and not board[x1][y1-1] and not board[x2][y2-1]:
        ret.append((x1,y2-1,x1,y2))
        ret.append((x2,y1-1,x2,y1))
    return ret
def solution(MAP):
    global board, N
    N = len(MAP)
    board=MAP
    return bfs() 