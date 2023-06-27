import sys
input = sys.stdin.readline
# Anm = min(Ank+Ak+1m + sum(C[n:m]))
T = int(input())
for _ in range(T):
    K = int(input())
    C = list(map(int, input().split()))
    dp = [[50000000]*K for i in range(K)]
    S =[C[0]]
    for i in range(1,K):
        S.append(S[i-1]+C[i])
    S.append(0)
    for i in range(K):
        dp[i][i] = 0
    for n in range(K-1, -1, -1):
        for m in range(n+1, K):
            s = S[m]-S[n-1]
            for j in range(n, m):
                dp[n][m] = min(dp[n][m], dp[n][j]+dp[j+1][m]+s)
    print(dp[0][K-1])
