import sys
input = sys.stdin.readline
w, l, d = map(float, input().split())
dp = [[0]*61 for _ in range(21)]
dp[0][40] = 1
def round(a, i):
    n = "{:.9f}".format(a)
    if int(n[-1]) >= 5:
        n = float(n[:-1]) + 0.00000001
    else:
        n = float(n[:-1])
    return "{:.8f}".format(a)
    
for i in range(20):
    for j in range(1, 60):
        dp[i+1][j-1] += l*dp[i][j]
        dp[i+1][j+1] += w*dp[i][j]
        dp[i+1][j] += d*dp[i][j]
print(round(sum(dp[-1][20:30]),8))
print(round(sum(dp[-1][30:40]),8))
print(round(sum(dp[-1][40:50]),8))
print(round(sum(dp[-1][50:60]),8))
print(round(dp[-1][60],8))