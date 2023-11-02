import sys
import itertools
input=sys.stdin.readline
T=int(input())
dp = [0, 1,5,11]
dp1 = [0,0,1,2]
dp2 = [0,0,1,2]
dp3 = [0,0,0,1]
dp4 = [0,0,1,1]
for i in range(30):
    dp1.append(dp2[i+3]+dp[i+2])
    dp2.append(dp1[i+3]+dp[i+2])
    dp3.append(dp4[i+3])
    dp4.append(dp3[i+3]+dp[i+2])
    dp.append(dp[i+3]+dp[i+2]+dp1[i+4]+dp2[i+4]+dp4[i+4])
for _ in range(T):
    print(dp[int(input())])