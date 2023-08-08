N,M=map(int,input().split())
MAP=[list(input()) for _ in range(M)]
n =1
for i in range(M):
    for j in range(N):
        if MAP[i][j] == "X":
            MAP[i][j] = n
            n *= 2
        elif MAP[i][j] == ".":
            MAP[i][j] = 0
        elif MAP[i][j] == "S":
            x=i;y=j
            MAP[i][j] = 0
        elif MAP[i][j] == "E":
            endx= i
            endy = j
            MAP[i][j] = 0
INF=10000000
dp = [[[INF]*n for j in range(N)] for _ in range(M)]
q = [(0,x, y)]; answer=0;t=[]
while q:
    bit, x, y = q.pop()
    if x ==endx and y == endy and bit == n-1:
        break
    for dx, dy in ((-1,0),(1,0),(0,1),(0,-1)):
        if 0<=x+dx<M and 0<=y+dy<N and MAP[x+dx][y+dy] != "#":
            newbit = bit | MAP[x+dx][y+dy]
            if dp[x+dx][y+dy][newbit] > answer:
                dp[x+dx][y+dy][newbit] = answer
                t.append((newbit, x+dx, y+dy))
    if not q:
        q = t
        t = []
        answer += 1
print(answer)