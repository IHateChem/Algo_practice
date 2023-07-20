import sys
input = sys.stdin.readline
N=int(input())
MAP=[list(map(int, input().split())) for _ in range(N)]
for i  in range(N):
    for j in range(N):
        if MAP[i][j] == 9:
            x, y = i,j
            MAP[x][y] = 0
q = [(x,y)]; food = []; next=set(); level=2; exp=0; answer=0;history =set();count=0
def levelup(level, exp):
    exp += 1
    if level == exp:
        exp = 0
        level += 1
    return level, exp
canMove = lambda  x,y,dx,dy: 0<=x+dx<N and 0<=y+dy<N and MAP[x+dx][y+dy] <= level and not (x+dx,y+dy) in history
canEat = lambda x,y: MAP[x][y] < level and MAP[x][y]
while q:
    x, y = q.pop()
    history.add((x,y))
    for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
        if not canMove(x,y,dx,dy): continue
        if canEat(x+dx,y+dy):
            food.append((x+dx, y+dy))
        next.add((x+dx, y+dy))
    if q: continue
    if food:
        x,y = sorted(food)[0]
        level, exp = levelup(level, exp)
        answer += count + 1
        MAP[x][y] = 0
        q = [(x,y)]
        next = set()
        history = set()
        food = []
        count = 0
    else:
        q = list(next)
        next = set()
        count += 1
print(answer)