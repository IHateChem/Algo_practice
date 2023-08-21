import sys
input=sys.stdin.readline
minDict ={2:1,3:7,4:4, 5:2,6:0,7:8}
T=int(input())
INF=100000000000000000
dp=[INF]*101
dp[0] =0;dp[6]=6
def getMax(n):
    if n % 2 == 1: return "7" + "1" *(n//2-1)
    return "1" * (n//2)    
def getMin(n):
    if dp[n] == INF:
        for i in range(2,8):
            if n-i>=0 and dp[n-i]+minDict[i]: dp[n] = min(dp[n-i]*10 + minDict[i], dp[n])
    return dp[n]
for i in range(101):
    getMin(i)
for _ in range(T):
    n = int(input())
    print(dp[n], getMax(n))