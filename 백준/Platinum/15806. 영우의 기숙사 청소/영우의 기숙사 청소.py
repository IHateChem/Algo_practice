import sys
input = sys.stdin.readline

N,M,K,T = map(int,input().split())

Molds = sorted([tuple(map(int,input().split())) for _ in range(M)])

Cleans = [list(map(int,input().split())) for _ in range(K)]

MoldsPeriod = [Molds]
inbound = lambda x, y: 0<x<=N and 0<y<=N
while 1:
    t = set()
    for x, y in MoldsPeriod[-1]:
        for dx ,dy in ((2,1), (2,-1), (-2,1), (-2,-1), (1,2), (1,-2), (-1,2), (-1,-2)):
            if not inbound(x+dx, y+dy): continue
            t.add((x+dx, y+dy))
    MoldsPeriod.append(sorted(list(t)))
    if len(MoldsPeriod) > 2 and MoldsPeriod[-3] == MoldsPeriod[-1]: break
if T > len(MoldsPeriod):
    if T % 2 == len(MoldsPeriod)%2: t = -2
    else: t = -1
else:
    t = T
for x, y in Cleans:
    for a, b in MoldsPeriod[t]:
        if (x,y) == (a,b):
            print("YES")
            exit(0)
print("NO")