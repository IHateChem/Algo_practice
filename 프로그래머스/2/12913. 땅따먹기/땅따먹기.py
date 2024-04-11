def solution(land):
    dp = [[0] * 4 for _ in range(len(land))]
    for i in range(4): dp[0][i] = land[0][i]
    for i in range(1, len(land)):
        for j in range(4):
            t = 0
            for k in range(4):
                if j== k: continue
                t = max(t, dp[i-1][k])
            dp[i][j] = t + land[i][j]
    return max(dp[-1])