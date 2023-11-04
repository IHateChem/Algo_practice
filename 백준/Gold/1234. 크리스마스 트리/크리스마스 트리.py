import sys
import itertools
from itertools import combinations as C
input=sys.stdin.readline
N,R,G,B=map(int,input().split())
dp = [[[[0 for _ in range(B+1)]for _ in range(G+1)]for _ in range(R+1)] for _ in range(N+1)]
dp[0][-1][-1][-1] = 1
for n in range(N):
    for r in range(R+1):
        for g in range(G+1):
            for b in range(B+1):
                if dp[n][r][g][b]:
                    half = (n + 1) // 2
                    oneThird=  (n+1) //3
                    if n % 3 == 2:
                        if r >= oneThird and g >= oneThird and b >= oneThird:
                            dp[n+1][r-oneThird][g-oneThird][b-oneThird] +=  len(list(C(range(n+1),oneThird))) * len(list(C(range(n+1-oneThird),oneThird)))* dp[n][r][g][b]
                    if n % 2 == 1:
                        if r >= half and g >= half:
                            dp[n+1][r-half][g-half][b] += len(list(C(range(n+1),half)))* dp[n][r][g][b]
                        if r >= half and b >= half:
                            dp[n+1][r-half][g][b-half] +=  len(list(C(range(n+1),half)))* dp[n][r][g][b]
                        if g >= half and b >= half:
                            dp[n+1][r][g-half][b-half] += len(list(C(range(n+1),half)))*dp[n][r][g][b]
                    if r > n:
                        dp[n+1][r-n-1][g][b] += dp[n][r][g][b]
                    if g > n:
                        dp[n+1][r][g-n-1][b] += dp[n][r][g][b]
                    if b > n:
                        dp[n+1][r][g][b-n-1] += dp[n][r][g][b]
answer = 0 
for r in range(R+1):
    for g in range(G+1):
        for b in range(B+1):
            answer += dp[-1][r][g][b]
print(answer)