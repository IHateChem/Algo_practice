import sys
input=sys.stdin.readline
N=int(input())
level = list(map(int,input().split()))
power = list(map(int,input().split()))
D =int(input())
dp=[[[l for l in level] for i in range(N)] for _ in range(D+1)]
calc = lambda l1: sum(x * y for x, y in zip(l1, power))
s = calc(level)
score=[[s]*N for _ in range(D+1)]
for i in range(D):
    for j in range(N):
        for k in range(N-1):
            for m in range(1,D+1-i):
                if not dp[i][j][k] or k+m>=N: continue
                level = dp[i][j]
                level[k] -= 1
                level[k+m] += 1
                if score[i+m][j] < calc(level):
                    dp[i+m][j] = [l for l in level]
                    score[i+m][j] = calc(level)
                level[k] += 1
                level[k+m] -= 1
            if score[i+m][j] < score[i][j]:
                score[i+m][j] = score[i][j]
                dp[i+m][j] = dp[i][j]
print(max(score[-1]))