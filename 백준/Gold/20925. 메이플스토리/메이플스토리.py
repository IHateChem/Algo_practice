import sys
input = sys.stdin.readline
N,T = map(int, input().split())
c = []
e = []
graph = []
start = []
for _ in range(N):
    tc, te = map(int,input().split())
    if not tc: start.append(_)
    c.append(tc);e.append(te)
for _ in range(N):
    graph.append(list(map(int,input().split())))
dp = [[-1]*N for _ in range(T+1)]
for i in start:
    dp[0][i] = 0
for n in range(T):  
    for i in range(N):
        if dp[n][i] == -1: continue
        dp[n+1][i] = max(dp[n][i]+e[i],dp[n+1][i])
        for v in range(N):
            if dp[n][i] >= c[v] and n+graph[i][v] < T and dp[n+graph[i][v]][v] < dp[n][i]:
                dp[n+graph[i][v]][v] = dp[n][i]
print(max(dp[-1]))