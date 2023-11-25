import sys
input = sys.stdin.readline
N,M,H = map(int,input().split())
MAP = [[0]*(H) for _ in range(N-1)]
for _ in range(M):
    a, b=  map(int,input().split())
    MAP[b-1][a-1] = 1
def calc():
    start = list(range(N))
    for i in range(H):
        for j in range(N-1):
            if MAP[j][i]: start[j], start[j+1] = start[j+1], start[j]
    if start == list(range(N)): return True
    else: return False
def check(i, j):
    if (0<i<N-1 and MAP[i-1][j]) or (0<=i<N-2 and MAP[i+1][j]): return True
    return False
idx2pos = [(i%H, i//H) for i in range(H*(N-1))]
if calc():
    print(0)
    exit(0)
else:
    for i,j in idx2pos:
        if MAP[j][i] or check(j,i): continue
        MAP[j][i] = 1
        if calc():
            print(1)
            exit(0)
        MAP[j][i] = 0
    for x in range(H*(N-1)):
        i, j = idx2pos[x]
        if MAP[j][i] or check(j,i): continue
        MAP[j][i] = 1
        for y in range(x+1,H*(N-1)):
            k, m = idx2pos[y]
            if MAP[m][k] or check(m,k): continue
            MAP[m][k] = 1
            if calc():
                print(2)
                exit(0)
            MAP[m][k] = 0
        MAP[j][i] = 0
    for x in range(H*(N-1)):
        i, j = idx2pos[x]
        if MAP[j][i] or check(j,i): continue
        MAP[j][i] = 1
        for y in range(x+1,H*(N-1)):
            k, m = idx2pos[y]
            if MAP[m][k] or check(m,k): continue
            MAP[m][k] = 1
            for z in range(y+1,H*(N-1)):
                a, b = idx2pos[z]
                if MAP[b][a] or check(b,a): continue
                MAP[b][a] = 1
                if calc():
                    print(3)
                    exit(0)
                MAP[b][a] = 0
            MAP[m][k] = 0
        MAP[j][i] = 0
print(-1)