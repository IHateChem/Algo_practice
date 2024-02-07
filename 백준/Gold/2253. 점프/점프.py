import sys
input = sys.stdin.readline
N,M = map(int,input().split())
stones = set([int(input()) for i in range(M)])
dp = [{} for _ in range(N+1)] 
dp[1][0] = 0
for i in range(N+1):
    for v, n in dp[i].items():
        for dv in (-1, 0, 1):
            if v + dv < 1 or i + v + dv > N or i +v + dv in stones : continue
            if not dp[i+v+dv].get(v+dv): dp[i+v+dv][v+dv] = n + 1
            dp[i+v+dv][v+dv] = min(dp[i+v+dv][v+dv], n+1)
answer = 10000000
for v in dp[-1].values():
    answer = min(answer, v)
print(answer if answer != 10000000 else -1)