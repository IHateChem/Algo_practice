import sys
sys.setrecursionlimit(100000)
input=sys.stdin.readline
N = int(input())
forest = [list(map(int, input().split())) for i in range(N)]
p = 0
dp = [[0]*N for i in range(N)]
visited = [[0]*N for i in range(N)]
def MkDP(i, j):
    if visited[i][j]: return dp[i][j]
    t = 0
    for dx, dy in ((1,0), (-1,0), (0,1), (0,-1)):
        if i+dx < 0 or i+dx>=N or j+dy < 0 or j+dy >= N: continue
        if forest[i][j] >= forest[i+dx][j+dy]:continue
        t = max(t,MkDP(i+dx, j+dy))
    dp[i][j] = t + 1
    visited[i][j] = 1
    return dp[i][j]
answer= 0
for i in range(N):
    for j in range(N):
        if visited[i][j]:
            answer = max(dp[i][j], answer)
            continue
        MkDP(i,j)
        answer = max(dp[i][j], answer)
print(answer)