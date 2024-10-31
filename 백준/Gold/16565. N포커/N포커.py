N = int(input())

dp = [[0]*53 for _ in range(53)]
for i in range(53):
    dp[i][0] = 1
# i C j = i-1 C j-1 + i-1 C j
for i in range(1, 51):
    for j in range(i+1):
        dp[i][j] = (dp[i-1][j-1] + dp[i-1][j]) % 10007
answer = 0
# 포함 배제의 원리
for i in range(N//4):
    answer = (answer + (-1)**i * dp[13][i+1] * dp[52-4*(i+1)][N-4*(i+1)]) % 10007
print(answer)