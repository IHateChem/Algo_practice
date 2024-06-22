# dp[a][b] a개(1~a) 사용해서 b개가 보일때 경우의수 
# dp[a+1][b] = (2a)dp[a][b] + dp[a][b-1]
def solution(n, count):
    dp = [[0]*(n+1) for _ in range(n+1)]
    dp[1][1] = 1
    for i in range(1,n):
        for j in range(i+1):
            dp[i+1][j+1] = (dp[i][j+1] * 2*i +  dp[i][j]) % 1000000007
    return dp[-1][count]