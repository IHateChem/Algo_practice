import sys
input= sys.stdin.readline
nextmove = [(1,0), (0,-1), (-1, 0), (0, 1)]
N = int(input())
MAP = [[0]*101 for _ in range(101)]
def copy(a):
    return [i for i in a]
def get_way(his, g):
    if g ==0: return
    t = copy(his)
    while t:
        d = t.pop()
        his.append((d+1)%4)
    return get_way(his,g-1)
def draw(x,y,stack):
    for d in stack:
        dx ,dy = nextmove[d]
        x += dx;y+=dy
        MAP[x][y] =1
for _ in range(N):
    x,y,d,g=map(int, input().split())
    MAP[x][y]=1
    stack = [d]
    get_way(stack,g)
    draw(x,y,stack)
answer = 0
for i in range(100):
    for j in range(100):
        if MAP[i][j] and MAP[i+1][j] and MAP[i][j+1] and MAP[i+1][j+1]: answer += 1
print(answer)