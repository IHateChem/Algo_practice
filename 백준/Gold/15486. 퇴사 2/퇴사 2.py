'''
dp: 앞에서 부터 돌면서 지금까지 n번째껄 햇을때와 안했을떄 각각의 최댓값을 기입. 
Dp[n] = max(a[n]+ dp[n+k], dp[n+1])
 O(n)

'''
import sys
from collections import defaultdict as dd
input = sys.stdin.readline
N = int(input().strip())
T = []
P = []
for i in range(N):
    t, p = map(int,input().strip().split())
    T.append(t)
    P.append(p)
DP = [0] *(N+1)
n = N-1
while n >= 0:
    if n + T[n] > N:
        DP[n] = DP[n+1]
    else:
        DP[n] = max(P[n]+DP[n+T[n]], DP[n+1])
    n -= 1
print(DP[0])