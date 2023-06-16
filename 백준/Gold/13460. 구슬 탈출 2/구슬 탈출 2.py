#10번 이하. 
#빨강은 구멍에 빠져야하고 파랑은 빠지면 안됨. 
#가능한 총 개수 4^10 -> 브루트 포스일듯!
#bfs로 구현. 
import sys
input = sys.stdin.readline
left = 0; right = 1; up = 2; down = 3
baseVector = [(0,-1), (0,1), (-1,0),(1,0)]
fail = 0;  success = 1; keep = 2
directions = range(4)
def check(red, blue):
    if blue == hole: return fail
    if red == hole: return success
    return keep
def isRedFirst(direction: int, red: tuple, blue: tuple) -> tuple:
    if direction == up: ret = red[0] < blue[0]
    elif direction == down: ret = red[0] > blue[0]
    elif direction == left: ret = red[1] <blue[1]
    else: ret = red[1] > blue[1]
    return ret
def getNextPosition(direction: int, red: tuple, blue: tuple):
    dx, dy = baseVector[direction]
    rx, ry = red
    bx, by = blue
    while 1:
        if 0<=rx+dx<N and 0<=ry+dy<M and MAP[rx+dx][ry+dy] != "#":
            rx += dx; ry += dy
        else: break
        if(rx,ry) == hole: break
    while 1:
        if 0<=bx+dx<N and 0<=by+dy<M and MAP[bx+dx][by+dy] != "#":
            bx += dx; by += dy
        else: break
        if(bx,by) == hole: break
    newRed = (rx,ry); newBlue = (bx,by)
    if newRed != hole and newBlue == newRed:
        if isRedFirst(direction, red, blue):
            newBlue = (bx-dx, by-dy)
        else:
            newRed = (rx-dx, ry-dy)
    return newRed, newBlue
def tilting(red: tuple, blue: tuple) -> int:
    stack = [(red, blue)]
    t = []
    for i in range(10):
        while stack:
            red, blue = stack.pop()
            for direction in directions:
                redNext, blueNext =  getNextPosition(direction, red, blue)
                if (redNext, blueNext) in history: continue
                result = check(redNext, blueNext)
                history.add((redNext, blueNext))
                if result == success: return i+1
                if result == fail: continue
                t.append((redNext, blueNext))
        stack = t
        t = []
    return -1

N, M = map(int, input().split())
MAP = [list(input().strip()) for i in range(N)]
nextPositionMap = {(i,j) : {} for j in range(M) for i in range(N)}
history =  set()
for i in range(N):
    for j in range(M):
        if MAP[i][j] == "B": blue = (i,j)
        if MAP[i][j] == "R": red = (i,j)
        if MAP[i][j] == "O": hole = (i,j)
print(tilting(red, blue))