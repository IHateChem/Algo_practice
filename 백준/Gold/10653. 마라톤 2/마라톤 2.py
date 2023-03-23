import sys 
input = sys.stdin.readline
N, K = map(int, input().split())
checkpoints = [tuple(map(int, input().split())) for _ in " "*N]
#def getdist(x,y, r,s):return abs(x-r)+abs(y-s)
getdist = lambda x,y,r,s: abs(x-r)+abs(y-s)
INF = 1000000
dp = [[INF]*(K+1) for _ in " "*N]
dp[0][0] = 0
p = checkpoints[0]
for i in range(N):
    d = getdist(*p, *checkpoints[i])
    for j in range(K+1):
        dp[i][j] = min(dp[i][j], dp[i-1][j] + d)
    for j in range(K):
        k = 1
        while k +i+1 < N and k < K+1-j:
            dp[i+k+1][j+k] = min(dp[i+k+1][k+j], dp[i][j] +getdist(*checkpoints[i], *checkpoints[i+k+1]))
            k += 1
    p = checkpoints[i]
print(min(dp[-1]))