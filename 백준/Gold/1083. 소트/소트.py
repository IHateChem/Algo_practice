import sys
input = sys.stdin.readline
N = int(input())
l = list(map(int,input().strip().split()))
M = int(input())
pnt = 0
limit = M
while limit and pnt < N:
    max_v = 0
    for i in range(pnt, pnt + limit+1 if pnt + limit+1 < N else N):
        if max_v <  l[i]:
            max_v = l[i]
            t_pnt = i
    limit -= t_pnt - pnt
    if t_pnt != pnt:
        k= l[t_pnt]
        del l[t_pnt]
        l.insert(pnt, k)
    pnt += 1

print(" ".join(map(str, l)))