import sys
input = sys.stdin.readline

N = int(input())
trains = [0]+list(map(int, input().split()))
max_train = int(input())

dp = [[0] * (N+1) for _ in range(3)]
cum_sum = [0] * (N+1)

for i in range(N+1):
    cum_sum[i] = cum_sum[i-1] + trains[i]

for i in range(1, 4):
    for j in range(i*max_train, N+1):
        dp[i-1][j] = max(dp[i-1][j-1], dp[i-2][j-max_train] +
                         cum_sum[j] - cum_sum[j-max_train])
print(dp[2][N])
