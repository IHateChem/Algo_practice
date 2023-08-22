import sys
input=sys.stdin.readline
N,M,D=map(int,input().split())
MAP=[list(map(int,input().split()))for _ in range(N)]
monsterO = set()
for i in range(N):
    for j in range(M):
        if MAP[i][j]: monsterO.add((i,j))
dist = lambda x,y,r,c : abs(x-r)+abs(y-c)
def shoot(i1,i2,i3,j1,j2,j3, monster):
    if not monster: return 0
    d1 = D+1;target1=None;d2=d1;target2=None;d3=d1;target3=None
    for i, j in monster:
        d1, target1 = canShoot(i,j,i1,j1, d1, target1)
        d2, target2 = canShoot(i,j,i2,j2, d2, target2)
        d3, target3 = canShoot(i,j,i3,j3, d3, target3)
    newMonster = set()
    for pos in monster:
        if pos in (target1, target2, target3): continue
        newMonster.add(pos)
    return len(monster) - len(newMonster), newMonster
def canShoot(i,j, r,c,d, target):
    t = dist(i,j, r, c)
    if t < d:
        d = t
        target = (i,j)
    elif t == d:
        if target and target[1] > j:
            target = (i,j)
    return d, target
def move(monster):
    newMonster = set()
    for i, j in monster:
        if i+1==N: continue
        newMonster.add((i+1,j))
    return newMonster
def score(i1,i2,i3,j1,j2,j3, monster):
    ret = 0
    while monster:
        t, monster = shoot(i1,i2,i3,j1,j2,j3, monster)
        ret += t
        monster = move(monster)
    return ret
answer = 0 
for j1 in range(M-2):
    for j2 in range(j1+1,M-1):
        for j3 in range(j2+1,M):
            monster = set([i for i in monsterO])
            answer = max(answer, score(N,N,N,j1,j2,j3, monster))
print(answer)