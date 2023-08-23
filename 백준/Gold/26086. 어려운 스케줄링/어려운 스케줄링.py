import sys
input=sys.stdin.readline
dq = []
N,Q,K=map(int,input().split())
works = [list(map(int,input().split())) for _ in range(Q)]
idx1 = max([i if q == 1 else -1 for i, (q, *p)in enumerate(works)])
for i, (q,*p) in enumerate(works):
    if i ==idx1: dq.sort(reverse=True)
    elif q==0: dq.append(p[0])
    elif i>idx1: dq.reverse()
print(dq[::-1][K-1])