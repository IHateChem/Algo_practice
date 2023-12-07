import sys
input=sys.stdin.readline
while 1:
    n,m = map(float,input().split())
    n = int(n)
    m = int(100*m)
    if n == 0: break
    candies = []
    for _ in range(n):
        c, p = map(float,input().rstrip().rsplit())
        candies.append([int(c),int(p * 100 + 0.5)])
    dp = [0]*(m+1)
    for i in range(m+1):
        for j in range(n):
            if i+candies[j][1] > m: continue
            dp[i+candies[j][1]] = max(dp[i+candies[j][1]], dp[i] + candies[j][0])
    print(int(max(dp)))