import sys
input=sys.stdin.readline
N,M,K=map(int,input().split())
candy=list(map(int,input().split()))
parent=[i for i in range(N+1)]
def union(a,b):
    pa = find(a)
    pb = find(b)
    parent[pb] = pa
def find(a):
    if parent[a] != a:
        p = find(parent[a])
        parent[a] = p
    return parent[a]
for _ in range(M):
    a,b=map(int,input().split())
    pa = find(a)
    pb = find(b)
    if pa < pb:
        union(pa,pb)
    else:
        union(pb,pa)
from collections import defaultdict as dd
groupSize = dd(int)
candySize = dd(int)
for i in range(1,N+1):
    p = find(i)
    groupSize[p] += 1
    candySize[p] += candy[i-1]
groupInfo=[]
for k in groupSize.keys():
    groupInfo.append((groupSize[k], candySize[k]))
groupInfo.sort()
dp=[[0]*(len(groupInfo)+1) for _ in range(K)]
for i in range(len(groupInfo)+1): dp[0][i]=0
for i in range(len(groupInfo)):
    g,c=groupInfo[i]
    for j in range(K):
        if j+g>=K: break
        dp[j][i+1] = max(dp[j][i+1], dp[j][i])
        dp[j+g][i+1] = max(dp[j][i] + c, dp[j+g][i+1])
print(max(dp[-1]))