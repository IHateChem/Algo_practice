import sys
input = sys.stdin.readline
N,M,K=map(int, input().split())
MAP = [[[] for i in range(N)] for _ in range(N)]
NEWMAP =  [[[] for i in range(N)] for _ in range(N)]
delta = [(-1,0),(-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), ((-1,-1))]
for _ in range(M):
    r,c,m,s,d = map(int,input().split())
    MAP[r-1][c-1].append((m,s,d))
def move(r,c,m,s,d):
    r += delta[d][0]*s 
    c += delta[d][1]*s
    r %= N
    c %= N
    NEWMAP[r][c].append((m,s,d))
def split(r,c):
    sumWeight=0
    sumSpeed=0
    p = NEWMAP[r][c][0][2]
    isEven = True
    for m,s,d in NEWMAP[r][c]:
        sumWeight+=m
        sumSpeed+=s
        if(p%2 != d %2): isEven = False
        p = d
    weight = sumWeight//5
    speed = sumSpeed // len(NEWMAP[r][c])
    if weight < 1: dirs = () 
    elif isEven: dirs = (0,2,4,6)
    else: dirs = (1,3,5,7)
    for d in dirs:
        MAP[r][c].append((weight, speed ,d))
        
def clear(MAP):
    for i in range(N):
        for j in range(N):
            MAP[i][j] = []
for _ in range(K):
    for i in range(N):
        for j in range(N):
            if MAP[i][j]:
                for k in MAP[i][j]:
                    move(i,j,*k)
    clear(MAP)
    for i in range(N):
        for j in range(N):
            if len(NEWMAP[i][j]) > 1:
                split(i,j)
            elif NEWMAP[i][j]:
                MAP[i][j] = NEWMAP[i][j]
    clear(NEWMAP)
answer =0
for i in range(N):
    for j in range(N):
        for m,s,d in MAP[i][j]:
            answer += m
print(answer)