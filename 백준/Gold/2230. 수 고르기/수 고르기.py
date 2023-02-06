import sys
input=sys.stdin.readline
N,M=map(int,input().split())
A = []
for _ in range(N):
    A.append(int(input()))
A.sort()
l=0;r=0
_min = 1e11
while r < N and l < N:
    _gap=0
    while r < N and _gap < M:
        _gap = A[r] -A[l]
        r += 1
    r -= 1
    if _gap >= M:_min = min(_min,_gap)
    l+=1
print(_min)