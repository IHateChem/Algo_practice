word=input()
N=len(word)
INF=10000000
dp = [[INF]*N for _ in range(N)]
for i in range(N):
    dp[i][i] = 0
    if i!= N-1: dp[i][i+1] = int(word[i] != word[i+1])
# dp[i][j] = dp[i][j-1]+1, dp[i+1][j]+1, dp[i+1][j-1] + word[i+1] != word[j-1] 
def solve(l, r, word):
    if dp[l][r] !=  INF: return dp[l][r]
    if l >= r: return 0
    dp[l][r] = min(solve(l,r-1, word)+1, solve(l+1, r, word)+1, solve(l+1,r-1, word) + (word[l] != word[r]))
    return dp[l][r]
ans = solve(0, N-1, word)
for i in range(N):
    for j in range(i+1, N):
        newWord = []
        for k in range(N):
            if k==i: newWord.append(word[j])
            elif k==j: newWord.append(word[i])
            else: newWord.append(word[k])   
        dp = [[INF]*N for _ in range(N)]
        for l in range(N):
            dp[l][l] = 0
            if l!= N-1: dp[l][l+1] = int(newWord[l] != newWord[l+1])
        ans=min(ans, solve(0,N-1, newWord)+1)
print(ans)