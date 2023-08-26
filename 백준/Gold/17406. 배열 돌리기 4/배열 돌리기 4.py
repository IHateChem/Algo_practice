import sys
input = sys.stdin.readline
N,M,K=map(int,input().split())
B=[list(map(int,input().split()))for _ in range(N)]
rotateSeq=[list(map(int,input().split()))for _ in range(K)]
def rotate(r,c,s):
    for k in range(s):
        p=A[r-1-k][c-k-2]
        for i in range(-k-1,k+1): A[r-k-2][c+i-1], p= p, A[r-k-2][c+i-1]
        for i in range(-k-1,k+1): A[r+i-1][c+k], p= p, A[r+i-1][c+k]
        for i in range(-k-1,k+1): A[r+k][c-i-1], p= p, A[r+k][c-i-1]
        for i in range(-k-1,k+1): A[r-i-1][c-k-2], p= p, A[r-i-1][c-k-2]
INF= 100000000
def minRow():
    ret = INF
    for a in A: ret = min(sum(a),ret)
    return ret
from itertools import permutations as P
answer=INF
for orders in P(range(K), K):
    A = [[k for k in i] for i in B]
    for i in orders:
        rotate(*rotateSeq[i])
    answer = min(minRow(),answer)
print(answer)