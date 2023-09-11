import sys
input=sys.stdin.readline
key=list(input().strip())
engel=list(input().strip())
devil=list(input().strip())
K=len(key);N=len(engel)
dp1=[[0]*(K+1) for _ in range(N)]
dp2=[[0]*(K+1) for _ in range(N)]
for i in range(N):
    for k in range(K):
        if engel[i] == key[k]:
            if k == 0:
                dp1[i][k] = dp1[i-1][k]+1
            else:
                dp1[i][k] = dp1[i-1][k]+dp2[i-1][k-1]
        else:
            dp1[i][k] = dp1[i-1][k]
        if devil[i] == key[k]:
            if k == 0:
                dp2[i][k] = dp2[i-1][k]+1
            else:
                dp2[i][k] = dp2[i-1][k]+dp1[i-1][k-1]
        else:
            dp2[i][k] = dp2[i-1][k]
print(dp1[-1][-2]+dp2[-1][-2])