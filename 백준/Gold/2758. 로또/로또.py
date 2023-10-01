import sys
input=sys.stdin.readline
T=int(input())
for _ in range(T):
    n,m=map(int,input().split())
    dp=[[0]*(m+1) for _ in range(n)]
    for i in range(max(2**(n-1),1), m+1):
        dp[0][i] = 1
    for i in range(n-1):
        for j in range(max(2**(n-i-2),1), m+1):
            for k in range(2*j,m+1):
                if not dp[i][k]: break
                dp[i+1][j] += dp[i][k]
            if not dp[i+1][j]: break
    print(sum(dp[-1]))