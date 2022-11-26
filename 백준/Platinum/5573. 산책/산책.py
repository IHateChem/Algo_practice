import sys
input = sys.stdin.readline
H, W, N = map(int, input().split())
infor = []
for _ in range(H):
    infor.append(list(map(int, input().split())))
dp = [[0]*(W+1) for _ in range(H+1)]
dp[1][1] = N-1
for i in range(2, H+1):
    dp[i][1] = dp[i-1][1]//2 
    if dp[i-1][1] % 2 == 1: dp[i][1] += (infor[i-2][0]+1)%2
for j in range(2, W+1):
    dp[1][j] = dp[1][j-1]//2 
    if dp[1][j-1] % 2 == 1: dp[1][j] += infor[0][j-2]
for i in range(2, H+1):
    for j in range(2, W+1):
        dp[i][j] = dp[i][j-1]//2  + dp[i-1][j]//2
        if dp[i][j-1] % 2 == 1: dp[i][j] += infor[i-1][j-2]
        if dp[i-1][j] % 2 == 1: dp[i][j] += (infor[i-2][j-1]+1)%2
for i in range(1, H+1):
    for j in range(1, W+1):
        if dp[i][j] % 2 == 1: 
            infor[i-1][j-1] = (infor[i-1][j-1]+1)%2
x = 1; y =1
while x <= H and y <= W:
    if infor[x-1][y-1] == 1: y +=1
    else: x += 1
print("{} {}".format(x,y))