import sys
input = sys.stdin.readline
N = int(input())
dp = [0]*(N+3)
bf = 0
for i in range(N):
    dp[i] = max(dp[i-1]+1, dp[i])
    t = dp[i]
    dp[i+3] = max(dp[i+3], t*2)
    for j in range(4, N-i):
        dp[i+j] = max((j-1)*t, dp[i+j])
print(dp[N-1])