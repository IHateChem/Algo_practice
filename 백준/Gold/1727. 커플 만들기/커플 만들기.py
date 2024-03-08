N, M = map(int,input().split())
men = sorted(list(map(int, input().split())))
women = sorted(list(map(int,input().split())))
dp = [[0]*(max(N,M)) for _ in range(min(N,M))]
smaller = men if N < M else women
bigger = men if N >= M else women
if N > M: M, N = N, M
for j in range(M):
    dp[0][j] = abs(smaller[0]-bigger[j])
for i in range(1, N):
    t_min = dp[i-1][i-1]
    for j in range(i, M):
        dp[i][j] = t_min+ abs(smaller[i]-bigger[j])
        t_min = min(t_min, dp[i-1][j])
print(min(dp[N-1][N-1:]))