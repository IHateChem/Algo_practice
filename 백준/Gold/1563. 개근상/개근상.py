n=int(input())
dp=[[1,0,0]]
dp2=[[0,0,0]]
for i in range(n):
    t = [0,0,0]
    t[0] = sum(dp[i])
    t[1] = dp[i][0]
    t[2] = dp[i][1]
    dp.append(t)
    t = [0,0,0]
    t[0] = sum(dp[i]) + sum(dp2[i])
    t[1] = dp2[i][0]
    t[2] = dp2[i][1]
    dp2.append(t)
print((sum(dp[-1])+sum(dp2[-1]))%1000000)