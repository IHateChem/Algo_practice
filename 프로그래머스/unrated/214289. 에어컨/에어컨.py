INF  = 10000000
def solution(temperature, t1, t2, a, b, onboard):
    dp = [[INF] * 51 for _ in range(len(onboard)+1)]
    dp[0][temperature+10] = 0
    for i in range(1, len(onboard)+1):
        for j in range(51):
            if dp[i-1][j] != INF:
                if j == temperature+10:
                    dp[i][j] =min(dp[i][j] ,  dp[i-1][j])
                else:
                    dp[i][j] = min(dp[i][j] , dp[i-1][j] + b)
                if j > 0:
                    if j - 11 - temperature < 0:
                        dp[i][j-1] = min(dp[i][j-1], dp[i-1][j] + a)
                    else:
                        dp[i][j-1] = min(dp[i][j-1] , dp[i-1][j])
                if j < 50:
                    if j -9 - temperature > 0:
                        dp[i][j+1] = min(dp[i][j+1], dp[i-1][j] + a)
                    else:
                        dp[i][j+1] = min(dp[i][j+1] , dp[i-1][j])
        for j in range(51):
            if onboard[i-1]:
                if not (t1<= j-10 <= t2):
                    dp[i][j] = INF

    answer = min(dp[len(onboard)])
    return answer