import sys
input = sys.stdin.readline
N,M,K=map(int,input().split())
MAP=[list(input().strip()) for _ in range(N)]
word = list(input().strip())
dp = [[[0]*M for _ in range(N)] for _ in range(len(word))]
for i in range(N):
    for j in range(M):
        if MAP[i][j] == word[0]:
            dp[0][i][j] = 1
for w in range(1,len(word)):
    for i in range(N):
        for j in range(M):
            if MAP[i][j] == word[w]:
                sum = 0
                for k in range(K):
                    if i+k+1 < N: sum += dp[w-1][i+k+1][j]
                    if i-k-1 >= 0: sum += dp[w-1][i-k-1][j]
                    if j+k+1 < M: sum += dp[w-1][i][j+k+1]
                    if j-k-1 >= 0: sum += dp[w-1][i][j-k-1]
                dp[w][i][j] = sum
answer = 0
for i in range(N):
    for j in range(M):
        answer += dp[-1][i][j]
print(answer) 
    