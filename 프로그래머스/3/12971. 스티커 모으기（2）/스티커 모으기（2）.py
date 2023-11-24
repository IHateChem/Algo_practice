def solution(sticker):
    if len(sticker) == 1:
        return sticker[0]
    answer = 0
    dp = [[0,0] for _ in range(len(sticker))]
    dp1 = [[0,0] for _ in range(len(sticker))]
    dp[0][0] = sticker[0]
    for i in range(len(sticker)-2):
        dp[i+1][0] = sticker[i+1] + dp[i][1]
        dp[i+1][1] = max(dp[i])
    dp[-1][1] = max(dp[-2])
    for i in range(len(sticker)-1):
        dp1[i+1][0] = sticker[i+1] + dp1[i][1]
        dp1[i+1][1] = max(dp1[i])
    return max(*dp[-1],*dp1[-1])