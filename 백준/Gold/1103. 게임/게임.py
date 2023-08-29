import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
N,M=map(int,input().split())
MAP=[list(input().strip()) for _ in range(N)]
dp=[[0]*M for _ in range(N)]
direction=[(1,0),(-1,0),(0,1),(0,-1)]
inbound = lambda x,y : 0<=x<N and 0<=y<M
def sol(i,j,n):
    if (not inbound(i,j)) or MAP[i][j] == "H": return 0
    if n>N*M+1:
        print(-1)
        exit(0)
    if dp[i][j]: return dp[i][j]
    t = 0
    dist=int(MAP[i][j])
    for dir in range(4):
        di,dj=direction[dir]
        t = max(t, sol(i+di*dist, j+dj*dist,n+1)+1)
    dp[i][j] = t
    return t
print(sol(0,0,0))